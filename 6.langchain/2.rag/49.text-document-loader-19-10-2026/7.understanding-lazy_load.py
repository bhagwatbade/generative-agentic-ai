from pathlib import Path

from langchain_community.document_loaders import TextLoader


# ========================================
# CREATE SAMPLE FILE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "course_notice.txt"
)

file_path.write_text(
    "New Python batch starts on Monday.\n"
    "Class timing is 7 AM.\n",
    encoding="utf-8"
)


# ========================================
# CREATE TEXT LOADER
# ========================================

loader = TextLoader(
    file_path=str(file_path),
    encoding="utf-8"
)


# ========================================
# PROCESS DOCUMENTS LAZILY
# ========================================

count = 0

lazy_documents = loader.lazy_load()

print(type(lazy_documents))
print(type(lazy_documents).__name__)

for document in lazy_documents:

    count += 1

    print("DOCUMENT", count)

    print(
        "CONTENT:",
        document.page_content.strip()
    )

    print(
        "SOURCE:",
        Path(
            document.metadata["source"]
        ).name
    )


# ========================================
# DISPLAY TOTAL
# ========================================

print("\nTOTAL PROCESSED:", count)