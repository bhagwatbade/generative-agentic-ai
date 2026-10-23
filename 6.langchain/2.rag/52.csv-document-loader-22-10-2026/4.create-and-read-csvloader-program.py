from pathlib import Path

from langchain_community.document_loaders import CSVLoader


# ========================================
# CREATE SAMPLE CSV FILE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "students_day4.csv"
)

print(type(file_path))

file_path.write_text(
    "student_id,name,course,fee\n"
    "S101,Ravi,Python,5000\n"
    "S102,Priya,Java,6000\n"
    "S103,Rahul,Data Science,12000\n",
    encoding="utf-8"
)


# ========================================
# CREATE CSV LOADER
# ========================================

loader = CSVLoader(
    file_path=str(file_path),
    encoding="utf-8"
)


# ========================================
# LOAD CSV DOCUMENTS
# ========================================

documents = loader.load()


# ========================================
# DISPLAY DOCUMENT COUNT
# ========================================

print("TOTAL DOCUMENTS")
print("---------------")

print(len(documents))


# ========================================
# DISPLAY EACH DOCUMENT
# ========================================

for number, document in enumerate(
        documents,
        start=1
):

    print("\nDOCUMENT", number)
    print("----------------")

    print("PAGE CONTENT")
    print(document.page_content)

    print("\nSOURCE:")
    print(
        Path(
            document.metadata["source"]
        ).name
    )

    print(
        "ROW INDEX:",
        document.metadata["row"]
    )