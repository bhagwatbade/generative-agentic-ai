from pathlib import Path

from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader


# ========================================
# CUSTOM PDF LOADER
# ========================================

class PDFPageLoader(BaseLoader):

    def __init__(self, pdf_path):

        self.pdf_path = Path(pdf_path)

    def lazy_load(self):

        reader = PdfReader(str(self.pdf_path))

        total_pages = len(reader.pages)

        for page_index, page in enumerate(reader.pages):

            yield Document(
                page_content=page.extract_text() or "",
                metadata={
                    "source": str(self.pdf_path),
                    "source_type": "pdf",
                    "page": page_index,
                    "total_pages": total_pages
                }
            )


# ========================================
# USE CUSTOM LOADER
# ========================================

pdf_path = (
        Path(__file__).resolve().parent
        / "company_policy.pdf"
)

loader = PDFPageLoader(pdf_path)


# ========================================
# PROCESS DOCUMENTS
# ========================================

count = 0

for document in loader.lazy_load():

    count += 1

    text = " ".join(
        document.page_content.split()
    )

    print(
        "PAGE:",
        document.metadata["page"] + 1
    )

    print(
        "STATUS:",
        "TEXT FOUND" if text else "NO EXTRACTABLE TEXT"
    )


print("\nTOTAL PAGES PROCESSED:", count)