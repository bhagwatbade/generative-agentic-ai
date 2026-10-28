import csv

from pathlib import Path

from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader


# ========================================
# CUSTOM CSV LOADER
# ========================================

class StudentCSVLoader(BaseLoader):

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def lazy_load(self):

        with self.file_path.open(
                "r",
                encoding="utf-8",
                newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row_index, row in enumerate(reader):

                content = (
                    f"name: {row['name']}\n"
                    f"fee: {row['fee']}"
                )

                yield Document(
                    page_content=content,
                    metadata={
                        "source": str(self.file_path),
                        "source_type": "csv",
                        "row": row_index,
                        "student_id": row["student_id"],
                        "course": row["course"]
                    }
                )


# ========================================
# CREATE SAMPLE FILE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "student_fees.csv"
)

file_path.write_text(
    "student_id,name,course,fee\n"
    "S101,Ravi,Python,5000\n"
    "S102,Priya,Java,6000\n",
    encoding="utf-8"
)


# ========================================
# LOAD STUDENT DOCUMENTS
# ========================================

loader = StudentCSVLoader(file_path)

documents = loader.load()


# ========================================
# DISPLAY RESULTS
# ========================================

print("TOTAL DOCUMENTS:", len(documents))


for document in documents:

    print("\nCONTENT:")
    print(document.page_content)

    print(
        "STUDENT ID:",
        document.metadata["student_id"]
    )

    print(
        "COURSE:",
        document.metadata["course"]
    )

