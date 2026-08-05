from fastapi import FastAPI

app = FastAPI(
    title="AI Resume Analyzer",
    description="API for analyzing resumes using AI",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Resume Analyzer API"
    }