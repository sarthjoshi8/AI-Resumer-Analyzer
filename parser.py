import fitz  # PyMuPDF
from docx import Document
import io

def extract_text(content: bytes, content_type: str) -> str:
    if "pdf" in content_type:
        return extract_pdf(content)
    elif "word" in content_type or "docx" in content_type:
        return extract_docx(content)
    raise ValueError("Unsupported file type")

def extract_pdf(content: bytes) -> str:
    text = []
    with fitz.open(stream=content, filetype="pdf") as doc:
        for page in doc:
            text.append(page.get_text())
    return "\n".join(text)

def extract_docx(content: bytes) -> str:
    doc = Document(io.BytesIO(content))
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
