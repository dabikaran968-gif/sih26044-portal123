"""
Master Skill Taxonomy & Ontology aligned with NSQF (National Skills Qualification Framework)
and Industry Standards for SIH26044.
"""

from typing import Dict, List, Optional, Tuple
import re

# Standardized Categories aligned with NSQF Level 5-7 IT-ITeS Job Roles
SKILL_CATEGORIES = {
    "Programming": [
        "Python", "Java", "C++", "C", "JavaScript", "TypeScript", "Go", "Rust", "C#", "Kotlin", "Swift", "PHP"
    ],
    "Frontend": [
        "React", "Angular", "Vue.js", "Next.js", "HTML5", "CSS3", "Tailwind CSS", "Bootstrap", "Redux", "TypeScript"
    ],
    "Backend & APIs": [
        "Node.js", "Express", "FastAPI", "Django", "Flask", "Spring Boot", "REST APIs", "GraphQL", "Microservices", "ASP.NET"
    ],
    "Database": [
        "PostgreSQL", "MongoDB", "MySQL", "Redis", "SQLite", "SQL", "Firebase", "Cassandra"
    ],
    "Cloud & DevOps": [
        "Docker", "Kubernetes", "AWS", "Google Cloud", "Microsoft Azure", "CI/CD", "Linux", "Terraform", "Git", "GitHub Actions"
    ],
    "AI & Data Science": [
        "Machine Learning", "Deep Learning", "PyTorch", "TensorFlow", "Scikit-Learn", "Pandas", "NumPy", "NLP", "Computer Vision", "Data Analysis", "LLMs"
    ],
    "Core CS & Systems": [
        "Data Structures & Algorithms", "System Design", "Operating Systems", "Computer Networks", "DBMS", "Object Oriented Programming"
    ],
    "Soft Skills & Tools": [
        "Agile", "Scrum", "Git", "Problem Solving", "Technical Writing", "Team Collaboration", "Communication"
    ]
}

# Synonyms and Canonical Alias Normalization
CANONICAL_ALIASES: Dict[str, str] = {
    # Frontend
    "react": "React",
    "reactjs": "React",
    "react.js": "React",
    "react js": "React",
    "vue": "Vue.js",
    "vuejs": "Vue.js",
    "vue.js": "Vue.js",
    "angularjs": "Angular",
    "angular": "Angular",
    "next": "Next.js",
    "nextjs": "Next.js",
    "next.js": "Next.js",
    "html": "HTML5",
    "html5": "HTML5",
    "css": "CSS3",
    "css3": "CSS3",
    "tailwind": "Tailwind CSS",
    "tailwindcss": "Tailwind CSS",
    "tailwind-css": "Tailwind CSS",
    "bootstrap": "Bootstrap",
    "redux": "Redux",

    # Backend
    "node": "Node.js",
    "nodejs": "Node.js",
    "node.js": "Node.js",
    "express": "Express",
    "expressjs": "Express",
    "express.js": "Express",
    "fastapi": "FastAPI",
    "fast-api": "FastAPI",
    "fast api": "FastAPI",
    "django": "Django",
    "flask": "Flask",
    "spring": "Spring Boot",
    "springboot": "Spring Boot",
    "spring-boot": "Spring Boot",
    "rest": "REST APIs",
    "restful": "REST APIs",
    "rest api": "REST APIs",
    "rest apis": "REST APIs",
    "restful api": "REST APIs",
    "restful apis": "REST APIs",
    "graphql": "GraphQL",
    "microservices": "Microservices",
    "microservice": "Microservices",

    # Programming
    "python": "Python",
    "python3": "Python",
    "py": "Python",
    "java": "Java",
    "c++": "C++",
    "cpp": "C++",
    "c": "C",
    "c#": "C#",
    "csharp": "C#",
    "javascript": "JavaScript",
    "js": "JavaScript",
    "typescript": "TypeScript",
    "ts": "TypeScript",
    "golang": "Go",
    "go": "Go",
    "rust": "Rust",
    "kotlin": "Kotlin",
    "swift": "Swift",

    # Databases
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "psql": "PostgreSQL",
    "mongo": "MongoDB",
    "mongodb": "MongoDB",
    "mysql": "MySQL",
    "redis": "Redis",
    "sqlite": "SQLite",
    "sqlite3": "SQLite",
    "sql": "SQL",

    # Cloud & DevOps
    "docker": "Docker",
    "containerization": "Docker",
    "containers": "Docker",
    "k8s": "Kubernetes",
    "kubernetes": "Kubernetes",
    "aws": "AWS",
    "amazon web services": "AWS",
    "gcp": "Google Cloud",
    "google cloud": "Google Cloud",
    "azure": "Microsoft Azure",
    "microsoft azure": "Microsoft Azure",
    "ci/cd": "CI/CD",
    "cicd": "CI/CD",
    "github actions": "GitHub Actions",
    "linux": "Linux",
    "ubuntu": "Linux",
    "terraform": "Terraform",
    "git": "Git",
    "github": "Git",

    # AI & Data Science
    "ml": "Machine Learning",
    "machine learning": "Machine Learning",
    "dl": "Deep Learning",
    "deep learning": "Deep Learning",
    "pytorch": "PyTorch",
    "torch": "PyTorch",
    "tensorflow": "TensorFlow",
    "tf": "TensorFlow",
    "scikit": "Scikit-Learn",
    "scikit-learn": "Scikit-Learn",
    "sklearn": "Scikit-Learn",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "nlp": "NLP",
    "natural language processing": "NLP",
    "computer vision": "Computer Vision",
    "cv": "Computer Vision",
    "llm": "LLMs",
    "llms": "LLMs",
    "large language models": "LLMs",
    "data analysis": "Data Analysis",
    "data analytics": "Data Analysis",

    # Core CS
    "dsa": "Data Structures & Algorithms",
    "data structures": "Data Structures & Algorithms",
    "algorithms": "Data Structures & Algorithms",
    "oop": "Object Oriented Programming",
    "oops": "Object Oriented Programming",
    "object oriented programming": "Object Oriented Programming",
    "dbms": "DBMS",
    "system design": "System Design",
    "os": "Operating Systems",
    "operating systems": "Operating Systems",
    "computer networks": "Computer Networks",
    "cn": "Computer Networks",

    # Soft Skills
    "agile": "Agile",
    "scrum": "Scrum",
    "problem solving": "Problem Solving",
    "communication": "Communication"
}

