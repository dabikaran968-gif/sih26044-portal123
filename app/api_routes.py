"""
FastAPI REST API Routes for SIH26044 Portal.
Handles Resume Parsing, Gap Analysis, Job Recommendations, Recruiter actions, and TPO Analytics.
Powered by Supabase / Neon PostgreSQL or Local SQLite fallback via app.database.
"""

from typing import List, Optional, Dict, Any
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import Response
import io
import csv

from app.models import (
    ExtractedProfile,
    JobPosting,
    SkillGapAnalysis,
    RecommendationItem,
    CourseRecommendation,
    TPOBatchSummary,
    CandidateMatch
)
from app.taxonomy import (
    SKILL_CATEGORIES,
    CANONICAL_ALIASES,
    normalize_skill_name,
    get_skill_category
)
from app.parser_engine import (
    extract_text_from_pdf_bytes,
    parse_resume_content
)
from app.matching_engine import (
    calculate_skill_gap,
    rank_recommendations
)
from app.upskilling_engine import get_upskilling_recommendations
from app.seed_data import SAMPLE_RESUMES
from app.database import (
    init_db,
    get_all_jobs,
    insert_job,
    get_all_students,
    update_or_create_application,
    get_application_statuses,
    db_type
)

router = APIRouter(prefix="/api")

# Initialize database schema and seeds
init_db()


# ==========================================
# 1. RESUME PARSER & SKILL EXTRACTION APIS
# ==========================================

@router.post("/resume/upload", response_model=ExtractedProfile)
async def upload_resume(file: UploadFile = File(...)):
    """Upload and parse a PDF/Text resume. Extracts explicit and implicit skills."""
    filename = file.filename.lower()
    content = await file.read()
    
    if filename.endswith(".pdf"):
        raw_text = extract_text_from_pdf_bytes(content)
        if not raw_text.strip():
            raise HTTPException(status_code=400, detail="Could not extract legible text from PDF. Ensure PDF is not encrypted or purely image-based.")
    else:
        try:
            raw_text = content.decode("utf-8", errors="ignore")
        except Exception:
            raise HTTPException(status_code=400, detail="Unsupported file encoding.")
            
    profile = parse_resume_content(raw_text)
    return profile

@router.get("/resume/sample/{sample_id}", response_model=ExtractedProfile)
def get_sample_resume(sample_id: str):
    """Load a pre-packaged sample resume for instant 1-click evaluation."""
    if sample_id not in SAMPLE_RESUMES:
        raise HTTPException(status_code=404, detail=f"Sample '{sample_id}' not found.")
    raw_text = SAMPLE_RESUMES[sample_id]
    profile = parse_resume_content(raw_text)
    return profile

@router.get("/skills/taxonomy")
def get_taxonomy():
    """Returns standardized NSQF-aligned categories and skills."""
    return {
        "categories": SKILL_CATEGORIES,
        "aliases_count": len(CANONICAL_ALIASES),
        "total_skills": sum(len(v) for v in SKILL_CATEGORIES.values()),
        "database_backend": db_type
    }

@router.post("/skills/normalize")
def normalize_skills(skills: List[str]):
    """Normalize input list of skills against master taxonomy."""
    results = []
    for s in skills:
        norm = normalize_skill_name(s) or s
        results.append({
            "original": s,
            "canonical": norm,
            "category": get_skill_category(norm)
        })
    return results


# ==========================================
# 2. SKILL GAP & RECOMMENDATION APIS
# ==========================================

@router.post("/gap-analysis", response_model=SkillGapAnalysis)
def run_gap_analysis(payload: Dict[str, Any]):
    """
    Computes quantifiable skill gap vector between student skills and target job.
    Payload: {"student_skills": [...], "job_id": "job-101"}
    """
    student_skills = payload.get("student_skills", [])
    job_id = payload.get("job_id")

    jobs = get_all_jobs()
    job = next((j for j in jobs if j.id == job_id), None)
    if not job:
        job = jobs[0] if jobs else None
        if not job:
            raise HTTPException(status_code=404, detail="No jobs available")

    return calculate_skill_gap(student_skills, job)

