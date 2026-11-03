
# ========================================
# ORIGINAL TEXT
# ========================================

text = "ABCDEFGHIJKL"


# ========================================
# CONFIGURE CHUNK SIZE
# ========================================

chunk_size = 5


# ========================================
# CREATE CHUNKS
# ========================================

chunks = []

for i in range(0, len(text), chunk_size):

    chunk = text[i:i + chunk_size]

    chunks.append(chunk)


# ========================================
# DISPLAY RESULTS
# ========================================

print("ORIGINAL TEXT:", text)

print("ORIGINAL LENGTH:", len(text))

print("TOTAL CHUNKS:", len(chunks))


for index, chunk in enumerate(chunks, start=1):

    print(
        f"Chunk {index}: {chunk} "
        f"| Length: {len(chunk)}"
    )
