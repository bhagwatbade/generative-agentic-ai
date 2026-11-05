from langchain_core.documents import Document

from langchain_text_splitters import CharacterTextSplitter


# ========================================
# CREATE DOCUMENT
# ========================================

document = Document(
    page_content="AAA|BBB|CCC|DDD",

    metadata={
        "source": "company_policy.txt",
        "department": "HR"
    }
)


# ========================================
# CREATE SPLITTER
# ========================================

splitter = CharacterTextSplitter(
    separator="|",
    chunk_size=7,
    chunk_overlap=0
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

print("TOTAL CHUNKS:", len(chunks))


for index, chunk in enumerate(chunks, start=1):

    print(f"\nCHUNK {index}")

    print("CONTENT:", chunk.page_content)

    print("METADATA:", chunk.metadata)

    print("TYPE:", type(chunk).__name__)