@router.post("/recommendations", response_model=List[RecommendationItem])
def get_job_recommendations(payload: Dict[str, Any]):
    """
    Ranks internships/jobs by skill match and categorizes into Best Fit, Stretch, Safe Matches.
    """
    student_skills = payload.get("student_skills", [])
    sector = payload.get("sector")
    remote_only = payload.get("remote_only", False)
    location = payload.get("location")

    jobs = get_all_jobs()
    return rank_recommendations(
        student_skills=student_skills,
        all_jobs=jobs,
        sector_filter=sector,
        remote_only=remote_only,
        location_filter=location
    )

@router.post("/upskilling", response_model=List[CourseRecommendation])
def get_upskilling_path(payload: Dict[str, Any]):
    """
    Suggests curated SWAYAM, NPTEL, and Coursera courses for missing skills.
    """
    missing_skills = payload.get("missing_skills", [])
    return get_upskilling_recommendations(missing_skills)


# ==========================================
# 3. RECRUITER & COMPANY PORTAL APIS
# ==========================================

@router.get("/recruiter/jobs", response_model=List[JobPosting])
def list_recruiter_jobs():
    """List all posted jobs/internships from database."""
    return get_all_jobs()

@router.post("/recruiter/jobs", response_model=JobPosting)
def create_job_posting(job_data: Dict[str, Any]):
    """Post a new internship/job into database."""
    jobs = get_all_jobs()
    new_id = f"job-{len(jobs) + 101}"
    new_job = JobPosting(
        id=new_id,
        title=job_data.get("title", "Software Intern"),
        company=job_data.get("company", "Tech Enterprise"),
        sector=job_data.get("sector", "IT/Software"),
        location=job_data.get("location", "Bengaluru, Karnataka"),
        is_remote=job_data.get("is_remote", False),
        stipend_salary=job_data.get("stipend_salary", "₹35,000 / month"),
        stipend_numeric=job_data.get("stipend_numeric", 35000),
        duration=job_data.get("duration", "6 Months"),
        required_skills=job_data.get("required_skills", ["Python", "SQL"]),
        preferred_skills=job_data.get("preferred_skills", ["Git"]),
        experience_level=job_data.get("experience_level", "Fresher"),
        description=job_data.get("description", "Join our fast-growing engineering team."),
        openings=job_data.get("openings", 3)
    )
    insert_job(new_job)
    return new_job

@router.get("/recruiter/candidates/{job_id}", response_model=List[CandidateMatch])
def get_ranked_candidates(job_id: str):
    """Returns ranked candidate list for a specific job posting."""
    jobs = get_all_jobs()
    job = next((j for j in jobs if j.id == job_id), None)
    if not job:
        raise HTTPException(status_code=404, detail="Job posting not found")

    students = get_all_students()
    statuses = get_application_statuses()
    candidates: List[CandidateMatch] = []

    for stu in students:
        gap = calculate_skill_gap(stu["skills"], job)
        status_key = f"{job_id}:{stu['id']}"
        curr_status = statuses.get(status_key, "Under Review")
        
        candidates.append(CandidateMatch(
            student_id=stu["id"],
            name=stu["name"],
            department=stu["dept"],
            batch=stu["batch"],
            cgpa=stu["cgpa"],
            match_score=gap.match_score,
            matched_skills=gap.matched_skills,
            missing_skills=[m["name"] for m in gap.missing_skills],
            status=curr_status
        ))

    candidates.sort(key=lambda c: c.match_score, reverse=True)
    return candidates

@router.post("/recruiter/status")
def update_candidate_status(payload: Dict[str, str]):
    """Update candidate recruitment status (e.g. 'Shortlisted', 'Interview Scheduled')."""
    job_id = payload.get("job_id")
    student_id = payload.get("student_id")
    status = payload.get("status", "Shortlisted")
    if not job_id or not student_id:
        raise HTTPException(status_code=400, detail="job_id and student_id required")
    update_or_create_application(job_id, student_id, status)
    return {"success": True, "status": status}


