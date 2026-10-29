'''


PDF LOADING USING pypdf AND LANGCHAIN CORE
------------------------------------------
In the last session, we learned how to load information from text files.
We also created our own LangChain-compatible text loader using BaseLoader.


Previously, we discussed PyPDFLoader from the sunset langchain-community package.

For our revised course, we will use a more maintainable approach:
Use pypdf for PDF extraction and langchain-core for Document objects.


Master Formula:
PDF → pypdf.PdfReader → Page Text → LangChain Documents

2. Why Do We Need a PDF Parsing Library?
-----------------------------------------
Friends, a PDF is different from an ordinary text file.
It may contain pages, images, tables, fonts and positioned text.
We need a parser that understands the PDF format.

For today's class, that parser is:
pypdf

What Is PdfReader?
PdfReader is a class from the pypdf package that allows us to open and inspect PDF files.

Important import:
from pypdf import PdfReader

Note:
PdfReader is not a LangChain class.
Its responsibility is PDF processing.
After extracting text, we use LangChain's Document class to represent it.
The pypdf documentation confirms page-wise access using reader.pages and text extraction using page.extract_text().

2 approaches:
Page-wise: One Document per PDF page.
Whole PDF: One Document containing combined page text.
We control this behaviour in our own program.

Note: For Scanned PDFs, this apporach may not work, we should use OCR approach.
7. Important Syntax Before Programming
-------------------------------------
Requirement	Syntax
Open PDF	PdfReader(pdf_path)
Get page count	len(reader.pages)
Access a page	reader.pages[0]
Extract page text	page.extract_text()
Create LangChain Document	Document(page_content=..., metadata=...)
Make a custom LangChain PDF loader	Inherit from BaseLoader
Return Documents using common API	loader.load()
Iterate through page Documents	loader.lazy_load()
------------------------------------------------------
reportlab: we will create sample PDFs using the reportlab package.

python -m pip install pypdf reportlab

Program 1 — Read a Single-Page PDF
----------------------------------
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

=====================
Note:
The drawString() method takes 3 arguments.
Argument	Meaning	Explanation
60	X-coordinate	Distance from the left side of the PDF page
750	Y-coordinate	Distance from the bottom of the PDF page
heading	Text	Text to display at the given position

Remember: In ReportLab, 72 points = 1 inch.

9. Program 2 — Multipage PDF Loading
====================================
Important Methods:
1. canvas.Canvas(pdf_path) creates a new Canvas object in memory.
2. pdf.drawString() adds text to the PDF page.
3. pdf.showPage() finishes the current page and opens the next page.
4. pdf.save() finalises and writes the PDF file to disk.

--------------------------
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
======================================
Program 3 — Whole-PDF Loading(Creating a single document object)
----------------------------------------------------------------
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
===============================================
Program 4 — Custom PDF Loader Using BaseLoader
=============================================
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
-------------------------------------------------------
Main Conclusion: A custom BaseLoader can combine a dedicated PDF parser with LangChain's maintained Document-loading interface.

Important Conclusions:
1. pypdf extracts text from PDF pages.
2. LangChain Document represents the extracted information.
3. Page-wise loading can create one Document per PDF page.
4. Whole-document loading combines multiple pages into one Document.
5. Metadata should preserve the original source and page indexes.
6. The first page index is zero.
7. Basic text extraction does not guarantee successful OCR.
8. BaseLoader provides a maintained interface for custom PDF loaders.

'''