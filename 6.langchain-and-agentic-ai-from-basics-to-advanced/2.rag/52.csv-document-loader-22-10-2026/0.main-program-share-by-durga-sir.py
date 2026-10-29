'''

DOCUMENT LOADERS — CSVLoader
----------------------------
Today's Master Formulas:
CSV File → CSVLoader → One Document Per Data Row

Situation 1:
Our training institute maintains student information in a CSV file.
The file contains student names, course names, fee details and joining dates.
How will LangChain read this information?

ID 	Name	Course	Fee
S101	Ravi	Python	5000
S102	Priya	Java	6000
S103	Rahul	Data Science	12000
S104	Shiva	Agentic AI	18000


Suppose one student asks:
"Sir, what is my course fee?"
Our administrator opens the register and says:
"Ravi pays ₹5,000, Priya pays ₹6,000, Rahul pays ₹12,000. Everybody please pay all these fees together!"
Ayyooo! 😄
Friends, each student's information is separate.

That is why row-wise representation is useful.

Note:
When working with CSV data, a single row can be represented as one LangChain Document object.

. What Is CSVLoader?
-------------------
CSVLoader is a LangChain document loader that reads CSV files and creates one Document object for each CSV data row.

In normal CSV loading, the number of Documents matches the number of data rows, not the number of header-plus-data lines.

. How Does CSVLoader Prepare page_content?
------------------------------------------
Suppose the first student row contains:
Student ID: S101
Name: Ravi
Course: Python
Fee: 5000

CSVLoader typically converts the row into labelled text.
Conceptually:

student_id: S101
name: Ravi
course: Python
fee: 5000

Friends, observe carefully.
Each column name is associated with its value.
This complete text becomes the page_content of the first Document.

Why Are Column Names Useful?
----------------------------
CSVLoader's labelled text representation can be useful in document-processing workflows.

Important Observation
---------------------
CSVLoader does not merely store the raw CSV row as a comma-separated string.
It prepares a text representation of the row using field names and values.

Main Conclusion
----------------
Each CSV row becomes a Document whose page_content describes the row's field values

7. Understanding CSV Metadata
Friends, in Day 3 we learned PDF metadata such as:
source
page
total_pages
Today, CSVLoader uses a different important field:
row
Example
For the first CSV data row, metadata may contain:
{
    "source": "students.csv",
    "row": 0
}

For the second row:
{
    "source": "students.csv",
    "row": 1
}

For the third row:
{
    "source": "students.csv",
    "row": 2
}

Important Observation
----------------------
The row value is a zero-based data-row index.
The header is not counted as data row zero.

8. Understanding metadata_columns
---------------------------------
metadata_columns identifies which CSV fields should be stored in the Document's metadata.

Suppose our CSV contains:
student_id	name	course	fee
S101	Ravi	Python	5000

Now imagine we want:
page_content:

name: Ravi
fee: 5000

metadata:

{
    "student_id": "S101",
    "course": "Python"
}

We can tell CSVLoader to treat particular columns as metadata.
For example:

metadata_columns=[
    "student_id",
    "course"
]

metadata_columns lets us place selected CSV fields inside Document metadata.
Note: It is very helpful to reduce retrieval time from the vector database.

9. Understanding content_columns
--------------------------------
content_columns tells CSVLoader which CSV fields should be included in page_content.
Suppose the CSV contains:
student_id
name
course
fee
But we want only:
name
and
fee
inside page_content.




We can specify:
content_columns=[
    "name",
    "fee"
]

Parameter	Purpose
metadata_columns	Select fields to store in metadata
content_columns	Select fields to include in page_content

Note: A field can appear in both if it is selected for both purposes.

Understanding source_column
----------------------------
source_column tells CSVLoader to use the value of a particular CSV column as the Document's source metadata.

By default, source metadata identifies the CSV file.
For example:

{"source": "students.csv"}

Now suppose we specify:

source_column="student_id"

For Ravi, the source becomes:
S101
For Priya:
S102
Note: This is useful when a row has its own source identifier.

metadata_columns vs source_column
---------------------------------
metadata_columns adds selected fields to metadata under their column names.
source_column specifically controls the value of metadata's source key.
source_column changes what CSVLoader records as the source of each Document.

11. Understanding csv_args
---------------------------
Not every CSV file uses exactly the same separator or quoting rules.
The csv_args parameter lets us pass CSV-reading options to the underlying CSV reader.

Europian people they may not use comma separator and they will use ;

csv_args={
    "delimiter": ";"
}

csv_args lets us configure how CSVLoader interprets the structure of the CSV file.

Requirement	Syntax
Import CSVLoader	from langchain_community.document_loaders import CSVLoader
Create CSV loader	CSVLoader(file_path="students.csv")
Select metadata columns	metadata_columns=["course"]
Select content columns	content_columns=["name", "fee"]
Change source column	source_column="student_id"
Configure CSV parsing	csv_args={"delimiter": ";"}


Program 1A — Our First CSVLoader Program
---------------------------------------
from langchain_community.document_loaders import CSVLoader

# ========================================
# CREATE CSV LOADER
# ========================================

loader = CSVLoader(
    file_path="students.csv",
	encoding='utf-8'
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

for document in documents:
	print("\nPAGE CONTENT")
	print(document.page_content)
	print("METADATA")
	print(document.metadata)


Program 1A — Our First CSVLoader Program
---------------------------------------
Objective: Read an actual CSV file and observe how its data rows become LangChain Document objects.

from pathlib import Path

from langchain_community.document_loaders import CSVLoader


# ========================================
# CREATE SAMPLE CSV FILE
# ========================================

file_path = (
    Path(__file__).resolve().parent
    / "students_day4.csv"
)

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


25. Program 2 — Using metadata_columns and content_columns
-----------------------------------------------------------
Objective: Separate selected CSV fields into page_content and metadata.

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

Note: CSVLoader still provides source and row information

26. Program 3 — Understanding source_column and csv_args
Objective: Change the source metadata using a CSV column and read a file using a semicolon delimiter.


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




Observation 1 — csv_args
Our file uses:
;
instead of the normal comma separator.
We supplied:
csv_args={"delimiter": ";"}
Therefore, CSVLoader interprets the fields correctly.
Observation 2 — source_column
We supplied:
source_column="student_id"
Therefore, the source metadata becomes:
S101
for Ravi.
And:
S102
for Priya.


Observation 3 — metadata_columns
We selected:
course
as metadata.
Therefore, the course value appears in metadata.
Because content_columns was not supplied, CSVLoader automatically includes the other non-metadata fields in page_content.



'''