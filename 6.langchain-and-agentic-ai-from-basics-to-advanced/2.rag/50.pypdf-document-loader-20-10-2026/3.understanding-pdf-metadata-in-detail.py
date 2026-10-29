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