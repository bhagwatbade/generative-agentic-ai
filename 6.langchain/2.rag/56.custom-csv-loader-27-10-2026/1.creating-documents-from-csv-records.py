import csv
from pathlib import Path
from langchain_core.documents import Document


# ========================================
# CREATE SAMPLE CSV
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "students.csv"
)

file_path.write_text(
    "student_id,name,course,fee\n"
    "S101,Ravi,Python,5000\n"
    "S102,Priya,Java,6000\n"
    "S103,Rahul,Data Science,12000\n",
    encoding="utf-8"
)


# ========================================
# CREATE DOCUMENTS FROM CSV
# ========================================

documents = []

with file_path.open(
        "r",
        encoding="utf-8",
        newline=""
) as file:

    reader = csv.DictReader(file)

    for row_index, row in enumerate(reader):

        content = "\n".join(
            f"{field}: {value}"
            for field, value in row.items()
        )

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "source": str(file_path),
                    "source_type": "csv",
                    "row": row_index
                }
            )
        )


# ========================================
# DISPLAY RESULTS
# ========================================

print("TOTAL DOCUMENTS:", len(documents))


for document in documents:

    print("\nROW:", document.metadata["row"])

    print(document.page_content)