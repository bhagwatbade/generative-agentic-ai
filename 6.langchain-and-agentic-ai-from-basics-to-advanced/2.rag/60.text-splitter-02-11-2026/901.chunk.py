text = 'ABCDEFGHIJKL'

chunk_size = 5
chunks = []

for i in range(0,len(text),chunk_size):
    chunk = text[i : (i + chunk_size)]
    chunks.append(chunk)

for index, chunk in enumerate(chunks, start = 1):
    print(f'Chunk {index}: {chunk} | Length: {len(chunk)}')
