from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


# ========================================
# ORIGINAL TEXT
# ========================================

text = "ABCDEFGHIJKL"


# ========================================
# CREATE TEXT SPLITTER
# ========================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=5,
    chunk_overlap=2,
    separators=[""]
)


# ========================================
# SPLIT TEXT
# ========================================

chunks = splitter.split_text(text)


# ========================================
# DISPLAY RESULTS
# ========================================

print("RETURN TYPE:", type(chunks))

print("TOTAL CHUNKS:", len(chunks))


for index, chunk in enumerate(chunks, start=1):

    print(f"Chunk {index}: {chunk}")