from langchain_core.documents import Document

# ========================================
# CREATE FIRST DOCUMENT
# ========================================

document1 = Document(
    page_content = 'The library opens at 8 AM.',
    metadata = {
        'source' : 'library_rules.txt',
    }
)

# ========================================
# CREATE SECOND DOCUMENT
# ========================================

document2 = Document(
    page_content = 'Students must wear their ID cards.',
    metadata = {
        'source' : 'student_rules.txt',
    }
)

# ========================================
# CREATE SECOND DOCUMENT
# ========================================

document3 = Document(
    page_content = 'Fees must be paid before the deadline.',
    metadata = {
        'source' : 'fee_rules.txt',
    }
)

# ========================================
# STORE DOCUMENTS IN A LIST
# ========================================

documents = [
    document1,
    document2,
    document3
]

# ========================================
# COUNT DOCUMENTS
# ========================================

print('TOTAL DOCUMENTS:', len(documents))

# ========================================
# DISPLAY DOCUMENT INFORMATION
# ========================================

for number, document in enumerate(documents,start=1):
    print('\nDOCUMENT:', number)
    print('CONTENT:', document.page_content)
    print('SOURCE:', document.metadata['source'])