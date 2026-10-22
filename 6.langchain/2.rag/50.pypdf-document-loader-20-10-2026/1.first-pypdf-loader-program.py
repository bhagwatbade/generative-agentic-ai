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

print(type(documents))
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