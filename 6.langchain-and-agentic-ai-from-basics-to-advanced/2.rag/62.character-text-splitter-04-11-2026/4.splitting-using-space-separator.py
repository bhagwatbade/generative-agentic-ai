from langchain_text_splitters import CharacterTextSplitter


text = "Apple Banana Mango Orange"


splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=12,
    chunk_overlap=0
)


chunks = splitter.split_text(text)


print("TOTAL CHUNKS:", len(chunks))

for index, chunk in enumerate(chunks, start=1):

    print(f"Chunk {index}: {repr(chunk)}")
    print("Length:", len(chunk))
