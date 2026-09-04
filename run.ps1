# SIH26044 Portal Startup Script for Windows PowerShell
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " SIH26044: Skill, Internship & Placement Portal" -ForegroundColor Yellow
Write-Host " Smart India Hackathon 2026 Prototype" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan

# Check dependencies
Write-Host "Starting FastAPI Application Server at http://localhost:8000..." -ForegroundColor Green
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
