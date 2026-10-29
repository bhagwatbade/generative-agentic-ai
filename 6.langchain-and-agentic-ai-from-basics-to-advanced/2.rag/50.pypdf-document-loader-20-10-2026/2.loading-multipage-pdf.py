from langchain_community.document_loaders import PyPDFLoader

# ========================================
# CREATE PAGE-WISE PDF LOADER
# ========================================

loader = PyPDFLoader(
    file_path="company_policy.pdf",
    mode="page",
    #mode="single",
    #pages_delimiter= '\n---------------- PAGE BREAK --------------------\n'
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

    page_index = document.metadata.get("page",0)

    page_number = page_index + 1



    print("\nPAGE", page_number)
    print("---------------------")

    print("CONTENT:\n", document.page_content)