import fitz

from app.services.pdf_service import extract_text_from_pdf

def create_test_pdf() -> bytes:
    document = fitz.open()
    
    page = document.new_page()
    
    page.insert_text(
        (72, 72),
        "Murilo Martins\nPython\nJava\nSQL"
    )
    
    pdf_bytes = document.tobytes()
    
    document.close()
    
    return pdf_bytes

def test_extract_text_from_pdf():
    pdf_bytes= create_test_pdf()
    
    text = extract_text_from_pdf(pdf_bytes)
    
    assert "Murilo Martins" in text
    assert "Python" in text
    assert "Java" in text
    assert "SQL" in text