# ==========================================
# 4. INSTITUTION & TPO DASHBOARD APIS
# ==========================================

@router.get("/tpo/analytics", response_model=TPOBatchSummary)
def get_tpo_analytics():
    """Aggregated batch readiness metrics and department skill gap heatmap data."""
    students = get_all_students()
    total = len(students)
    if total == 0:
        return TPOBatchSummary(
            total_students=0,
            avg_readiness=0.0,
            placement_ready_pct=0.0,
            dept_heatmaps={},
            top_missing_skills=[],
            students_list=[]
        )

    avg_ready = round(sum(s["readiness_score"] for s in students) / total, 1)
    ready_count = sum(1 for s in students if s["readiness_score"] >= 75.0)
    ready_pct = round((ready_count / total) * 100.0, 1)

    # Department Heatmap
    depts = ["CSE", "IT", "AI/DS", "ECE"]
    benchmark_vectors = ["Web Dev", "Cloud & DevOps", "AI & Data Science", "Core CS", "Databases"]
    
    dept_heatmaps: Dict[str, Dict[str, float]] = {}
    for d in depts:
        dept_stus = [s for s in students if s["dept"] == d]
        if not dept_stus:
            dept_heatmaps[d] = {v: 50.0 for v in benchmark_vectors}
            continue
            
        heat: Dict[str, float] = {}
        for vec in benchmark_vectors:
            if vec == "Web Dev":
                target_keys = {"React", "Node.js", "JavaScript", "HTML5", "CSS3"}
            elif vec == "Cloud & DevOps":
                target_keys = {"Docker", "AWS", "Kubernetes", "Linux", "CI/CD"}
            elif vec == "AI & Data Science":
                target_keys = {"Python", "Machine Learning", "PyTorch", "Pandas", "NLP"}
            elif vec == "Core CS":
                target_keys = {"C++", "Data Structures & Algorithms", "Operating Systems", "Computer Networks"}
            else:
                target_keys = {"PostgreSQL", "SQL", "MongoDB", "MySQL"}

            matches = 0
            for stu in dept_stus:
                if any(s in target_keys for s in stu["skills"]):
                    matches += 1
            heat[vec] = round((matches / len(dept_stus)) * 100.0, 1)
        dept_heatmaps[d] = heat

    # Missing skill frequency across students
    all_essential = ["Docker", "AWS", "Kubernetes", "TypeScript", "PostgreSQL", "CI/CD", "System Design", "Microservices"]
    missing_counts = {}
    for sk in all_essential:
        count = sum(1 for s in students if sk not in s["skills"])
        missing_counts[sk] = round((count / total) * 100.0, 1)

    sorted_missing = sorted(
        [{"skill": k, "missing_percentage": v, "students_count": int((v / 100) * total)} for k, v in missing_counts.items()],
        key=lambda x: x["missing_percentage"],
        reverse=True
    )

    return TPOBatchSummary(
        total_students=total,
        avg_readiness=avg_ready,
        placement_ready_pct=ready_pct,
        dept_heatmaps=dept_heatmaps,
        top_missing_skills=sorted_missing,
        students_list=students
    )

@router.get("/tpo/export-csv")
def export_tpo_report():
    """Generates and downloads a CSV report of student readiness for placement audits."""
    students = get_all_students()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Student ID", "Candidate Name", "Department", "Batch", "CGPA", "Verified Skills Count", "Readiness Score (%)", "Status"])

    for s in students:
        writer.writerow([
            s["id"],
            s["name"],
            s["dept"],
            s["batch"],
            s["cgpa"],
            len(s["skills"]),
            s["readiness_score"],
            s["status"]
        ])

    csv_content = output.getvalue()
    return Response(
        content=csv_content,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=SIH26044_Student_Placement_Readiness_Report.csv"}
    )
