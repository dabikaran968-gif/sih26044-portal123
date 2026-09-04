"""
Main FastAPI Application Entrypoint for SIH26044 Portal.
Serves REST API and Bilingual Interactive Frontend.
"""

from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api_routes import router as api_router

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="SIH26044 — Skill, Internship & Placement Portal",
    description="Smart India Hackathon 2026 AI-driven Portal for Resume Skill Extraction, Skill Gap Analysis & Recommendations",
    version="1.0.0"
)

# Enable CORS for cross-origin integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Router
app.include_router(api_router)

# Mount static directory
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/api/health")
def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "SIH26044 Skill, Internship and Placement Portal",
        "version": "1.0.0",
        "taxonomy": "NSQF Level 5-7 Aligned"
    }

@app.get("/")
def serve_index():
    """Serve single-page application dashboard."""
    index_file = STATIC_DIR / "index.html"
    return FileResponse(index_file)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
