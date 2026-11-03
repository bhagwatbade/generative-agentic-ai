from langchain_core.documents import Document

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


# ========================================
# CREATE DOCUMENT
# ========================================

document = Document(
    page_content="ABCDEFGHIJKL",

    metadata={
        "source": "sample.txt"
    }
)


# ========================================
# CREATE TEXT SPLITTER
# ========================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=5,
    chunk_overlap=2,
    separators=[""]
)


# ========================================
# SPLIT DOCUMENT
# ========================================

chunks = splitter.split_documents(
    [document]
)


# ========================================
# DISPLAY RESULTS
# ========================================

print("TOTAL DOCUMENT CHUNKS:", len(chunks))


for index, chunk in enumerate(chunks, start=1):

    print(f"\nCHUNK {index}")

    print("CONTENT:", chunk.page_content)

    print("METADATA:", chunk.metadata)

    print("TYPE:", type(chunk).__name__)
