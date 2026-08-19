import os

from dotenv import load_dotenv
from openai import OpenAI

from app.schemas.resume_analysis import ResumeAnalysis

load_dotenv()

def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not configured."
        )

    return OpenAI(api_key=api_key)


def analyse_resume(
    resume_text: str,
    job_title: str,
    job_description: str
) -> ResumeAnalysis:
   
    client = get_client()
    
    prompt = f"""
You are an AI assistant specialized in resume analysis.

Analyze the candidate's resume against the provided job description.

Your analysis must be objective and based only on the information
provided in the resume and job description.

Do not invent experience, skills, education or qualifications.

JOB TITLE:
{job_title}

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}

Evaluate:

1. Overall compatibility from 0 to 100.
2. A short summary.
3. Skills present in both the resume and job requirements.
4. Relevant skills required by the job that are missing from the resume.
5. The candidate's main strengths for this position.
6. Recommendations to improve the candidate's compatibility.

Return the result using the required structured format.
"""

    response = client.responses.parse(
        model="gpt-5-mini",
        input=prompt,
        text_format=ResumeAnalysis,
    )
    
    return response.output_parsed