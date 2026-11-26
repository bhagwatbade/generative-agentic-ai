from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("company_policy.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=40
)

chunks = splitter.split_documents(documents)

print("COMPANY POLICY TEXT SPLITTER")
print("=" * 50)
print("Original Documents:", len(documents))
print("Total Chunks:", len(chunks))

for index, chunk in enumerate(chunks, start=1):
    print(f"\nCHUNK {index}")
    print("-" * 50)
    print(chunk.page_content)
    print("Chunk Length:", len(chunk.page_content))
    print("Metadata:", chunk.metadata)
