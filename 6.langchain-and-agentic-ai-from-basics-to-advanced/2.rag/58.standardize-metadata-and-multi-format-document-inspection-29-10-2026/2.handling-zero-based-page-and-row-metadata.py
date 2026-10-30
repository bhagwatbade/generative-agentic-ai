from langchain_core.documents import Document


# ========================================
# CREATE SAMPLE DOCUMENTS
# ========================================

documents = [

    Document(
        page_content="Employee leave policy.",
        metadata={
            "source": "policy.pdf",
            "page": 0
        }
    ),

    Document(
        page_content="name: Ravi",
        metadata={
            "source": "students.csv",
            "row": 0
        }
    ),

    Document(
        page_content="Library opens at 8 AM.",
        metadata={
            "source": "library.txt"
        }
    )

]


# ========================================
# INSPECT SOURCE-SPECIFIC METADATA
# ========================================

for document in documents:

    metadata = document.metadata

    print("\nSOURCE:", metadata["source"])

    page_index = metadata.get("page")

    row_index = metadata.get("row")

    if page_index is not None:

        print(
            "DISPLAY PAGE:",
            page_index + 1
        )

    elif row_index is not None:

        print(
            "DISPLAY ROW:",
            row_index + 1
        )

    else:

        print(
            "PAGE/ROW:",
            "Not applicable"
        )