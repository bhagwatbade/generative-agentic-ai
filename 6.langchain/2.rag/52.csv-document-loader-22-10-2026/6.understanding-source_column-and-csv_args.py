from pathlib import Path

from langchain_community.document_loaders import CSVLoader


# ========================================
# CREATE SEMICOLON-SEPARATED FILE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "special_students_day4.csv"
)

file_path.write_text(
    "student_id;name;course;fee\n"
    "S101;Ravi;Python;5000\n"
    "S102;Priya;Java;6000\n",
    encoding="utf-8"
)


# ========================================
# CREATE CSV LOADER
# ========================================

loader = CSVLoader(
    file_path=str(file_path),
    encoding="utf-8",

    source_column="student_id",

    metadata_columns=[
        "course"
    ],

    csv_args={
        "delimiter": ";"
    }
)


# ========================================
# LOAD DOCUMENTS
# ========================================

documents = loader.load()


# ========================================
# DISPLAY RESULTS
# ========================================

print("TOTAL DOCUMENTS:", len(documents))


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
        document.metadata["source"]
    )

    print("COURSE:")
    print(
        document.metadata["course"]
    )
