# ========================================
# ORIGINAL TEXT
# ========================================

text = (
    "Python is easy.\n\n"
    "LangChain helps create AI applications.\n\n"
    "RAG uses documents."
)


# ========================================
# DEFINE SEPARATOR
# ========================================

separator = "\n\n"


# ========================================
# SPLIT TEXT
# ========================================

chunks = text.split(separator)


# ========================================
# DISPLAY RESULTS
# ========================================

print("TOTAL CHUNKS:", len(chunks))


for index, chunk in enumerate(chunks, start=1):

    print(f"\nChunk {index}:")
    print(chunk)
