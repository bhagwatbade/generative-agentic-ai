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