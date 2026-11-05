from langchain_text_splitters import CharacterTextSplitter


# ========================================
# ORIGINAL TEXT
# ========================================

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# ========================================
# CREATE SPLITTER
# ========================================

splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=5,
    chunk_overlap=0
)


# ========================================
# SPLIT TEXT
# ========================================

chunks = splitter.split_text(text)


# ========================================
# DISPLAY RESULTS
# ========================================

print("ORIGINAL LENGTH:", len(text))
print("CONFIGURED CHUNK SIZE:", 5)
print("TOTAL CHUNKS:", len(chunks))

for index, chunk in enumerate(chunks, start=1):

    print(f"Chunk {index}: {chunk}")
    print("Length:", len(chunk))
