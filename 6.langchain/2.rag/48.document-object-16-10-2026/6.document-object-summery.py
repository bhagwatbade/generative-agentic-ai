from langchain_core.documents import Document

# ========================================
# CREATE STUDENT INFORMATION DOCUMENT
# ========================================

documents = [

    Document(
        page_content = 'Admission start on 1 November 2026.',
        metadata = {
            'source' : 'admission_notice.txt',
            'department' : 'Admissions',
        }
    ),

    Document(
        page_content = 'The library is open at 8 AM to 6 PM.',
        metadata = {
            'source' : 'library_notice.txt',
            'department' : 'Library',
        }
    ),

    Document(
        page_content = 'All Student must carry their ID cards.',
        metadata = {
            'source' : 'student_notice.txt'
        }
    )

]

# ========================================
# DISPLAY EVERY DOCUMENT
# ========================================

for number, document in enumerate(documents,start=1):
    print('\nDOCUMENT:', number)
    print('CONTENT:', document.page_content)
    print('SOURCE:', document.metadata.get('source', 'Unknown'))
    print('DEPARTMENT:', document.metadata.get('department', 'Not specified'))