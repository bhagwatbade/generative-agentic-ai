from langchain_core.documents import Document

document = Document(
    page_content = 'Python is a programming language',
    metadata = {
        'source' : 'python_notes.txt',
        'department' : 'training',
    }
)

print('-----------------------------------------')
print(document)
print('-----------------------------------------')
print(type(document).__name__)
print('-----------------------------------------')
print(document.page_content)
print('-----------------------------------------')
print(document.metadata)
print('-----------------------------------------')
print(document.metadata['source'])
print('-----------------------------------------')
print(document.metadata['department'])
print('-----------------------------------------')
#print(document.metadata['author']) # KeyError: 'author'
print(document.metadata.get('author'))
print(document.metadata.get('author', 'Not Available'))
print('-----------------------------------------')
