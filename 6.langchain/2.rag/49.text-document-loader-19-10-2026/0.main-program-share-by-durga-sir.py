'''
from langchain_core.documents import Document

document = Document(
    page_content="Python is a programming language.",
    metadata={
        "source": "python_notes.txt"
    }
)

Instead of manually providing the content, we want LangChain to read the actual file and create Document objects for us.

Loader reads the content
Loader can supply source metadata
Actual file is required
Loader creates the Document
Main class: TextLoader


We need an  rganized mechanism to load information from existing files.

Document Loaders help us obtain information from external sources in a standard LangChain Document format.

Def:
A Document Loader is a component that reads information from a supported external source and produces LangChain Document objects.


Convert source information into LangChain Document objects.

Document vs Document Loader vs LLM:
-----------------------------------
Document Loader reads the information.
Document represents the information.
LLM may later use relevant information to generate a response.

TextLoader
Definition
TextLoader is a LangChain Document Loader used to read plain text files and represent their contents as Document objects.


pip install langchain_community
from langchain_community.document_loaders import TextLoader

Note:
Document	Represents content and metadata
TextLoader	Reads text files and produces Documents

Why TextLoader When Python Already Has open()?
----------------------------------------------
with open(
        "student_rules.txt",
        "r",
        encoding="utf-8"
) as file:
    content = file.read()

A Python string containing the file's text.

loader = TextLoader(
    "student_rules.txt",
    encoding="utf-8"
)

documents = loader.load()

What does this give?
A list of LangChain Document objects.


loader = TextLoader(
    file_path="student_rules.txt",
    encoding="utf-8"
)


file_path	Identifies the file to load
encoding	Specifies how the file's text is decoded

Definition
The .load() method reads the source through the loader and returns the loaded information as a list of Document objects.

10. What Does load() Return?
-----------------------------
It is a list of Document objects.

•	A TextLoader normally produces one Document for one text file.
•	A PDF loader may produce multiple Documents, depending on its settings.
Using a list provides a consistent return structure.

12. Understanding Metadata After Loading
-----------------------------------------
TextLoader supplies source metadata, and our application may add custom metadata when required.
{"source": "student_rules.txt"}

document.metadata["department"] = "Administration"

Why UTF-8?
UTF-8 supports English, Telugu, Hindi and many other languages, along with symbols such as ₹.

---------------------------------------------------
from pathlib import Path

base_dir = Path(__file__).resolve().parent

file_path = base_dir / "student_rules.txt"

from pathlib import Path

base_dir = Path(__file__).resolve().parent

file_path = base_dir / "student_rules.txt"
print(file_path)

E:\lcclasses>py test.py
E:\lcclasses\student_rules.txt

Note:
Purpose: To get the absolute path of the folder where the currently running Python file is located.
Let's understand step by step.

1. __file__
It represents the path of the current Python file.
Example:
__file__ = "D:/projects/chatbot/main.py"


2. Path(__file__)
Converts the file path into a Path object.
Path("D:/projects/chatbot/main.py")



This allows us to perform path-related operations easily.
3. .resolve()
Converts the path into an absolute path and resolves symbolic links.
Example:
Path(__file__).resolve()



Output:
D:\projects\chatbot\main.py


4. .parent
Returns the directory containing the file.
Path(__file__).resolve().parent



Output:
D:\projects\chatbot

17. Understanding load() vs lazy_load()
----------------------------------------
What Is lazy_load()?
lazy_load() provides an iterator that yields Document objects as they become available.
For example:
for document in loader.lazy_load():
    print(document.page_content)


load()	                          lazy_load()
----------------------------------------------
Returns a list of Documents	        Returns an iterator of Documents
Collects results before returning	Allows processing as Documents are yielded
Convenient for ordinary loading	        Useful for iterative processing

Note:
.load() returns a complete list. .lazy_load() supports iterative Document processing

Requirement	Syntax
Import TextLoader	from langchain_community.document_loaders import TextLoader
Create loader	  TextLoader(file_path, encoding="utf-8")
Load file	 loader.load()
Iterate lazily	  loader.lazy_load()
Access first Document	 documents[0]
Access actual text	 documents[0].page_content
Access metadata	    documents[0].metadata
Access source	    documents[0].metadata["source"]
-----------------------
21. Program 1 — Our First TextLoader Program
--------------------------------------------
from pathlib import Path

from langchain_community.document_loaders import TextLoader


# ========================================
# CREATE SAMPLE TEXT FILE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "student_rules.txt"
)

file_path.write_text(
    "Students must carry their ID cards.\n"
    "Classes start at 9 AM.\n"
    "Mobile phones are not allowed.\n",
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
# LOAD DOCUMENTS
# ========================================

documents = loader.load()


# ========================================
# DISPLAY TOTAL DOCUMENTS
# ========================================

print("TOTAL DOCUMENTS")
print("---------------")

print(len(documents))


# ========================================
# ACCESS FIRST DOCUMENT
# ========================================

document = documents[0]


# ========================================
# DISPLAY CONTENT
# ========================================

print("\nPAGE CONTENT")
print("------------")

print(document.page_content.strip())


# ========================================
# DISPLAY SOURCE
# ========================================

print("\nSOURCE FILE")
print("-----------")

print(
    Path(
        document.metadata["source"]
    ).name
)
-----------------------
22. Program 2 — Understanding Return Type and Metadata
--------------------------------------------------------
from pathlib import Path

from langchain_community.document_loaders import TextLoader


# ========================================
# CREATE SAMPLE TEXT FILE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "library_rules.txt"
)

content = (
    "The library opens at 8 AM.\n"
    "The library closes at 6 PM.\n"
)

file_path.write_text(
    content,
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
# LOAD DOCUMENTS
# ========================================

documents = loader.load()


# ========================================
# CHECK RETURN TYPE
# ========================================

print("RETURN TYPE")
print("-----------")

print(type(documents).__name__)


# ========================================
# CHECK TOTAL DOCUMENTS
# ========================================

print("\nTOTAL DOCUMENTS")
print("---------------")

print(len(documents))


# ========================================
# ACCESS DOCUMENT
# ========================================

document = documents[0]

print("\nDOCUMENT TYPE")
print("-------------")

print(type(document).__name__)


# ========================================
# DISPLAY SOURCE METADATA
# ========================================

print("\nSOURCE FILE")
print("-----------")

print(
    Path(
        document.metadata["source"]
    ).name
)


# ========================================
# ADD CUSTOM METADATA
# ========================================

document.metadata["department"] = "Library"


# ========================================
# DISPLAY CUSTOM METADATA
# ========================================

print("\nDEPARTMENT")
print("----------")

print(document.metadata["department"])


# ========================================
# CHECK ORIGINAL FILE
# ========================================

print("\nORIGINAL FILE UNCHANGED?")
print("------------------------")

print(
    file_path.read_text(encoding="utf-8")
    == content
)


Main Conclusion
TextLoader creates Document objects with source metadata. We can extend the metadata without changing the original text file.

24. Program 3 — Loading Multiple Text Files
--------------------------------------------
from pathlib import Path

from langchain_community.document_loaders import TextLoader


# ========================================
# CREATE DEMO FOLDER
# ========================================

base_dir = (
        Path(__file__).resolve().parent
        / "day2_notices"
)

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

Main Conclusion
We can use TextLoader repeatedly to convert information from multiple text files into a collection of LangChain Document objects.

============
Program 5 — Handling a Missing Text File
------------------------------------------
from pathlib import Path

from langchain_community.document_loaders import TextLoader


# ========================================
# SPECIFY NON-EXISTING FILE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "missing_notice_for_demo_98765.txt"
)


# ========================================
# CREATE TEXT LOADER
# ========================================

loader = TextLoader(
    file_path=str(file_path),
    encoding="utf-8"
)


# ========================================
# ATTEMPT TO LOAD FILE
# ========================================

try:

    documents = loader.load()

    print(
        "TOTAL DOCUMENTS:",
        len(documents)
    )

except RuntimeError:

    print("FILE LOADING FAILED")

    print(
        "The file could not be read."
    )

    print(
        "Check the file path,"
        " permissions and encoding."
    )

Main Conclusion
Document loading depends on the availability and accessibility of the actual source file.
-----------------
Program 6 — Understanding lazy_load()
=====================================
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

for document in loader.lazy_load():

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

Main Conclusion
load() collects Documents into a list, whereas lazy_load() allows us to process Documents as they are yielded.

'''