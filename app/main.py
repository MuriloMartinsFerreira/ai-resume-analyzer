from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from app.services.pdf_service import extract_text_from_pdf
from app.services.ai_service import analyse_resume

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
    
@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_title: str = Form(...),
    job_description: str = Form(...)):
    
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="The upload file must be a pdf."
        )
        
    file_bytes = await file.read()
    
    resume_text = extract_text_from_pdf(file_bytes)

    if not resume_text:
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from the PDF."
        )
        
    analysis = analyse_resume(
        resume_text=resume_text,
        job_title=job_title,
        job_description=job_description
    )
    
    return {
        "filename" : file.filename,
        "analysis": analysis
    }