from langchain_core.documents import Document

# ========================================
# CREATE DOCUMENT
# ========================================

document = Document(
    page_content = 'Student must carry their ID cards.',
    metadata = {
        'source' : 'college_notice.txt',
        'department' : 'Student Services',
    }
)

# ========================================
# ACCESS EXISTING METADATA
# ========================================

print('\nSOURCE')
print('------------')
print(document.metadata['source'])

print('\nDEPARTMENT')
print('------------')
print(document.metadata.get('department'))

# ========================================
# ACCESS MISSING METADATA SAFELY
# ========================================

print('\nAUTHOR')
print('------------')
print(document.metadata.get('author', 'NOT AVAILABLE'))
