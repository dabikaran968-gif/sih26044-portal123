"""
Seeded Datasets for SIH26044 Portal.
Includes realistic internships/jobs, student cohorts for TPO analytics, and 3 sample resumes for 1-click testing.
"""

from typing import List, Dict
from app.models import JobPosting

SEEDED_JOBS: List[JobPosting] = [
    JobPosting(
        id="job-101",
        title="Full Stack Software Engineer Intern",
        company="Razorpay",
        sector="Fintech",
        location="Bengaluru, Karnataka",
        is_remote=True,
        stipend_salary="₹45,000 / month",
        stipend_numeric=45000,
        duration="6 Months",
        required_skills=["React", "Node.js", "JavaScript", "TypeScript", "PostgreSQL"],
        preferred_skills=["Docker", "AWS", "Redis"],
        experience_level="Fresher",
        description="Work on critical payment gateway infrastructure and high-throughput merchant dashboard interfaces.",
        openings=6
    ),
    JobPosting(
        id="job-102",
        title="Backend & Cloud Infrastructure Intern",
        company="Zomato Engineering",
        sector="E-Commerce",
        location="Gurugram, Haryana",
        is_remote=False,
        stipend_salary="₹50,000 / month",
        stipend_numeric=50000,
        duration="6 Months",
        required_skills=["Python", "FastAPI", "Docker", "PostgreSQL", "REST APIs"],
        preferred_skills=["Kubernetes", "Redis", "CI/CD"],
        experience_level="Fresher",
        description="Design scalable microservices supporting 100k+ concurrent delivery tracking events.",
        openings=4
    ),
    JobPosting(
        id="job-103",
        title="AI / Machine Learning Research Intern",
        company="TCS Research & Innovation",
        sector="IT/Software",
        location="Hyderabad, Telangana",
        is_remote=True,
        stipend_salary="₹38,000 / month",
        stipend_numeric=38000,
        duration="6 Months",
        required_skills=["Python", "PyTorch", "Machine Learning", "NLP", "Pandas"],
        preferred_skills=["Deep Learning", "LLMs", "Scikit-Learn"],
        experience_level="Fresher",
        description="Contribute to generative AI and domain-specific multilingual language models for Indian regional languages.",
        openings=5
    ),
    JobPosting(
        id="job-104",
        title="Frontend UI/UX Developer",
        company="Swiggy",
        sector="E-Commerce",
        location="Bengaluru, Karnataka",
        is_remote=True,
        stipend_salary="₹40,000 / month",
        stipend_numeric=40000,
        duration="3 Months",
        required_skills=["React", "Next.js", "Tailwind CSS", "JavaScript", "HTML5"],
        preferred_skills=["TypeScript", "Redux", "CSS3"],
        experience_level="Fresher",
        description="Build responsive, high-performance customer-facing discovery components with sub-second page loads.",
        openings=3
    ),
    JobPosting(
        id="job-105",
        title="Cloud DevOps & SRE Intern",
        company="Infosys Cloud Labs",
        sector="IT/Software",
        location="Pune, Maharashtra",
        is_remote=False,
        stipend_salary="₹30,000 / month",
        stipend_numeric=30000,
        duration="6 Months",
        required_skills=["Docker", "Linux", "AWS", "Git", "CI/CD"],
        preferred_skills=["Kubernetes", "Terraform", "Python"],
        experience_level="Fresher",
        description="Automate CI/CD delivery pipelines and monitor resilient multi-region cloud infrastructures.",
        openings=8
    ),
    JobPosting(
        id="job-106",
        title="Junior Data Analyst",
        company="Zerodha",
        sector="Fintech",
        location="Bengaluru, Karnataka",
        is_remote=True,
        stipend_salary="₹35,000 / month",
        stipend_numeric=35000,
        duration="6 Months",
        required_skills=["SQL", "Python", "Pandas", "Data Analysis", "NumPy"],
        preferred_skills=["PostgreSQL", "Tableau", "Machine Learning"],
        experience_level="Fresher",
        description="Extract analytical insights from billions of trade ledger entries and user portfolio interactions.",
        openings=4
    ),
    JobPosting(
        id="job-107",
        title="Systems Software & Core Engineer",
        company="ISRO Space Applications Centre",
        sector="Public Sector / PSU",
        location="Ahmedabad, Gujarat",
        is_remote=False,
        stipend_salary="₹28,000 / month",
        stipend_numeric=28000,
        duration="12 Months",
        required_skills=["C++", "Data Structures & Algorithms", "Operating Systems", "Linux", "C"],
        preferred_skills=["Computer Networks", "System Design"],
        experience_level="Fresher",
        description="Develop mission-critical telemetry ingestion software and high-reliability embedded control routines.",
        openings=10
    ),
    JobPosting(
        id="job-108",
        title="Mobile App Developer Intern (React Native)",
        company="Jio Platforms",
        sector="Telecom & Digital",
        location="Navi Mumbai, Maharashtra",
        is_remote=False,
        stipend_salary="₹32,000 / month",
        stipend_numeric=32000,
        duration="6 Months",
        required_skills=["React", "JavaScript", "TypeScript", "REST APIs"],
        preferred_skills=["Redux", "Tailwind CSS"],
        experience_level="Fresher",
        description="Help engineer consumer digital services accessed by over 450 million Indian subscribers.",
        openings=12
    )
]

