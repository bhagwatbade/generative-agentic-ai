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