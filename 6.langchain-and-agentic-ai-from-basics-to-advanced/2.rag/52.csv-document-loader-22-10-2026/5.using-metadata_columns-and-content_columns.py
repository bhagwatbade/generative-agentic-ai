from pathlib import Path

from langchain_community.document_loaders import CSVLoader


# ========================================
# CREATE CSV FILE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "student_metadata_day4.csv"
)

file_path.write_text(
    "student_id,name,course,fee\n"
    "S101,Ravi,Python,5000\n"
    "S102,Priya,Java,6000\n",
    encoding="utf-8"
)


# ========================================
# CREATE CSV LOADER
# ========================================

loader = CSVLoader(
    file_path=str(file_path),
    encoding="utf-8",

    metadata_columns=[
        "student_id",
        "course"
    ],

    content_columns=[
        "name",
        "fee"
    ]
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

    print("\nSTUDENT ID:")
    print(
        document.metadata["student_id"]
    )

    print("COURSE:")
    print(
        document.metadata["course"]
    )

    print("ROW INDEX:")
    print(
        document.metadata["row"]
    )