'''

CSV  LOADING
------------
CSV → csv.DictReader → Document Per Data Row

2. What Is Our Requirement?
---------------------------
Suppose we have:
students.csv
student_id	name	course	fee
S101	Ravi	Python	5000
S102	Priya	Java	6000
S103	Rahul	Data Science	12000

Friends, three students means three data records.
We want to create three LangChain Documents.

3. Important CSV Document Structure
For Ravi:
page_content
student_id: S101
name: Ravi
course: Python
fee: 5000

metadata

{
    "source": "students.csv",
    "row": 0,
    "source_type": "csv"
}

The content contains the student's information.
The metadata tells us where the record came from.

5.	Understanding CSV Field Selection
-----------------------------------------
In the old CSVLoader, we studied concepts such as:

metadata_columns
content_columns
source_column

Those were parameters of the old integration.
They are not parameters of LangChain’s Document class.
But the underlying requirements remain useful.
We may decide:
•	Which CSV fields become Document text?
•	Which fields become metadata?
•	Which field acts as the record’s identifier?
We can implement those decisions using csv.DictReader and Document.

Program 1 — Creating Documents From CSV Records
-----------------------------------------------
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

Note:
newline="" means: "Python, don't modify the original line-ending characters. Let the CSV reader handle them."


Using "\n".join():
student_id: S101
name: Ravi
course: Python
fee: 5000

Using " ".join()
student_id: S101 name: Ravi course: Python fee: 5000
=====================================================================
Program 2 — Custom CSV Loader With Selected Content and Metadata
----------------------------------------------------------------
Objective: Use the maintained BaseLoader interface and control which CSV fields appear in content and metadata.

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


Note:
Custom BaseLoader implementations allow us to control the content and metadata generated from structured source data.

'''