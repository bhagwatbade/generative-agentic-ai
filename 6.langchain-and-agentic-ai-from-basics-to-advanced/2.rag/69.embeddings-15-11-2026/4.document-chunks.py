# ========================================
# PROGRAM 4 — DOCUMENT CHUNKS
# ========================================

from langchain_core.documents import Document
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

documents = [
    Document(
        page_content=(
            "Python is a popular programming language. "
            "Java is widely used in enterprise applications. "
            "LangChain helps build applications using LLMs."
        ),
        metadata={"source": "courses.txt"}
    )
]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=55,
    chunk_overlap=0
)

chunks = splitter.split_documents(documents)

print("Total Chunks:", len(chunks))

for index, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {index}:")
    print(chunk.page_content)

print("\nNext Step:")
print("Generate embeddings for these chunks")