'''

1. Why is langchain_community being sunset?
-------------------------------------------
langchain_community was a large package containing hundreds of integrations, including document loaders, vector stores, tools, and other components.

Over time, the package became difficult to maintain because:
1. Heavyweight package: It contained a very large number of integrations and supported many optional dependencies.
2. Dependency complexity: Different integrations required different third-party libraries.
3. Difficult maintenance: Maintaining so many integrations in one package became complicated.
4. Shared release cycle: Updating one integration could require coordinating changes across the common package.
5. Better alternatives: Standalone integration packages allow independent development and maintenance.
LangChain officially announced the sunset on 22 May 2026.

Important clarification: It does not mean Python loads every library into memory whenever we import langchain_community. The problem was mainly the large package structure, dependency management and maintenance complexity.


TEXT FILE LOADING USING MODERN LANGCHAIN
----------------------------------------
TWO MODERN WAYS TO LOAD TEXT

Approach 1 — Direct Text Reading and Document Creation
-------------------------------------------------------
from pathlib import Path
from langchain_core.documents import Document

file_path = Path("student_rules.txt")

document = Document(
    page_content=file_path.read_text(encoding="utf-8"),
    metadata={"source": str(file_path)}
)
print(document.page_content)
print(document.metadata)


Approach 1 — Using Normal Python Without LangChain

This approach is not recommended for large-scale applications because of:
1. Scalability Issues: Difficult to manage and maintain as the application grows.
2. Lack of Standardization: No common structure for loading and processing documents.


Approach 2 — Creating a LangChain-Compatible Loader (Recommended)
------------------------------------------------------------------
We should create custom loaders using LangChain's Document and BaseLoader classes.

Advantages:
1. Scalability: Easier to extend and maintain.
2. Standardization: Follows LangChain's standard document-loading structure.
3. Compatibility: Works smoothly with other LangChain components.
4. Reusability: The same loader can be reused across multiple applications.


BaseLoader is the core interface used to implement LangChain document loaders.
It remains documented in langchain-core.

We can create our own loader class using this interface.
That loader can read a file and yield Document objects.

Understanding BaseLoader
-------------------------
Important Import:
from langchain_core.document_loaders import BaseLoader

Our custom loader will inherit from BaseLoader.
We will implement:
lazy_load()

The BaseLoader interface already provides:
load()


Note:
lazy_load()	Yields Documents through an iterator
load()	Collects Documents into a list
------------------------------------------------
Generator simple example to understand:
---------------------------------------
def numbers():
    yield 10
    yield 20
    yield 30


result = numbers()

print(type(result))

for num in result:
    print(num)

E:\lcclasses>py test.py
<class 'generator'>
10
20
30

Understanding the Custom Text Loader
-------------------------------------
We will create a class called:
SimpleTextLoader
This is our own classroom implementation, not a built-in LangChain class.
It will accept:
•	file_path
•	encoding
It will:
1.	Read the specified text file.
2.	Create a LangChain Document.
3.	Store the source path in metadata.
4.	Yield the Document.

Program 2 — Creating a Custom LangChain Text Loader
---------------------------------------------------
Objective: Create a reusable loader using the maintained BaseLoader interface.

from pathlib import Path

from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader


# ========================================
# CUSTOM TEXT LOADER
# ========================================

class SimpleTextLoader(BaseLoader):

    def __init__(
        self,
        file_path,
        encoding="utf-8"
    ):

        self.file_path = Path(file_path)
        self.encoding = encoding

    def lazy_load(self):

        content = self.file_path.read_text(
            encoding=self.encoding
        )

        yield Document(
            page_content=content,
            metadata={
                "source": str(self.file_path)
            }
        )


# ========================================
# CREATE SAMPLE FILE
# ========================================

file_path = (
    Path(__file__).resolve().parent
    / "library_rules.txt"
)

file_path.write_text(
    "Library opens at 8 AM.\n"
    "Library closes at 6 PM.\n",
    encoding="utf-8"
)


# ========================================
# USE CUSTOM LANGCHAIN LOADER
# ========================================

loader = SimpleTextLoader(
    file_path=file_path
)

documents = loader.load()


# ========================================
# DISPLAY RESULTS
# ========================================

print("RETURN TYPE:", type(documents).__name__)

print("TOTAL DOCUMENTS:", len(documents))

print("DOCUMENT TYPE:", type(documents[0]).__name__)

print("\nCONTENT:")
print(documents[0].page_content.strip())

print("\nSOURCE:")
print(
    Path(
        documents[0].metadata["source"]
    ).name
)

Note:
1. We created SimpleTextLoader, our own implementation of LangChain's BaseLoader interface.
We implemented lazy_load().
We did not implement a separate load() method.
Why?
Because the maintained BaseLoader interface already provides it.

2. At the time of execution there is no deprecation warning.

Main Conclusion:
----------------
BaseLoader lets us build our own LangChain-compatible document loaders without depending on sunset community integrations

9. Program 3 — Loading Multiple Text Files
-------------------------------------------
Objective: Load several files into one collection using a custom BaseLoader implementation.

from pathlib import Path

from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader


# ========================================
# CUSTOM DIRECTORY TEXT LOADER
# ========================================

class FolderTextLoader(BaseLoader):

    def __init__(self, folder_path):

        self.folder_path = Path(folder_path)

    def lazy_load(self):

        for file_path in sorted(
            self.folder_path.glob("*.txt")
        ):

            content = file_path.read_text(
                encoding="utf-8"
            )

            yield Document(
                page_content=content,
                metadata={
                    "source": str(file_path)
                }
            )


# ========================================
# PREPARE SAMPLE FILES
# ========================================

folder = (
    Path(__file__).resolve().parent
    / "day2_sample_files"
)

folder.mkdir(exist_ok=True)

files = {
    "admissions.txt": "Admissions start on Monday.",
    "library.txt": "Library opens at 8 AM.",
    "student_rules.txt": "Students must carry ID cards."
}

for filename, content in files.items():

    (folder / filename).write_text(
        content,
        encoding="utf-8"
    )


# ========================================
# LOAD MULTIPLE TEXT FILES
# ========================================

loader = FolderTextLoader(folder)

documents = loader.load()


# ========================================
# DISPLAY DOCUMENTS
# ========================================

print("TOTAL DOCUMENTS:", len(documents))


for number, document in enumerate(
    documents,
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

Note: The inherited .load() method returns all yielded Documents as a list.

Important points:
-----------------

1. Document loading brings external information into LangChain Document objects.
2. The Document class remains supported in LangChain Core.
3. BaseLoader is the maintained interface for custom loaders.
4. A custom loader should implement lazy_load() to yield Documents.
5. The inherited .load() method returns a list of Documents.
6. One file may produce one or multiple Documents depending on our loading design.
7. Our recommended classroom code no longer depends on langchain-community.

Today's Master Formula:
TXT File → Custom BaseLoader → Document → List of Documents

'''