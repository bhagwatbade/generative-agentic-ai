from pathlib import Path

from reportlab.pdfgen import canvas
from pypdf import PdfReader

from langchain_core.documents import Document


# ========================================
# PREPARE SAMPLE PDF
# ========================================

pdf_path = "library_notice.pdf"

pdf = canvas.Canvas(pdf_path) #creates a Canvas object to generate a PDF file

pdf.drawString(
    60, 750,
    "LIBRARY NOTICE"
)

pdf.drawString(
    60, 720,
    "Library opens at 8 AM."
)

pdf.drawString(
    60, 690,
    "Library closes at 6 PM."
)

pdf.save()


# ========================================
# READ PDF
# ========================================

reader = PdfReader(pdf_path)


# ========================================
# CREATE LANGCHAIN DOCUMENT
# ========================================

page = reader.pages[0]

document = Document(
    page_content=page.extract_text() or "",
    metadata={
        "source": pdf_path,
        "source_type": "pdf",
        "page": 0,
        "total_pages": len(reader.pages)
    }
)


# ========================================
# DISPLAY RESULTS
# ========================================

print("TOTAL PDF PAGES:", len(reader.pages))

print("DOCUMENT TYPE:", type(document).__name__)

print("\nPAGE CONTENT:")
print(document.page_content)

print("\nPAGE INDEX:", document.metadata["page"])

print("SOURCE:",document.metadata["source"])