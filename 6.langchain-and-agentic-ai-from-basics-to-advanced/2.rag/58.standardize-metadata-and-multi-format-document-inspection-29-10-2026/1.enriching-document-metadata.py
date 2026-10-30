from langchain_core.documents import Document


# ========================================
# CREATE DOCUMENT
# ========================================

document = Document(
    page_content="Library closes at 6 PM.",
    metadata={
        "source": "library_rules.txt"
    }
)


# ========================================
# PRESERVE ORIGINAL METADATA
# ========================================

original_metadata = document.metadata.copy()


# ========================================
# ADD CUSTOM METADATA
# ========================================

document.metadata.update({
    "source_type": "txt",
    "department": "Library",
    "category": "Notice"
})


# ========================================
# DISPLAY RESULTS
# ========================================

print("SOURCE:", document.metadata["source"])

print(
    "SOURCE TYPE:",
    document.metadata["source_type"]
)

print(
    "DEPARTMENT:",
    document.metadata["department"]
)

print(
    "CATEGORY:",
    document.metadata["category"]
)

print(
    "SOURCE PRESERVED:",
    document.metadata["source"]
    ==
    original_metadata["source"]
)