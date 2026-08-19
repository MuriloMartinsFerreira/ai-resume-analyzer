from unittest.mock import MagicMock, patch
from app.schemas.resume_analysis import ResumeAnalysis
from app.services.ai_service import analyse_resume

def test_analyze_resume():
    
    expected_analysis = ResumeAnalysis(
        score=85,
        summary="Good compatibility with the position.",
        matched_skills=[
            "Python",
            "SQL",
            "Git"
        ],
        missing_skills=[
            "Docker"
        ],
        strengths=[
            "Programming experience"
        ],
        recommendations=[
            "Gain experience with Docker"
        ]
    )
    
    mock_response = MagicMock()
    mock_response.output_parsed = expected_analysis

    mock_client = MagicMock()
    mock_client.responses.parse.return_value = mock_response
    
    with patch(
        "app.services.ai_service.get_client",
        return_value=mock_client
    ):
        
        result = analyse_resume(
            resume_text="Python developer with SQL experience.",
            job_title="Software Engineer",
            job_description="Python, SQL, Git and Docker."
        )
        
    assert result.score == 85
    assert "Python" in result.matched_skills
    assert "Docker" in result.missing_skills