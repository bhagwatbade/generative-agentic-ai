text = 'ABCDEFGHIJKL'

chunk_size = 5
chunk_overlap = 2
chunks = []

step = chunk_size - chunk_overlap #3 from where chunk should start
for i in range(0,len(text),step):
    chunk = text[i: (i + chunk_size)] # chunk_size to take required number of chunk
    print(chunk)