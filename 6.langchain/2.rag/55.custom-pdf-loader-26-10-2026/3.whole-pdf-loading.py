from pathlib import Path

from pypdf import PdfReader

from langchain_core.documents import Document


# ========================================
# SPECIFY EXISTING PDF
# ========================================

pdf_path = (
        Path(__file__).resolve().parent
        / "company_policy.pdf"
)


# ========================================
# READ ALL PDF PAGES
# ========================================

reader = PdfReader(str(pdf_path))

page_texts = [
    page.extract_text() or ""
    for page in reader.pages
]


# ========================================
# COMBINE PAGE TEXT
# ========================================

combined_text = (
    "\n--- PAGE BREAK ---\n"
    .join(page_texts)
)


# ========================================
# CREATE ONE LANGCHAIN DOCUMENT
# ========================================

document = Document(
    page_content=combined_text,
    metadata={
        "source": str(pdf_path),
        "source_type": "pdf",
        "total_pages": len(reader.pages),
        "loading_mode": "single"
    }
)


# ========================================
# DISPLAY RESULTS
# ========================================

documents = [document]

print("TOTAL DOCUMENTS:", len(documents))

print(
    "TOTAL PDF PAGES:",
    document.metadata["total_pages"]
)

print(
    "PAGE BREAKS:",
    document.page_content.count(
        "--- PAGE BREAK ---"
    )
)

print(
    "PAGE INDEX AVAILABLE:",
    "page" in document.metadata
)