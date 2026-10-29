import csv
from importlib.metadata import metadata
from pathlib import Path

from langchain_core.documents import Document

# ========================================
# CREATE SAMPLE CSV FILE
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

documents = []

with file_path.open("r",encoding="utf-8",newline="") as file:
    reader = csv.DictReader(file)
    for row_index, row in enumerate(reader):
        content = "\n".join(
            f"{field}: {value}"
            for field, value in row.items()
        )

        documents.append(
            Document(
                page_content= content,
                metadata = {
                    "source" : str(file_path),
                    "source_type" : "csv",
                    "name" : row_index,
                }
            )
        )

print('The number of documents:', len(documents))

for document in documents:
    print('\npage content:\n')
    print(document.page_content)
    print('\nmetadata:\n')
    print(document.metadata)