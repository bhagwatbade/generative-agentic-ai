from pathlib import Path

from bs4 import BeautifulSoup

from langchain_core.documents import Document


# ========================================
# PREPARE SAMPLE HTML PAGE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "course_page.html"
)

file_path.write_text(
    """
    <html lang="en">
    <head>
        <title>Course Updates</title>
    </head>
    <body>
        <main>
            <h1>Python Training</h1>
            <p>New batch starts on Monday.</p>
        </main>
    </body>
    </html>
    """,
    encoding="utf-8"
)


# ========================================
# PARSE HTML
# ========================================

html = file_path.read_text(
    encoding="utf-8"
)

soup = BeautifulSoup(
    html,
    "html.parser"
)

main = soup.select_one("main")


# ========================================
# CREATE LANGCHAIN DOCUMENT
# ========================================

document = Document(
    page_content=main.get_text(
        " ",
        strip=True
    ),
    metadata={
        "source": file_path.as_uri(),
        "source_type": "html",
        "title": soup.title.get_text(
            strip=True
        )
    }
)


# ========================================
# DISPLAY RESULT
# ========================================

print("TITLE:", document.metadata["title"])

print("CONTENT:", document.page_content)

print(
    "SOURCE TYPE:",
    document.metadata["source_type"]
)
print("SOURCE:", document.metadata["source"])