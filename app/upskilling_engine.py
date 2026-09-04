"""
Curated Upskilling Engine for SIH26044.
Maps missing skills to government & MOOC courses (NPTEL, SWAYAM, Coursera, freeCodeCamp).
"""

from typing import List, Dict
from app.models import CourseRecommendation
from app.taxonomy import normalize_skill_name

# Curated catalog mapping technical skills to recognized Indian & global educational platforms
CURATED_COURSES: Dict[str, List[Dict]] = {
    "Docker": [
        {
            "course_title": "Docker for Developers & Microservices",
            "provider": "SWAYAM / NPTEL",
            "url": "https://swayam.gov.in/explorer?searchText=Docker",
            "duration": "4 Weeks (16 Hours)",
            "level": "Intermediate",
            "is_free": True,
            "certification_available": True
        },
        {
            "course_title": "Docker & Containerization Hands-on",
            "provider": "freeCodeCamp",
            "url": "https://www.youtube.com/watch?v=fqMOX6JJhGo",
            "duration": "3 Hours",
            "level": "Beginner",
            "is_free": True,
            "certification_available": False
        }
    ],
    "Kubernetes": [
        {
            "course_title": "Cloud Native Architecture & Kubernetes",
            "provider": "NPTEL / IIT Kharagpur",
            "url": "https://nptel.ac.in/courses/106105167",
            "duration": "8 Weeks",
            "level": "Advanced",
            "is_free": True,
            "certification_available": True
        }
    ],
    "AWS": [
        {
            "course_title": "Cloud Computing Infrastructure & AWS Fundamentals",
            "provider": "NPTEL / IIT Kharagpur",
            "url": "https://nptel.ac.in/courses/106105167",
            "duration": "8 Weeks",
            "level": "Intermediate",
            "is_free": True,
            "certification_available": True
        },
        {
            "course_title": "AWS Certified Cloud Practitioner Essentials",
            "provider": "Coursera",
            "url": "https://www.coursera.org/learn/aws-cloud-practitioner-essentials",
            "duration": "6 Hours",
            "level": "Beginner",
            "is_free": True,
            "certification_available": True
        }
    ],
    "PostgreSQL": [
        {
            "course_title": "Database Management System (DBMS) & Relational SQL",
            "provider": "NPTEL / IIT Madras",
            "url": "https://nptel.ac.in/courses/106106093",
            "duration": "8 Weeks",
            "level": "Intermediate",
            "is_free": True,
            "certification_available": True
        }
    ],
    "MongoDB": [
        {
            "course_title": "NoSQL Database Design & MongoDB Basics",
            "provider": "SWAYAM",
            "url": "https://swayam.gov.in/explorer?searchText=MongoDB",
            "duration": "4 Weeks",
            "level": "Beginner",
            "is_free": True,
            "certification_available": True
        }
    ],
    "React": [
        {
            "course_title": "Full Stack Web Development with React",
            "provider": "Coursera / HKUST",
            "url": "https://www.coursera.org/learn/front-end-react",
            "duration": "4 Weeks",
            "level": "Intermediate",
            "is_free": True,
            "certification_available": True
        },
        {
            "course_title": "Modern React & Hooks Course 2026",
            "provider": "freeCodeCamp",
            "url": "https://www.youtube.com/watch?v=bMknfKXIFA8",
            "duration": "12 Hours",
            "level": "Beginner",
            "is_free": True,
            "certification_available": False
        }
    ],
    "FastAPI": [
        {
            "course_title": "High-Performance REST APIs with Python & FastAPI",
            "provider": "freeCodeCamp",
            "url": "https://www.youtube.com/watch?v=0sOvCWFmrtA",
            "duration": "19 Hours",
            "level": "Intermediate",
            "is_free": True,
            "certification_available": False
        }
    ],
    "Machine Learning": [
        {
            "course_title": "Applied Machine Learning & Statistical Inference",
            "provider": "NPTEL / IIT Madras",
            "url": "https://nptel.ac.in/courses/106106198",
            "duration": "12 Weeks",
            "level": "Advanced",
            "is_free": True,
            "certification_available": True
        },
        {
            "course_title": "Machine Learning Specialization",
            "provider": "Coursera / DeepLearning.AI",
            "url": "https://www.coursera.org/specializations/machine-learning-introduction",
            "duration": "8 Weeks",
            "level": "Beginner to Intermediate",
            "is_free": False,
            "certification_available": True
        }
    ],
    "Deep Learning": [
        {
            "course_title": "Deep Learning for Computer Vision & NLP",
            "provider": "NPTEL / IIT Ropar",
            "url": "https://nptel.ac.in/courses/106106184",
            "duration": "12 Weeks",
            "level": "Advanced",
            "is_free": True,
            "certification_available": True
        }
    ],
    "PyTorch": [
        {
            "course_title": "Deep Learning with PyTorch Bootcamp",
            "provider": "freeCodeCamp",
            "url": "https://www.youtube.com/watch?v=V_xro1bcAuA",
            "duration": "24 Hours",
            "level": "Intermediate",
            "is_free": True,
            "certification_available": False
        }
    ],
    "Data Structures & Algorithms": [
        {
            "course_title": "Data Structures and Algorithms using Java/C++",
            "provider": "NPTEL / IIT Delhi",
            "url": "https://nptel.ac.in/courses/106102064",
            "duration": "12 Weeks",
            "level": "Intermediate",
            "is_free": True,
            "certification_available": True
        }
    ],
    "CI/CD": [
        {
            "course_title": "DevOps & CI/CD with GitHub Actions",
            "provider": "Coursera",
            "url": "https://www.coursera.org/learn/devops-culture-and-mindset",
            "duration": "3 Weeks",
            "level": "Beginner",
            "is_free": True,
            "certification_available": True
        }
    ],
    "TypeScript": [
        {
            "course_title": "TypeScript Complete Course 2026",
            "provider": "freeCodeCamp",
            "url": "https://www.youtube.com/watch?v=30LWjhZzg50",
            "duration": "5 Hours",
            "level": "Intermediate",
            "is_free": True,
            "certification_available": False
        }
    ]
}

def get_upskilling_recommendations(missing_skills: List[str]) -> List[CourseRecommendation]:
    """Return top curated courses for any missing skills identified in gap analysis."""
    recommendations: List[CourseRecommendation] = []
    seen_skills = set()

    for raw_skill in missing_skills:
        skill = normalize_skill_name(raw_skill) or raw_skill
        if skill in seen_skills:
            continue
        seen_skills.add(skill)

        if skill in CURATED_COURSES:
            for item in CURATED_COURSES[skill]:
                recommendations.append(CourseRecommendation(
                    skill=skill,
                    course_title=item["course_title"],
                    provider=item["provider"],
                    url=item["url"],
                    duration=item["duration"],
                    level=item["level"],
                    is_free=item["is_free"],
                    certification_available=item["certification_available"]
                ))
        else:
            # Smart government portal / SWAYAM fallback
            recommendations.append(CourseRecommendation(
                skill=skill,
                course_title=f"Mastering {skill}: Foundational & Practical Guide",
                provider="SWAYAM / NPTEL",
                url=f"https://swayam.gov.in/explorer?searchText={skill}",
                duration="4 to 8 Weeks",
                level="Beginner to Intermediate",
                is_free=True,
                certification_available=True
            ))

    return recommendations
