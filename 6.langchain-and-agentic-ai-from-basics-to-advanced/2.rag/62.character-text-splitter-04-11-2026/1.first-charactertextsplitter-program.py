from langchain_text_splitters import CharacterTextSplitter


# ========================================
# ORIGINAL TEXT
# ========================================

text = "AAA|BBB|CCC|DDD"


# ========================================
# CREATE TEXT SPLITTER
# ========================================

splitter = CharacterTextSplitter(
    separator="|",
    chunk_size=7,
    chunk_overlap=0
)


# ========================================
# SPLIT TEXT
# ========================================

chunks = splitter.split_text(text)


# ========================================
# DISPLAY RESULTS
# ========================================

print("ORIGINAL TEXT:", text)
print("TOTAL CHUNKS:", len(chunks))
print("RETURN TYPE:", type(chunks))

for index, chunk in enumerate(chunks, start=1):

    print(
        f"Chunk {index}: {chunk} "
        f"| Length: {len(chunk)}"
    )