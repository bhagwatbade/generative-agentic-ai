from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path='student-with-semicolon.csv',
    encoding='utf-8',
    csv_args= {
        'delimiter': ';',
    }
)

documents = loader.load()

print(len(documents))

print('==========================')

for document in documents:
    print(document.page_content)
    print(document.metadata)
    print('==========================')
