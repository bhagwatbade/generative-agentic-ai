# ========================================
# ORIGINAL TEXT
# ========================================

text = "ABCDEFGHIJKL"


# ========================================
# CONFIGURATION
# ========================================

chunk_size = 5

chunk_overlap = 2


# ========================================
# VALIDATE CONFIGURATION
# ========================================

if not 0 <= chunk_overlap < chunk_size:
    raise ValueError(
        "Overlap must be non-negative "
        "and smaller than chunk size"
    )


# ========================================
# CALCULATE STEP SIZE
# ========================================

step = chunk_size - chunk_overlap


# ========================================
# CREATE CHUNKS
# ========================================

chunks = []

for i in range(0, len(text), step):

    chunk = text[i:i + chunk_size]

    chunks.append(chunk)


# ========================================
# DISPLAY RESULTS
# ========================================

print("CHUNK SIZE:", chunk_size)

print("CHUNK OVERLAP:", chunk_overlap)

print("STEP SIZE:", step)


for index, chunk in enumerate(chunks, start=1):

    print(f"Chunk {index}: {chunk}")