# Sample Resumes for 1-Click Instant Testing
SAMPLE_RESUMES = {
    "sample_web_dev": """Aarav Sharma
Email: aarav.sharma@college.edu | Phone: +91 98765 43210 | Bengaluru, India
GitHub: github.com/aaravsharma | LinkedIn: linkedin.com/in/aaravsharma

EDUCATION
B.Tech in Computer Science and Engineering
National Institute of Technology Karnataka (NITK), Surathkal (2022 - 2026)
CGPA: 8.75 / 10.0

TECHNICAL SKILLS
- Programming Languages: JavaScript, TypeScript, Python, C++, HTML5, CSS3
- Web & Frontend: React, Next.js, Redux, Tailwind CSS, Bootstrap
- Backend & Databases: Node.js, Express, REST APIs, PostgreSQL, MongoDB
- Tools & DevOps: Git, Docker, Linux, Postman

KEY PROJECTS
1. E-Commerce Microservices Platform:
- Built responsive client portal using React, Next.js and Tailwind CSS.
- Developed scalable REST APIs using Node.js and Express with PostgreSQL database.
- Implemented JWT authentication and containerized deployment with Docker.

2. Real-Time Chat & Collaborative Canvas:
- Architected live WebSocket server with Node.js and Redis cache.
- Designed schema models in MongoDB and frontend components in React with Redux state.

EXPERIENCE & INTERNSHIPS
- Software Engineering Intern at AlphaTech Solutions (May 2025 - July 2025)
  Developed automated backend endpoints in Node.js and improved database query latency by 35%.

CERTIFICATIONS
- Meta Certified Front-End Developer (Coursera)
- NPTEL Programming in Python - Elite Medal
""",

    "sample_ai_ds": """Priya Patel
Email: priya.patel@engineering.edu | Phone: +91 98123 45678 | Hyderabad, India
GitHub: github.com/priyapatel-ai | Portfolio: priyapatel.dev

EDUCATION
B.Tech in Artificial Intelligence & Data Science
Vellore Institute of Technology (VIT), 2022 - 2026
CGPA: 9.1 / 10.0

TECHNICAL SKILLS
- Languages: Python, SQL, R, C++
- AI / ML Frameworks: PyTorch, TensorFlow, Scikit-Learn, Hugging Face Transformers
- Data & Analytics: Pandas, NumPy, Data Analysis, Computer Vision, NLP
- Databases & Tools: PostgreSQL, SQLite, Git, Linux, Jupyter

PROJECTS
1. Multilingual Indian Sentiment Classifier:
- Fine-tuned RoBERTa transformer model using PyTorch and Hugging Face.
- Preprocessed 100,000+ customer reviews using Pandas and NLTK for NLP sentiment scoring.
- Reached 94.2% validation accuracy across Hindi and English datasets.

2. Automated Defect Detection in Satellite Imagery:
- Developed CNN architecture using PyTorch for Computer Vision segmentation.
- Built interactive dashboard in Streamlit connected with PostgreSQL data warehouse.

EXPERIENCE
- Data Science Intern, Center for AI Research (Jan 2025 - May 2025)
  Executed exploratory Data Analysis and trained Random Forest / XGBoost models with Scikit-Learn.

CERTIFICATIONS
- DeepLearning.AI Deep Learning Specialization
- NPTEL Applied Machine Learning - 92% Topper
""",

    "sample_core_systems": """Rohan Verma
Email: rohan.verma@iit.ac.in | Phone: +91 97000 11223 | New Delhi, India

EDUCATION
B.Tech in Computer Science & Engineering
Delhi Technological University (DTU), 2022 - 2026 | CGPA: 8.6 / 10.0

TECHNICAL SKILLS
- Languages: C++, C, Python, Java, Bash
- Systems & Core CS: Data Structures & Algorithms, Operating Systems, Computer Networks, DBMS, System Design
- DevOps & Cloud: Linux, Docker, AWS, Git, CI/CD

PROJECTS
1. High-Performance Distributed Key-Value Store:
- Engineered in modern C++ with multithreaded network IO and Raft consensus algorithm.
- Benchmarked using Linux eBPF tools achieving 120,000 requests/sec with sub-millisecond p99.

2. Cloud CI/CD Automation Engine:
- Automated GitHub Actions deployment workflows packaging microservices into Docker images.
- Deployed instances across AWS EC2 with automatic health check monitoring.

ACHIEVEMENTS
- Solved 600+ problems on LeetCode & Codeforces (Candidate Master rating 1920)
- Finalist at Smart India Hackathon (SIH 2024)
"""
}

