# https://www.durgasoftonline.com/s/pages/new-batches/

from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.durgasoftonline.com/s/pages/new-batches/'

loader = WebBaseLoader(
    web_path = url
)

documents = loader.load()

print('=' * 100)


print(len(documents))

print('=' * 100)


document = documents[0]

print(document.page_content)

print('=' * 100)

print(document.metadata)