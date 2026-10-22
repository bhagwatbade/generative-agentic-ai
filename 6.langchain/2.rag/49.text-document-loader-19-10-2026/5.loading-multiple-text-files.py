from pathlib import Path

from langchain_community.document_loaders import TextLoader


# ========================================
# CREATE DEMO FOLDER
# ========================================

base_dir = (
        Path(__file__).resolve().parent
        / "day2_notices"
)

print(type(base_dir))

base_dir.mkdir(
    exist_ok=True
)


# ========================================
# CREATE THREE TEXT FILES
# ========================================

file_data = {
    "student_rules.txt":
        "Students must carry their ID cards.",

    "library_notice.txt":
        "The library closes at 6 PM.",

    "fee_notice.txt":
        "Course fee deadline is 15 November 2026."
}

for file_name, content in file_data.items():

    file_path = base_dir / file_name

    file_path.write_text(
        content,
        encoding="utf-8"
    )


# ========================================
# LOAD ALL TEXT FILES
# ========================================

all_documents = []

for file_name in file_data:

    file_path = base_dir / file_name

    print(type(file_path))

    loader = TextLoader(
        file_path=str(file_path),
        encoding="utf-8"
    )

    documents = loader.load()

    all_documents.extend(documents)


# ========================================
# DISPLAY TOTAL DOCUMENTS
# ========================================

print("TOTAL DOCUMENTS")
print("---------------")

print(len(all_documents))


# ========================================
# DISPLAY EACH DOCUMENT
# ========================================

for number, document in enumerate(
        all_documents,
        start=1
):

    print("\nDOCUMENT", number)

    print(
        "SOURCE:",
        Path(
            document.metadata["source"]
        ).name
    )

    print(
        "CONTENT:",
        document.page_content
    )