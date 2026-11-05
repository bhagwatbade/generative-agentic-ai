from langchain_text_splitters import CharacterTextSplitter


# ========================================
# ORIGINAL TEXT
# ========================================

text = (
    "Python is easy.\n\n"
    "Java is powerful.\n\n"
    "LangChain builds AI apps."
)


# ========================================
# CREATE SPLITTER
# ========================================

splitter = CharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=0
)


# ========================================
# SPLIT TEXT
# ========================================

chunks = splitter.split_text(text)


# ========================================
# DISPLAY RESULTS
# ========================================

print("TOTAL CHUNKS:", len(chunks))

for index, chunk in enumerate(chunks, start=1):

    print(f"\nCHUNK {index}")

    print(repr(chunk))

    print("LENGTH:", len(chunk))