# Reverse lookup: skill -> category
SKILL_TO_CATEGORY: Dict[str, str] = {}
for cat, skills in SKILL_CATEGORIES.items():
    for s in skills:
        SKILL_TO_CATEGORY[s] = cat

# Implicit Skill Extraction Patterns
# When these phrases/contexts are encountered in descriptions, infer secondary implicit skills
IMPLICIT_INFERENCE_RULES = [
    {
        "pattern": r"(rest\s*api|endpoint|crud\s*api|fastapi|flask|django|express)",
        "inferred": ["REST APIs", "Backend & APIs"],
        "confidence": 0.88,
        "reason": "API development phrase found in project/experience description"
    },
    {
        "pattern": r"(flask|django|fastapi)",
        "inferred": ["Python", "Backend & APIs"],
        "confidence": 0.90,
        "reason": "Python web framework indicates Python proficiency"
    },
    {
        "pattern": r"(mern|mean\s*stack)",
        "inferred": ["MongoDB", "Express", "React", "Node.js", "JavaScript"],
        "confidence": 0.92,
        "reason": "Full stack architecture acronym implies complete MERN components"
    },
    {
        "pattern": r"(docker\s*compose|dockerfile|containeriz)",
        "inferred": ["Docker", "Linux"],
        "confidence": 0.86,
        "reason": "Containerization tooling implies Linux and Docker environment"
    },
    {
        "pattern": r"(fine-tun|llama|bert|gpt|hugging\s*face|transformer)",
        "inferred": ["NLP", "PyTorch", "Deep Learning", "LLMs"],
        "confidence": 0.89,
        "reason": "Modern transformer/LLM workflows imply PyTorch and Deep Learning"
    },
    {
        "pattern": r"(convolutional|cnn|yolo|opencv|image\s*segmentation)",
        "inferred": ["Computer Vision", "Deep Learning", "Python"],
        "confidence": 0.88,
        "reason": "Computer vision models imply Deep Learning frameworks"
    },
    {
        "pattern": r"(ci/cd|github\s*action|pipeline\s*deploy)",
        "inferred": ["CI/CD", "Git"],
        "confidence": 0.85,
        "reason": "Automated workflow pipelines imply CI/CD and version control"
    },
    {
        "pattern": r"(aws\s*s3|aws\s*ec2|aws\s*lambda|cloudformation)",
        "inferred": ["AWS", "Cloud & DevOps"],
        "confidence": 0.90,
        "reason": "Cloud infrastructure service mentions"
    },
    {
        "pattern": r"(responsive\s*design|styled-components|tailwind|flexbox)",
        "inferred": ["CSS3", "HTML5"],
        "confidence": 0.85,
        "reason": "Styling and responsive layouts require modern CSS/HTML"
    },
    {
        "pattern": r"(leetcode|codeforces|competitive\s*programming|hackerrank)",
        "inferred": ["Data Structures & Algorithms", "Problem Solving"],
        "confidence": 0.92,
        "reason": "Competitive programming directly indicates strong DSA fundamentals"
    }
]

def normalize_skill_name(raw_name: str) -> Optional[str]:
    """Resolves any variant/alias into its canonical standardized name."""
    clean = raw_name.strip().lower()
    clean = re.sub(r"[\s\-_]+", " ", clean)
    
    # Direct alias lookup
    if clean in CANONICAL_ALIASES:
        return CANONICAL_ALIASES[clean]
    
    # Try with punctuation stripped
    clean_no_punct = re.sub(r"[^\w\s]", "", clean)
    if clean_no_punct in CANONICAL_ALIASES:
        return CANONICAL_ALIASES[clean_no_punct]
        
    return None

def get_skill_category(canonical_skill: str) -> str:
    """Returns the primary category for a canonical skill."""
    return SKILL_TO_CATEGORY.get(canonical_skill, "Other Technical")
