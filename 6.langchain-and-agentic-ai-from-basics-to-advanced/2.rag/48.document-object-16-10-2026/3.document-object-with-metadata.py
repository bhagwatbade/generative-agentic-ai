from langchain_core.documents import Document

# ========================================
# CREATE DOCUMENT WITH METADATA
# ========================================

document = Document(
    page_content = 'The office opens at 9 AM.',
    metadata = {
        'source' : 'office_rules.txt',
        'department' : 'Administration',
        'year' : 2026
    }
)

# ========================================
# ACCESS PAGE CONTENT
# ========================================

print('PAGE CONTENT')
print('------------')
print(document.page_content)

# ========================================
# ACCESS COMPLETE METADATA
# ========================================

print('\nCOMPLETE METADATA')
print('------------')
print(document.metadata)

# ========================================
# ACCESS INDIVIDUAL METADATA VALUES
# ========================================

print('\nSOURCE')
print('------------')
print(document.metadata['source'])

print('\nDEPARTMENT')
print('------------')
print(document.metadata['department'])

print('\nYEAR')
print('------------')
print(document.metadata['year'])