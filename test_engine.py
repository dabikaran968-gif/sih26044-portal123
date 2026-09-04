"""
Automated Test Suite for SIH26044 Portal AI Engine.
Tests taxonomy normalization, NLP parser, skill gap calculation, recommendations, and TPO analytics.
"""

import sys
import unittest
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.taxonomy import normalize_skill_name, get_skill_category, CANONICAL_ALIASES
from app.parser_engine import parse_resume_content, extract_explicit_skills, extract_implicit_skills
from app.matching_engine import calculate_skill_gap, rank_recommendations, compute_dimension_scores
from app.upskilling_engine import get_upskilling_recommendations
from app.seed_data import SEEDED_JOBS, SAMPLE_RESUMES, SEEDED_STUDENTS
from app.models import JobPosting

class TestSIH26044Engine(unittest.TestCase):

    def test_taxonomy_normalization(self):
        """Test canonical alias normalization across various spellings."""
        self.assertEqual(normalize_skill_name("reactjs"), "React")
        self.assertEqual(normalize_skill_name("react.js"), "React")
        self.assertEqual(normalize_skill_name("k8s"), "Kubernetes")
        self.assertEqual(normalize_skill_name("postgres"), "PostgreSQL")
        self.assertEqual(normalize_skill_name("fastapi"), "FastAPI")
        self.assertEqual(normalize_skill_name("dsa"), "Data Structures & Algorithms")
        self.assertEqual(normalize_skill_name("machine learning"), "Machine Learning")

    def test_explicit_skill_extraction(self):
        """Test explicit keyword matching in text."""
        sample_text = "Proficient in Python, React, PostgreSQL and Docker."
        skills = extract_explicit_skills(sample_text)
        skill_names = set(skills.keys())
        self.assertIn("Python", skill_names)
        self.assertIn("React", skill_names)
        self.assertIn("PostgreSQL", skill_names)
        self.assertIn("Docker", skill_names)

    def test_implicit_skill_extraction(self):
        """Test rule-based implicit skill inference from project descriptions."""
        proj_text = "Built a responsive REST API with Flask and containerized with docker compose."
        inferred = extract_implicit_skills(proj_text, "")
        inferred_names = set(inferred.keys())
        # "flask" implies Python, REST APIs; "docker compose" implies Docker, Linux
        self.assertTrue(any(s in inferred_names for s in ["Python", "REST APIs", "Docker", "Linux"]))

    def test_sample_resume_parsing(self):
        """Test parsing of the pre-loaded full stack sample resume."""
        raw_text = SAMPLE_RESUMES["sample_web_dev"]
        profile = parse_resume_content(raw_text)
        self.assertIn("Aarav", profile.name)
        self.assertEqual(profile.email, "aarav.sharma@college.edu")
        self.assertGreater(len(profile.skills), 5)
        
        extracted_names = [s.name for s in profile.skills]
        self.assertIn("React", extracted_names)
        self.assertIn("Node.js", extracted_names)
        self.assertIn("JavaScript", extracted_names)

    def test_skill_gap_analysis(self):
        """Test skill gap calculation between student skills and job."""
        job = SEEDED_JOBS[0]  # Razorpay: React, Node.js, JavaScript, TypeScript, PostgreSQL (Req) + Docker, AWS, Redis (Pref)
        student_skills = ["React", "Node.js", "JavaScript", "PostgreSQL", "Docker"]
        gap = calculate_skill_gap(student_skills, job)
        
        self.assertGreater(gap.match_score, 60.0)
        self.assertIn("React", gap.matched_skills)
        self.assertIn("PostgreSQL", gap.matched_skills)
        
        # Missing should include TypeScript (Req) and AWS (Pref)
        missing_names = [m["name"] for m in gap.missing_skills]
        self.assertIn("TypeScript", missing_names)
        self.assertIn("AWS", missing_names)
        
        # Radar dimensions
        self.assertEqual(len(gap.radar_labels), 6)
        self.assertEqual(len(gap.student_vector), 6)
        self.assertEqual(len(gap.role_vector), 6)

    def test_recommendation_ranking(self):
        """Test ranking of jobs by match score and filters."""
        student_skills = ["Python", "PyTorch", "Machine Learning", "Pandas", "SQL"]
        ranked = rank_recommendations(student_skills, SEEDED_JOBS)
        self.assertGreater(len(ranked), 0)
        
        # Top recommendation should be TCS Research (AI role) or Data Analyst
        top_job = ranked[0].job
        self.assertIn(top_job.title, ["AI / Machine Learning Research Intern", "Junior Data Analyst"])
        self.assertGreaterEqual(ranked[0].match_score, 60.0)

    def test_upskilling_recommendations(self):
        """Test course suggestions for missing skills."""
        missing = ["Docker", "Kubernetes", "AWS"]
        courses = get_upskilling_recommendations(missing)
        self.assertGreaterEqual(len(courses), 3)
        providers = [c.provider for c in courses]
        self.assertTrue(any("NPTEL" in p or "SWAYAM" in p for p in providers))

    def test_tpo_analytics_data(self):
        """Test student cohort stats for institutional dashboard."""
        self.assertGreaterEqual(len(SEEDED_STUDENTS), 20)
        cse_students = [s for s in SEEDED_STUDENTS if s["dept"] == "CSE"]
        self.assertGreater(len(cse_students), 3)

if __name__ == "__main__":
    print("=" * 60)
    print("Running SIH26044 Test Suite...")
    print("=" * 60)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSIH26044Engine)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
    print("\nAll SIH26044 unit and integration tests passed successfully!")
