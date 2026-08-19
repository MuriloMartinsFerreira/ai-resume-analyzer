from io import BytesIO
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {
        "message": "AI Resume Analyzer API"
    }
    
def test_analyze_rejects_non_pdf():
    response = client.post(
        "/analyze",
        files={
            "file": (
                "resume.txt",
                BytesIO(b"not a pdf"),
                "text/plain"
            )
        },
        data={
            "job_title": "Software Engineer",
            "job_description": "Python developer with SQL experience."
        }
    )
    
    assert response.status_code == 400
    assert response.json()["detail"] == (
        "The upload file must be a pdf."
    )