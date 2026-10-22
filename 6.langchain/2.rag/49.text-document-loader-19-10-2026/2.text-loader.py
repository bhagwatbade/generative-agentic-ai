from pathlib import Path

from langchain_community.document_loaders import TextLoader

file_path = Path(__file__).resolve().parent / 'sample.txt'

loader = TextLoader(file_path=str(file_path), encoding='utf-8')
documents = loader.load()

print('TOTAL DOCUMENTS:', len(documents))

for number, document in enumerate(documents, start=1):
    print('\nDOCUMENT:', number)
    print('CONTENT:', document.page_content)
    print('SOURCE:', document.metadata['source'])
