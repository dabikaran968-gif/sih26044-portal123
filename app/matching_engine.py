"""
Vector Similarity, Skill Gap Analysis & Recommendation Engine for SIH26044.
Calculates weighted match percentages, radar dimensions, and category rankings.
"""

from typing import List, Dict, Any, Tuple
import numpy as np
from app.models import JobPosting, SkillGapAnalysis, RecommendationItem
from app.taxonomy import normalize_skill_name, get_skill_category, SKILL_CATEGORIES

# Semantic dimensions for Radar Chart visualization
RADAR_DIMENSIONS = [
    "Programming",
    "Frontend",
    "Backend & APIs",
    "Database",
    "Cloud & DevOps",
    "AI & Data Science"
]

def canonicalize_list(skill_list: List[str]) -> List[str]:
    """Normalize a list of skills into canonical names."""
    canonical = []
    for s in skill_list:
        norm = normalize_skill_name(s)
        if norm and norm not in canonical:
            canonical.append(norm)
        elif s not in canonical:
            canonical.append(s)
    return canonical

def compute_dimension_scores(skills: List[str]) -> Dict[str, float]:
    """Calculates coverage score (0 to 100) across each radar dimension."""
    scores: Dict[str, float] = {}
    normalized_skills = set(canonicalize_list(skills))

    for dim in RADAR_DIMENSIONS:
        reference_pool = SKILL_CATEGORIES.get(dim, [])
        if not reference_pool:
            scores[dim] = 50.0
            continue
            
        matched_in_dim = [s for s in reference_pool if s in normalized_skills]
        # Benchmark score: 2 key skills in a dimension gives 80%, 3+ gives 100%
        count = len(matched_in_dim)
        if count == 0:
            scores[dim] = 20.0  # baseline foundational knowledge
        elif count == 1:
            scores[dim] = 60.0
        elif count == 2:
            scores[dim] = 85.0
        else:
            scores[dim] = 95.0
            
    return scores

def calculate_skill_gap(student_skills: List[str], job: JobPosting) -> SkillGapAnalysis:
    """Detailed skill gap analysis between student skills and a specific target job."""
    norm_student = set(canonicalize_list(student_skills))
    norm_required = canonicalize_list(job.required_skills)
    norm_preferred = canonicalize_list(job.preferred_skills)

    matched_required = [s for s in norm_required if s in norm_student]
    matched_preferred = [s for s in norm_preferred if s in norm_student]
    all_matched = matched_required + matched_preferred

    missing_required = [s for s in norm_required if s not in norm_student]
    missing_preferred = [s for s in norm_preferred if s not in norm_student]

    # Weighted scoring: Required skills weight = 3.0, Preferred skills weight = 1.0
    weight_req = 3.0
    weight_pref = 1.0

    total_weight = (len(norm_required) * weight_req) + (len(norm_preferred) * weight_pref)
    earned_weight = (len(matched_required) * weight_req) + (len(matched_preferred) * weight_pref)

    if total_weight > 0:
        raw_score = (earned_weight / total_weight) * 100.0
    else:
        raw_score = 50.0

    match_score = round(min(100.0, max(15.0, raw_score)), 1)

    # Missing skills structured with priority ranking
    missing_skills_data = []
    for s in missing_required:
        missing_skills_data.append({
            "name": s,
            "importance": "High",
            "domain": get_skill_category(s),
            "reason": "Mandatory role requirement"
        })
    for s in missing_preferred:
        missing_skills_data.append({
            "name": s,
            "importance": "Medium",
            "domain": get_skill_category(s),
            "reason": "Preferred / Good-to-have skill"
        })

    # Categorization as specified in PRD Section 5.4
    if match_score >= 80.0:
        category = "Safe Matches" if job.experience_level == "Fresher" and match_score >= 85.0 else "Best Fit"
    elif match_score >= 55.0:
        category = "Stretch Opportunities"
    else:
        category = "Foundation Needed"

    # Readiness Rating
    if match_score >= 80.0:
        readiness = "Placement Ready (Immediate Fit)"
    elif match_score >= 60.0:
        readiness = "Needs 1-2 Key Skills (High Potential)"
    else:
        readiness = "Requires Targeted Upskilling Roadmap"

    # Radar vectors
    student_dim_scores = compute_dimension_scores(student_skills)
    role_all_skills = norm_required + norm_preferred
    role_dim_scores = compute_dimension_scores(role_all_skills)

    radar_labels = RADAR_DIMENSIONS
    student_vector = [student_dim_scores[d] for d in radar_labels]
    # For role requirements, baseline expectation is at least 70% if present in requirement
    role_vector = []
    for d in radar_labels:
        req_in_dim = any(get_skill_category(s) == d for s in role_all_skills)
        role_vector.append(85.0 if req_in_dim else 40.0)

    # Explainability rationale
    if missing_required:
        explainability = (
            f"You matched {len(matched_required)}/{len(norm_required)} mandatory competencies. "
            f"Primary missing skill is '{missing_required[0]}'. Closing this gap can boost your score by "
            f"+{round((weight_req / total_weight) * 100, 1)}%."
        )
    elif missing_preferred:
        explainability = (
            f"Outstanding match! You fulfill 100% of mandatory prerequisites. "
            f"Learning '{missing_preferred[0]}' will give you an extra competitive edge."
        )
    else:
        explainability = "Perfect 100% technical compatibility with all posted specifications!"

    return SkillGapAnalysis(
        target_role_id=job.id,
        target_role_title=job.title,
        company=job.company,
        match_score=match_score,
        category=category,
        matched_skills=all_matched,
        missing_skills=missing_skills_data,
        radar_labels=radar_labels,
        student_vector=student_vector,
        role_vector=role_vector,
        explainability=explainability,
        readiness_rating=readiness
    )

def rank_recommendations(
    student_skills: List[str],
    all_jobs: List[JobPosting],
    sector_filter: Optional[str] = None,
    remote_only: bool = False,
    location_filter: Optional[str] = None
) -> List[RecommendationItem]:
    """Ranks all jobs against student skills and categorizes them into Best Fit, Stretch, Safe."""
    results: List[RecommendationItem] = []

    for job in all_jobs:
        # Apply filters
        if sector_filter and sector_filter.lower() != "all" and job.sector.lower() != sector_filter.lower():
            continue
        if remote_only and not job.is_remote:
            continue
        if location_filter and location_filter.lower() not in ["all", ""] and location_filter.lower() not in job.location.lower():
            continue

        gap = calculate_skill_gap(student_skills, job)
        
        results.append(RecommendationItem(
            job=job,
            match_score=gap.match_score,
            category=gap.category,
            matched_skills=gap.matched_skills,
            missing_skills=[m["name"] for m in gap.missing_skills],
            match_summary=gap.explainability
        ))

    # Sort descending by match score
    results.sort(key=lambda r: r.match_score, reverse=True)
    return results
