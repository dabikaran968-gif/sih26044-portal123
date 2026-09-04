# SIH26044 — Skill, Internship & Placement Portal

> **Smart India Hackathon (SIH) Problem Statement ID:** SIH26044  
> **Category:** Software  
> **Target Audience:** Students, Recruiters / Companies, Training & Placement Officers (TPOs), Institutional Admins  

An AI-driven intelligent platform that automates resume skill extraction, aligns competencies to the **National Skills Qualification Framework (NSQF)** taxonomy, computes quantifiable skill gap vectors against live industry job postings, recommends curated **SWAYAM / NPTEL** upskilling paths, and equips institutions with batch-level placement readiness heatmaps.

---

## 🌟 Core Features & PRD Alignment

### 1. AI Resume Parsing & NLP Skill Extraction (Section 5.1 & 5.2)
- **Multi-format ingestion**: Ingests PDF and text resumes with clean section segmentation (Education, Projects, Work History, Skills, Certifications).
- **Explicit Extraction**: Direct keyword scanner mapped to canonical taxonomy aliases (`"reactjs"` / `"react.js"` $\rightarrow$ `"React"`).
- **Implicit Extraction Engine**: Infers hidden competencies from project descriptions (e.g., *"Built REST APIs with Flask and containerized with Docker"* $\rightarrow$ infers `Python`, `REST APIs`, `Docker`, `Linux`).
- **Confidence Scoring & Editable Tags**: Each skill includes a confidence percentage (0-100%) and explicit/implicit tags, with the ability for students to manually add/remove skills.

### 2. Skill Gap Vector Analysis & Radar Chart (Section 5.3 & 9)
- **Weighted Competency Math**: Mandatory role requirements carry $3\times$ weight, preferred skills carry $1\times$.
- **Interactive Radar Chart**: Dynamic 6-dimensional visualization (Programming, Frontend, Backend & APIs, Database, Cloud & DevOps, AI & Data Science) comparing candidate competency vs. role threshold.
- **Match Score & Categorization**:
  - **Best Fit** ($\ge 75\%$ match)
  - **Stretch Opportunities** ($50\% - 74\%$ match)
  - **Safe Matches** ($\ge 85\%$ match or entry-level roles)
- **Explainable AI**: Rationale explaining why the candidate received the score and the exact impact of learning missing skills.

### 3. Smart Recommendations & Personalized Upskilling (Section 5.4 & 5.5)
- **Ranked Opportunity Feed**: Live filtering by Sector (Fintech, E-Commerce, IT, PSUs) and Remote/Onsite options.
- **Upskilling Bridge**: Auto-maps missing skills to curated Indian government & global MOOCs (**SWAYAM, NPTEL, Coursera, freeCodeCamp**).

### 4. Recruiter / Employer Portal (Section 5.6)
- **Post Openings**: Recruiters can publish internships with specific mandatory and preferred skill sets.
- **Instant Ranked Shortlist**: Real-time matching algorithm ranks registered student candidates with match percentages and skill overlap breakdowns.
- **Candidate Pipeline**: Update candidate statuses (*Under Review*, *Shortlisted*, *Interview Scheduled*, *Offer Extended*).

### 5. TPO / Institution Analytics Dashboard (Section 5.7)
- **Batch Readiness Metrics**: Placement Ready %, Average Readiness Score, and Total Students.
- **Department Heatmap**: Matrix view of competency across departments (CSE, IT, AI/DS, ECE).
- **Batch Skill Deficit Analysis**: Bar chart highlighting the most frequent missing skills across all students to guide college workshop planning.
- **One-Click CSV Export**: Instant download of the full student readiness audit report.

### 6. Bilingual User Experience (Section 6)
- Full toggle between **English** and **हिन्दी (Hindi)** across all dashboard tabs, labels, badges, and chart legends.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+ (Tested on Python 3.14)
- Pip

### Installation & Launch

1. Open PowerShell and navigate to the project directory:
   ```powershell
   cd C:\Users\dabik\.gemini\antigravity\scratch\sih26044-portal
   ```

2. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Run the automated test suite:
   ```powershell
   python test_engine.py
   ```

4. Launch the platform:
   ```powershell
   .\run.ps1
   # OR
   python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
   ```

5. Open your web browser at:
   ```
   http://localhost:8000
   ```

---

## 📁 Project Architecture

```
sih26044-portal/
├── app/
│   ├── __init__.py           # Package definition
│   ├── models.py             # Pydantic data schemas
│   ├── taxonomy.py           # NSQF master taxonomy & alias mapping
│   ├── parser_engine.py      # PDF parsing, NER & implicit inference
│   ├── matching_engine.py    # Vector similarity, radar scoring & gap logic
│   ├── upskilling_engine.py  # SWAYAM/NPTEL course mapping
│   ├── seed_data.py          # Seeded jobs, sample resumes & student cohorts
│   ├── api_routes.py         # REST API endpoints
│   └── main.py               # FastAPI server & static file mounts
├── static/
│   ├── index.html            # Bilingual SPA frontend layout
│   ├── app.js                # State management, Chart.js radar & i18n
│   └── styles.css            # Responsive CSS styling extensions
├── requirements.txt          # Python dependencies
├── test_engine.py            # Automated test suite
├── run.ps1                   # Windows startup script
└── README.md                 # Project documentation
```
