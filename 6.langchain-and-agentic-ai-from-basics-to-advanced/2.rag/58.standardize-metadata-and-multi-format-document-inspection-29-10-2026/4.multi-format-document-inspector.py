import csv

from pathlib import Path

from reportlab.pdfgen import canvas
from pypdf import PdfReader
from bs4 import BeautifulSoup

from langchain_core.documents import Document


# ========================================
# PROJECT FOLDER
# ========================================

base_dir = Path(__file__).resolve().parent

demo_dir = base_dir / "module9_final_demo"

demo_dir.mkdir(exist_ok=True)


# ========================================
# CREATE TEXT FILE
# ========================================

txt_path = demo_dir / "student_rules.txt"

txt_path.write_text(
    "Students must carry ID cards.",
    encoding="utf-8"
)


# ========================================
# CREATE TWO-PAGE PDF
# ========================================

pdf_path = demo_dir / "company_policy.pdf"

pdf = canvas.Canvas(str(pdf_path))

pdf.drawString(
    60, 750,
    "ATTENDANCE POLICY"
)

pdf.drawString(
    60, 720,
    "Employees must report by 9 AM."
)

pdf.showPage()

pdf.drawString(
    60, 750,
    "LEAVE POLICY"
)

pdf.drawString(
    60, 720,
    "Employees receive 12 casual leaves."
)

pdf.save()


# ========================================
# CREATE CSV FILE
# ========================================

csv_path = demo_dir / "students.csv"

csv_path.write_text(
    "name,course\n"
    "Ravi,Python\n"
    "Priya,Java\n",
    encoding="utf-8"
)


# ========================================
# CREATE HTML FILE
# ========================================

html_path = demo_dir / "course_page.html"

html_path.write_text(
    """
    <html>
    <head>
        <title>Course Updates</title>
    </head>
    <body>
        <main>
            <h1>Course Updates</h1>
            <p>Python batch starts Monday.</p>
        </main>
    </body>
    </html>
    """,
    encoding="utf-8"
)


# ========================================
# DOCUMENT COLLECTION
# ========================================

documents = []


# ========================================
# LOAD TEXT
# ========================================

documents.append(
    Document(
        page_content=txt_path.read_text(
            encoding="utf-8"
        ),
        metadata={
            "source": str(txt_path),
            "source_type": "txt",
            "department": "Administration"
        }
    )
)


# ========================================
# LOAD PDF PAGES
# ========================================

reader = PdfReader(str(pdf_path))

for page_index, page in enumerate(reader.pages):

    documents.append(
        Document(
            page_content=page.extract_text() or "",
            metadata={
                "source": str(pdf_path),
                "source_type": "pdf",
                "department": "HR",
                "page": page_index,
                "total_pages": len(reader.pages)
            }
        )
    )


# ========================================
# LOAD CSV ROWS
# ========================================

with csv_path.open(
        "r",
        encoding="utf-8",
        newline=""
) as file:

    reader = csv.DictReader(file)

    for row_index, row in enumerate(reader):

        content = "\n".join(
            f"{key}: {value}"
            for key, value in row.items()
        )

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "source": str(csv_path),
                    "source_type": "csv",
                    "department": "Admissions",
                    "row": row_index
                }
            )
        )


# ========================================
# LOAD SAVED HTML PAGE
# ========================================

soup = BeautifulSoup(
    html_path.read_text(encoding="utf-8"),
    "html.parser"
)

main = soup.select_one("main")

documents.append(
    Document(
        page_content=main.get_text(
            " ",
            strip=True
        ),
        metadata={
            "source": html_path.as_uri(),
            "source_type": "html",
            "department": "Training",
            "title": soup.title.get_text(
                strip=True
            )
        }
    )
)


# ========================================
# DOCUMENT INSPECTION REPORT
# ========================================

print("MULTI-FORMAT DOCUMENT INSPECTOR")
print("===============================")

print("TOTAL DOCUMENTS:", len(documents))


for number, document in enumerate(
        documents,
        start=1
):

    metadata = document.metadata

    content = " ".join(
        document.page_content.split()
    )

    print("\nDOCUMENT", number)

    print(
        "TYPE:",
        metadata["source_type"]
    )

    print(
        "DEPARTMENT:",
        metadata["department"]
    )

    print(
        "CONTENT STATUS:",
        "READY" if content else "EMPTY"
    )

    if "page" in metadata:

        print(
            "PAGE:",
            metadata["page"] + 1
        )

    if "row" in metadata:

        print(
            "ROW:",
            metadata["row"] + 1
        )

    print(
        "PREVIEW:",
        content[:70] if content else "No extractable text"
    )


# ========================================
# SUMMARY BY SOURCE TYPE
# ========================================

print("\nDOCUMENT COUNT BY TYPE")
print("----------------------")

for source_type in [
    "txt",
    "pdf",
    "csv",
    "html"
]:

    count = sum(
        document.metadata["source_type"]
        == source_type
        for document in documents
    )

    print(
        source_type.upper(),
        ":",
        count
    )


# ========================================
# EMPTY DOCUMENT COUNT
# ========================================

empty_count = sum(
    not document.page_content.strip()
    for document in documents
)

print("\nEMPTY DOCUMENTS:", empty_count)

print("\nINSPECTION COMPLETED")