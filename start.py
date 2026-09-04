import os
import sys
import uvicorn

# Add current directory and immediate subdirectories to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Look for app package in current folder or nested folder
for folder in os.listdir(current_dir):
    sub = os.path.join(current_dir, folder)
    if os.path.isdir(sub) and sub not in sys.path:
        sys.path.insert(0, sub)

app = None

# Attempt 1: Standard app.main
try:
    from app.main import app
except Exception:
    pass

# Attempt 2: If files were placed directly in root
if app is None:
    try:
        from main import app
    except Exception:
        pass

# Attempt 3: Nested repository folder (e.g. sih26044-portal/app)
if app is None:
    for folder in os.listdir(current_dir):
        nested_app = os.path.join(current_dir, folder, "app")
        if os.path.isdir(nested_app):
            sys.path.insert(0, os.path.join(current_dir, folder))
            try:
                from app.main import app
                break
            except Exception:
                pass

if app is None:
    raise RuntimeError(f"Could not locate FastAPI app. Directory contents: {os.listdir(current_dir)}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting server on port {port}...")
    uvicorn.run(app, host="0.0.0.0", port=port)
