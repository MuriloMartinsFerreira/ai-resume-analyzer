from pydantic import BaseModel, Field

class ResumeAnalysis(BaseModel):
    score: int = Field(
        ge=0,
        le=100,
        description="Compatibility score between resume and job"
    )
    
    sumary: str
    
    matched_skills: list[str]
    
    missing_skills: list[str]
    
    strengths: list [str]
    
    recommendations: list[str]