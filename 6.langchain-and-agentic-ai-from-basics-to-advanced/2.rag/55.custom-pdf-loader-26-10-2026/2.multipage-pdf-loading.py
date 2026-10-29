from pathlib import Path

from reportlab.pdfgen import canvas
from pypdf import PdfReader

from langchain_core.documents import Document


# ========================================
# CREATE THREE-PAGE PDF
# ========================================

pdf_path = (
        Path(__file__).resolve().parent
        / "company_policy.pdf"
)

pages = [
    (
        "ATTENDANCE POLICY",
        "Employees must report by 9 AM."
    ),
    (
        "LEAVE POLICY",
        "Employees receive 12 casual leaves."
    ),
    (
        "EMPLOYEE BENEFITS",
        "Medical insurance is available."
    )
]

pdf = canvas.Canvas(str(pdf_path))

for heading, content in pages:

    pdf.drawString(60, 750, heading)
    pdf.drawString(60, 720, content)

    pdf.showPage()

pdf.save()


# ========================================
# READ PDF AND CREATE DOCUMENTS
# ========================================

reader = PdfReader(str(pdf_path))

documents = []

for page_index, page in enumerate(reader.pages):

    documents.append(
        Document(
            page_content=page.extract_text() or "",
            metadata={
                "source": str(pdf_path),
                "page": page_index,
                "total_pages": len(reader.pages),
                "source_type": "pdf"
            }
        )
    )


# ========================================
# DISPLAY RESULTS
# ========================================

print("TOTAL DOCUMENTS:", len(documents))

for document in documents:

    page_number = document.metadata["page"] + 1

    text = " ".join(
        document.page_content.split()
    )

    print("\nPAGE", page_number)
    print("CONTENT:", text)