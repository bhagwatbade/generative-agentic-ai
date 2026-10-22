'''


1. Important PyPDFLoader Syntax Summary
----------------------------------------
Requirement	Syntax
Import loader	 from langchain_community.document_loaders import PyPDFLoader
Create PDF loader	PyPDFLoader(file_path="sample.pdf")
Page-wise loading	mode="page"
Combined loading	mode="single"
Load all Documents	loader.load()
Iterate over Documents	loader.lazy_load()
Read page text	document.page_content
Read page index	document.metadata["page"]
Read page count	document.metadata["total_pages"]
Read page label	document.metadata.get("page_label")
Read source	document.metadata["source"]
Page separator	pages_delimiter="..."
------------------------------
Program 1 — Our First PyPDFLoader Program
==========================================
Objective: Load a single-page PDF and access its content and source information.

from langchain_community.document_loaders import PyPDFLoader

# ========================================
# CREATE PDF LOADER
# ========================================

loader = PyPDFLoader(
    file_path="library_notice.pdf"
)


# ========================================
# LOAD PDF DOCUMENTS
# ========================================

documents = loader.load()


# ========================================
# DISPLAY RETURN INFORMATION
# ========================================

print("RETURN TYPE")
print("-----------")
print(type(documents).__name__) #List

print("\nTOTAL DOCUMENTS")
print("---------------")
print(len(documents))  #1


# ========================================
# ACCESS FIRST DOCUMENT
# ========================================

document = documents[0]


# ========================================
# DISPLAY EXTRACTED CONTENT
# ========================================

print("\nPAGE CONTENT")
print("------------")
print(document.page_content)


# ========================================
# DISPLAY METADATA
# ========================================
print("\nMETADATA")
print("------------")
print(document.metadata)


# ========================================
# DISPLAY SOURCE INFORMATION
# ========================================

print("\nSOURCE FILE")
print("-----------")

print(document.metadata["source"])

# ========================================
# DISPLAY PDF PAGE INFORMATION
# ========================================

print("\nPAGE INFORMATION")
print("----------------")

print("Page Index:",document.metadata["page"]) #0

print("Total Pages:", document.metadata["total_pages"])


-----------------------
Program 2 — Loading a Multipage PDF
-----------------------------------------
Objective: Load a three-page PDF and access each page separately.

from langchain_community.document_loaders import PyPDFLoader

# ========================================
# CREATE PAGE-WISE PDF LOADER
# ========================================

loader = PyPDFLoader(
    file_path="company_policy.pdf",
    mode="page"
)


# ========================================
# LOAD PDF PAGES
# ========================================

documents = loader.load()


# ========================================
# DISPLAY TOTAL DOCUMENTS
# ========================================

print("COMPANY POLICY PDF")
print("==================")

print(
    "Total Documents:",
    len(documents)
)


# ========================================
# DISPLAY EACH PAGE
# ========================================

for document in documents:

    page_index = document.metadata["page"]

    page_number = page_index + 1



    print("\nPAGE", page_number)
    print("---------------------")

    print("CONTENT:\n", document.page_content)

Program 3 — Understanding PDF Metadata in Detail
------------------------------------------------------
Objective: Examine source metadata, PDF page index, page label and total page count

from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

# ========================================
# CREATE PDF LOADER
# ========================================

loader = PyPDFLoader(
    file_path="company_policy.pdf",
    mode="page"
)


# ========================================
# LOAD DOCUMENTS
# ========================================

documents = loader.load()


# ========================================
# DISPLAY PDF SUMMARY
# ========================================

print("PDF METADATA REPORT")
print("===================")

print(
    "Total Documents:",
    len(documents)
)


# ========================================
# DISPLAY METADATA FOR EACH PAGE
# ========================================

for document in documents:

    metadata = document.metadata

    print("\nPAGE METADATA")
    print("-------------")

    print("Source:",metadata["source"])

    print(
        "Page Index:",
        metadata["page"]
    )

    print(
        "Display Page:",
        metadata["page"] + 1
    )

    print(
        "Page Label:",
        metadata.get(
            "page_label",
            "Not available"
        )
    )

    print(
        "Total Pages:",
        metadata["total_pages"]
    )
====================================================================
Program 4 — mode="page" vs mode="single"
--------------------------------------------
from langchain_community.document_loaders import PyPDFLoader

# ========================================
# PAGE MODE
# ========================================

page_loader = PyPDFLoader(
    file_path="company_policy.pdf",
    mode="page"
)

page_documents = page_loader.load()


# ========================================
# SINGLE MODE
# ========================================

single_loader = PyPDFLoader(
    file_path="company_policy.pdf",
    mode="single",
    pages_delimiter="\n--- PAGE BREAK ---\n"
)

single_documents = single_loader.load()


# ========================================
# COMPARE DOCUMENT COUNTS
# ========================================

print("PAGE MODE DOCUMENTS")
print("-------------------")
print(len(page_documents))

print("\nSINGLE MODE DOCUMENTS")
print("---------------------")
print(len(single_documents))


# ========================================
# ACCESS COMBINED DOCUMENT
# ========================================

document = single_documents[0]


# ========================================
# CHECK PAGE METADATA
# ========================================

print("\nSINGLE MODE METADATA")
print("--------------------")

print(
    "Total Pages:",
    document.metadata["total_pages"]
)

print(
    "Page Index Available:",
    "page" in document.metadata
)


# ========================================
# DISPLAY COMBINED PAGE CONTENT
# ========================================

print("\nCOMBINED PDF CONTENT")
print("--------------------")

pages = document.page_content.split(
    "--- PAGE BREAK ---"
)

#In Python, the split() method always returns a list of strings (list[str]).
for number, text in enumerate(
    pages,
    start=1
):

    clean_text = " ".join(
        text.split()
    )

    print("\nSECTION", number)
    print(clean_text)

Program 5 — Page-Wise Lazy Loading and Empty Text Detection
----------------------------------------------------------------
Objective: Process PDF pages using .lazy_load() and identify pages containing no extractable text.

from langchain_community.document_loaders import PyPDFLoader


# ========================================
# CREATE PAGE-WISE PDF LOADER
# ========================================

loader = PyPDFLoader(
    file_path="company_policy.pdf",
    mode="page"
)


# ========================================
# PROCESS PDF PAGES LAZILY
# ========================================

processed_pages = 0

for document in loader.lazy_load():

    processed_pages += 1

    page_number = (
        document.metadata["page"] + 1
    )

    text = document.page_content

    print("\nPAGE", page_number)
    print("---------------------")

    if text:

        print("STATUS: Text extracted")

        print("CONTENT:", text)

    else:

        print("STATUS: No extractable text")

        print(
            "Check whether the page is blank,"
            " scanned, or requires a different"
            " extraction approach."
        )


# ========================================
# DISPLAY TOTAL
# ========================================

print("\nTOTAL PAGES PROCESSED")
print("---------------------")

print(processed_pages)
====================================================

'''