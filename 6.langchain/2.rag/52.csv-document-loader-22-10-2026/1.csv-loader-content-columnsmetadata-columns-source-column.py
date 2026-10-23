from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path='students.csv',
    encoding='utf-8',
    content_columns = ['Name','Fee','Course'],
    metadata_columns= ['Course'],
    source_column = 'ID' # replace metadata 'source' with column value
)

documents = loader.load()

print(len(documents))

print('==========================')

for document in documents:
    print(document.page_content)
    print(document.metadata)
    print('==========================')
