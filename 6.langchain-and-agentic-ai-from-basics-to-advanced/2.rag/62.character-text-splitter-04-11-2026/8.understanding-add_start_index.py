from langchain_core.documents import Document

from langchain_text_splitters import CharacterTextSplitter


document = Document(
    page_content="AAA|BBB|CCC|DDD",
    metadata={"source": "demo.txt"}
)


splitter = CharacterTextSplitter(
    separator="|",
    chunk_size=7,
    chunk_overlap=0,
    add_start_index=True
)


chunks = splitter.split_documents([document])


for index, chunk in enumerate(chunks, start=1):

    print(f"\nCHUNK {index}")
    print("CONTENT:", chunk.page_content)
    print("START INDEX:", chunk.metadata["start_index"])
    print("SOURCE:", chunk.metadata["source"])