# 25+ Realistic Students for Institution/TPO Heatmaps & Analytics
SEEDED_STUDENTS: List[Dict] = [
    {
        "id": "STU-001", "name": "Aarav Sharma", "dept": "CSE", "batch": "2026", "cgpa": 8.75,
        "skills": ["React", "Node.js", "JavaScript", "TypeScript", "PostgreSQL", "Docker", "Tailwind CSS", "Git"],
        "readiness_score": 88.5, "status": "Ready to Apply"
    },
    {
        "id": "STU-002", "name": "Priya Patel", "dept": "AI/DS", "batch": "2026", "cgpa": 9.10,
        "skills": ["Python", "PyTorch", "Machine Learning", "Pandas", "NumPy", "SQL", "NLP", "Scikit-Learn"],
        "readiness_score": 92.0, "status": "Ready to Apply"
    },
    {
        "id": "STU-003", "name": "Rohan Verma", "dept": "CSE", "batch": "2026", "cgpa": 8.60,
        "skills": ["C++", "Data Structures & Algorithms", "Operating Systems", "Linux", "Docker", "AWS", "Git"],
        "readiness_score": 84.0, "status": "Ready to Apply"
    },
    {
        "id": "STU-004", "name": "Ananya Iyer", "dept": "IT", "batch": "2026", "cgpa": 8.40,
        "skills": ["React", "JavaScript", "HTML5", "CSS3", "Git", "Figma", "Tailwind CSS"],
        "readiness_score": 75.0, "status": "Needs 1-2 Skills"
    },
    {
        "id": "STU-005", "name": "Kavya Deshmukh", "dept": "AI/DS", "batch": "2026", "cgpa": 8.80,
        "skills": ["Python", "Pandas", "Data Analysis", "SQL", "Scikit-Learn", "Tableau"],
        "readiness_score": 81.0, "status": "Ready to Apply"
    },
    {
        "id": "STU-006", "name": "Vikram Malhotra", "dept": "ECE", "batch": "2026", "cgpa": 7.80,
        "skills": ["C", "C++", "Embedded C", "Microcontrollers", "Linux", "MATLAB"],
        "readiness_score": 68.0, "status": "Needs 1-2 Skills"
    },
    {
        "id": "STU-007", "name": "Sneha Kulkarni", "dept": "CSE", "batch": "2026", "cgpa": 8.95,
        "skills": ["Java", "Spring Boot", "REST APIs", "MySQL", "Docker", "Microservices", "Git"],
        "readiness_score": 89.0, "status": "Ready to Apply"
    },
    {
        "id": "STU-008", "name": "Aditya Nair", "dept": "IT", "batch": "2026", "cgpa": 7.90,
        "skills": ["Python", "Django", "HTML5", "CSS3", "SQLite", "Git"],
        "readiness_score": 65.0, "status": "Needs 1-2 Skills"
    },
    {
        "id": "STU-009", "name": "Tanvi Joshi", "dept": "ECE", "batch": "2026", "cgpa": 8.20,
        "skills": ["Python", "IoT", "C++", "Computer Networks", "Linux"],
        "readiness_score": 62.0, "status": "Needs 1-2 Skills"
    },
    {
        "id": "STU-010", "name": "Manish Gupta", "dept": "CSE", "batch": "2026", "cgpa": 7.40,
        "skills": ["JavaScript", "HTML5", "CSS3", "Bootstrap"],
        "readiness_score": 48.0, "status": "Requires Training"
    },
    {
        "id": "STU-011", "name": "Neha Reddy", "dept": "AI/DS", "batch": "2026", "cgpa": 8.65,
        "skills": ["Python", "TensorFlow", "Deep Learning", "Computer Vision", "Git"],
        "readiness_score": 79.0, "status": "Ready to Apply"
    },
    {
        "id": "STU-012", "name": "Rahul Meena", "dept": "IT", "batch": "2026", "cgpa": 7.60,
        "skills": ["Java", "SQL", "HTML5", "CSS3", "Git"],
        "readiness_score": 58.0, "status": "Needs 1-2 Skills"
    },
    {
        "id": "STU-013", "name": "Ishaan Choudhury", "dept": "CSE", "batch": "2026", "cgpa": 8.50,
        "skills": ["Go", "Docker", "Kubernetes", "Linux", "REST APIs", "Git"],
        "readiness_score": 86.0, "status": "Ready to Apply"
    },
    {
        "id": "STU-014", "name": "Divya Singhania", "dept": "IT", "batch": "2026", "cgpa": 8.10,
        "skills": ["React", "Node.js", "Express", "MongoDB", "JavaScript"],
        "readiness_score": 78.0, "status": "Ready to Apply"
    },
    {
        "id": "STU-015", "name": "Harshvardhan Rao", "dept": "ECE", "batch": "2026", "cgpa": 7.20,
        "skills": ["C", "Microcontrollers", "VLSI"],
        "readiness_score": 45.0, "status": "Requires Training"
    },
    {
        "id": "STU-016", "name": "Ritu Sengupta", "dept": "AI/DS", "batch": "2026", "cgpa": 8.90,
        "skills": ["Python", "Machine Learning", "NLP", "Pandas", "Scikit-Learn", "FastAPI"],
        "readiness_score": 87.0, "status": "Ready to Apply"
    },
    {
        "id": "STU-017", "name": "Karan Kapoor", "dept": "CSE", "batch": "2026", "cgpa": 7.80,
        "skills": ["Python", "Flask", "PostgreSQL", "Git"],
        "readiness_score": 64.0, "status": "Needs 1-2 Skills"
    },
    {
        "id": "STU-018", "name": "Siddharth Jain", "dept": "IT", "batch": "2026", "cgpa": 8.35,
        "skills": ["AWS", "Docker", "Linux", "Python", "CI/CD", "Git"],
        "readiness_score": 83.0, "status": "Ready to Apply"
    },
    {
        "id": "STU-019", "name": "Meera Swaminathan", "dept": "ECE", "batch": "2026", "cgpa": 8.00,
        "skills": ["Python", "C++", "IoT", "Linux", "Git"],
        "readiness_score": 66.0, "status": "Needs 1-2 Skills"
    },
    {
        "id": "STU-020", "name": "Abhishek Dubey", "dept": "CSE", "batch": "2026", "cgpa": 7.50,
        "skills": ["C++", "Data Structures & Algorithms", "SQL", "DBMS"],
        "readiness_score": 60.0, "status": "Needs 1-2 Skills"
    }
]
