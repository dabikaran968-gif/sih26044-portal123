from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class Skill(BaseModel):
    name: str
    category: str
    confidence: float = 0.85
    is_implicit: bool = False
    source: Optional[str] = None  # e.g., 'direct_keyword', 'project_inference'

class ExtractedProfile(BaseModel):
    name: str = "Student Candidate"
    email: str = ""
    phone: str = ""
    department: str = "Computer Science"
    education: List[str] = []
    experience: List[str] = []
    projects: List[str] = []
    certifications: List[str] = []
    skills: List[Skill] = []
    summary: str = ""
    raw_text_length: int = 0

class JobPosting(BaseModel):
    id: str
    title: str
    company: str
    sector: str = "IT/Software"
    location: str
    is_remote: bool = False
    stipend_salary: str
    stipend_numeric: int = 25000
    duration: str = "6 Months"
    required_skills: List[str]
    preferred_skills: List[str] = []
    experience_level: str = "Fresher"
    description: str = ""
    openings: int = 5
    created_at: str = "2026-09-01"

class SkillGapAnalysis(BaseModel):
    target_role_id: str
    target_role_title: str
    company: str
    match_score: float  # 0 to 100
    category: str  # "Best Fit", "Stretch Opportunity", "Safe Match"
    matched_skills: List[str]
    missing_skills: List[Dict[str, Any]]  # [{"name": "Docker", "importance": "High", "domain": "DevOps"}]
    radar_labels: List[str]
    student_vector: List[float]
    role_vector: List[float]
    explainability: str
    readiness_rating: str  # "Ready to Apply", "Needs 1-2 Skills", "Requires Training"

class CourseRecommendation(BaseModel):
    skill: str
    course_title: str
    provider: str  # "NPTEL", "SWAYAM", "Coursera", "FreeCodeCamp", "YouTube"
    url: str
    duration: str
    level: str  # "Beginner", "Intermediate", "Advanced"
    is_free: bool = True
    certification_available: bool = True

class RecommendationItem(BaseModel):
    job: JobPosting
    match_score: float
    category: str  # "Best Fit", "Stretch Opportunity", "Safe Match"
    matched_skills: List[str]
    missing_skills: List[str]
    match_summary: str

class CandidateMatch(BaseModel):
    student_id: str
    name: str
    department: str
    batch: str
    cgpa: float
    match_score: float
    matched_skills: List[str]
    missing_skills: List[str]
    status: str = "Under Review"

class TPOBatchSummary(BaseModel):
    total_students: int
    avg_readiness: float
    placement_ready_pct: float
    dept_heatmaps: Dict[str, Dict[str, float]]
    top_missing_skills: List[Dict[str, Any]]
    students_list: List[Dict[str, Any]]
