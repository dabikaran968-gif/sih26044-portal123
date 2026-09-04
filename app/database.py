"""
Database Adapter for SIH26044 Portal.
Supports PostgreSQL (Supabase / Neon) via SQLAlchemy & pg8000,
with automatic fallback to local SQLite when DATABASE_URL is not set.
"""

import os
import json
from typing import List, Dict, Optional, Any
from sqlalchemy import create_engine, Column, String, Integer, Float, Text, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

from app.models import JobPosting
from app.seed_data import SEEDED_JOBS, SEEDED_STUDENTS

Base = declarative_base()

# ==========================================
# SQL MODELS FOR SUPABASE / NEON POSTGRESQL
# ==========================================

class JobRecord(Base):
    __tablename__ = "jobs"

    id = Column(String(50), primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    sector = Column(String(100), default="IT/Software")
    location = Column(String(255), default="Bengaluru, Karnataka")
    is_remote = Column(Boolean, default=False)
    stipend_salary = Column(String(100), default="₹35,000 / month")
    stipend_numeric = Column(Integer, default=35000)
    duration = Column(String(50), default="6 Months")
    required_skills_json = Column(Text, default="[]")
    preferred_skills_json = Column(Text, default="[]")
    experience_level = Column(String(50), default="Fresher")
    description = Column(Text, default="")
    openings = Column(Integer, default=5)
    created_at = Column(String(50), default="2026-09-01")

class StudentRecord(Base):
    __tablename__ = "students"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    dept = Column(String(100), default="CSE")
    batch = Column(String(50), default="2026")
    cgpa = Column(Float, default=8.0)
    skills_json = Column(Text, default="[]")
    readiness_score = Column(Float, default=70.0)
    status = Column(String(100), default="Under Review")

class CandidateApplicationRecord(Base):
    __tablename__ = "candidate_applications"

    id = Column(String(100), primary_key=True, index=True)  # job_id:student_id
    job_id = Column(String(50), index=True)
    student_id = Column(String(50), index=True)
    status = Column(String(100), default="Under Review")


# ==========================================
# DATABASE INITIALIZATION & DRIVER SETUP
# ==========================================

raw_db_url = os.environ.get("DATABASE_URL", "").strip()

if raw_db_url:
    # Handle postgres:// vs postgresql:// and use pure-python pg8000 driver
    if raw_db_url.startswith("postgres://"):
        raw_db_url = raw_db_url.replace("postgres://", "postgresql+pg8000://", 1)
    elif raw_db_url.startswith("postgresql://") and not raw_db_url.startswith("postgresql+"):
        raw_db_url = raw_db_url.replace("postgresql://", "postgresql+pg8000://", 1)
    
    db_type = "Neon / Supabase PostgreSQL"
    engine = create_engine(raw_db_url, pool_pre_ping=True)
else:
    # Clean local SQLite fallback
    db_type = "Local SQLite (In-Memory / Persistent)"
    sqlite_path = os.path.join(os.path.dirname(__file__), "..", "portal.db")
    engine = create_engine(f"sqlite:///{sqlite_path}", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Create tables and seed initial jobs & students if tables are empty."""
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        # Seed Jobs if empty
        if session.query(JobRecord).count() == 0:
            for j in SEEDED_JOBS:
                rec = JobRecord(
                    id=j.id,
                    title=j.title,
                    company=j.company,
                    sector=j.sector,
                    location=j.location,
                    is_remote=j.is_remote,
                    stipend_salary=j.stipend_salary,
                    stipend_numeric=j.stipend_numeric,
                    duration=j.duration,
                    required_skills_json=json.dumps(j.required_skills),
                    preferred_skills_json=json.dumps(j.preferred_skills),
                    experience_level=j.experience_level,
                    description=j.description,
                    openings=j.openings,
                    created_at=j.created_at
                )
                session.add(rec)
            session.commit()

        # Seed Students if empty
        if session.query(StudentRecord).count() == 0:
            for s in SEEDED_STUDENTS:
                s_rec = StudentRecord(
                    id=s["id"],
                    name=s["name"],
                    dept=s["dept"],
                    batch=s["batch"],
                    cgpa=s["cgpa"],
                    skills_json=json.dumps(s["skills"]),
                    readiness_score=s["readiness_score"],
                    status=s["status"]
                )
                session.add(s_rec)
            session.commit()
    except Exception as e:
        session.rollback()
        print(f"Database init warning: {e}")
    finally:
        session.close()

def get_all_jobs() -> List[JobPosting]:
    """Retrieve all jobs from database."""
    session = SessionLocal()
    try:
        records = session.query(JobRecord).all()
        jobs = []
        for r in records:
            jobs.append(JobPosting(
                id=r.id,
                title=r.title,
                company=r.company,
                sector=r.sector,
                location=r.location,
                is_remote=r.is_remote,
                stipend_salary=r.stipend_salary,
                stipend_numeric=r.stipend_numeric,
                duration=r.duration,
                required_skills=json.loads(r.required_skills_json),
                preferred_skills=json.loads(r.preferred_skills_json),
                experience_level=r.experience_level,
                description=r.description,
                openings=r.openings,
                created_at=r.created_at
            ))
        return jobs
    finally:
        session.close()

def insert_job(job: JobPosting):
    """Insert newly posted job into database."""
    session = SessionLocal()
    try:
        rec = JobRecord(
            id=job.id,
            title=job.title,
            company=job.company,
            sector=job.sector,
            location=job.location,
            is_remote=job.is_remote,
            stipend_salary=job.stipend_salary,
            stipend_numeric=job.stipend_numeric,
            duration=job.duration,
            required_skills_json=json.dumps(job.required_skills),
            preferred_skills_json=json.dumps(job.preferred_skills),
            experience_level=job.experience_level,
            description=job.description,
            openings=job.openings,
            created_at=job.created_at
        )
        session.add(rec)
        session.commit()
    finally:
        session.close()

def get_all_students() -> List[Dict]:
    """Retrieve all students for TPO analytics."""
    session = SessionLocal()
    try:
        records = session.query(StudentRecord).all()
        students = []
        for r in records:
            students.append({
                "id": r.id,
                "name": r.name,
                "dept": r.dept,
                "batch": r.batch,
                "cgpa": r.cgpa,
                "skills": json.loads(r.skills_json),
                "readiness_score": r.readiness_score,
                "status": r.status
            })
        return students
    finally:
        session.close()

def update_or_create_application(job_id: str, student_id: str, status: str):
    """Persist candidate application status."""
    session = SessionLocal()
    try:
        app_id = f"{job_id}:{student_id}"
        rec = session.query(CandidateApplicationRecord).filter_by(id=app_id).first()
        if rec:
            rec.status = status
        else:
            rec = CandidateApplicationRecord(id=app_id, job_id=job_id, student_id=student_id, status=status)
            session.add(rec)
        session.commit()
    finally:
        session.close()

def get_application_statuses() -> Dict[str, str]:
    """Get all saved application statuses."""
    session = SessionLocal()
    try:
        records = session.query(CandidateApplicationRecord).all()
        return {r.id: r.status for r in records}
    finally:
        session.close()
