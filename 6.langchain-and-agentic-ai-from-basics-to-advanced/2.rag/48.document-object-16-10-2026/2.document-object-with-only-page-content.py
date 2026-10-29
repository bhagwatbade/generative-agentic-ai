from langchain_core.documents import Document

# ========================================
# CREATE DOCUMENT OBJECT
# ========================================

document = Document(
    page_content = 'Python is a popular programming language.',
)

# ========================================
# ACCESS PAGE CONTENT
# ========================================

print('PAGE CONTENT')
print('------------')
print(document.page_content)

# ========================================
# ACCESS METADATA
# ========================================

print('\nMETADATA')
print('------------')
print(document.metadata)

# ========================================
# CHECK OBJECT TYPE
# ========================================

print('\nOBJECT TYPE')
print('------------')
print(type(document).__name__)