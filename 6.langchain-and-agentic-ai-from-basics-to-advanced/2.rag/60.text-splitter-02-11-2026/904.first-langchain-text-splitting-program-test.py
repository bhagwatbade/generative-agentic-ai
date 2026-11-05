from langchain_text_splitters import (
    CharacterTextSplitter,
RecursiveCharacterTextSplitter
)


# ========================================
# ORIGINAL TEXT
# ========================================

# text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ\n\njhafsbksldbfvj\n\njshfdbvsd\n\njhdabfad\n\nfadf\n\nhfgsfkj\n\nsbdfjb'
text = '123\n\n98\n\n1 1\n\n98\n\n1234\n\n987\n\n12'

print(len(text))

# ========================================
# CREATE TEXT SPLITTER
# ========================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=4,
    separators=['\n\n']
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

    print(f"Chunk {index}: {chunk} | Length : {len(chunk)}")