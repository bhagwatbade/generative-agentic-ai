from langchain_text_splitters import CharacterTextSplitter


text = "AAA|BBB|CCC"


# ========================================
# APPROACH 1 — keep_separator=False
# ========================================

splitter1 = CharacterTextSplitter(
    separator="|",
    chunk_size=3,
    chunk_overlap=0,
    keep_separator=False
)

chunks1 = splitter1.split_text(text)


print("WITHOUT KEEPING SEPARATOR")

for chunk in chunks1:
    print(repr(chunk))


# ========================================
# APPROACH 2 — keep_separator=True
# ========================================

splitter2 = CharacterTextSplitter(
    separator="|",
    chunk_size=3,
    chunk_overlap=0,
    keep_separator=True
)

chunks2 = splitter2.split_text(text)


print("\nKEEP SEPARATOR AT START")

for chunk in chunks2:
    print(repr(chunk))
