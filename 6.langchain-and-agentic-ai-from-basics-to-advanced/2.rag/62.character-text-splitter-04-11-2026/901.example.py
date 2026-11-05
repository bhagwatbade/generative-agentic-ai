
from langchain_text_splitters import CharacterTextSplitter
splitter = CharacterTextSplitter(
    separator='|',
    chunk_size= 5,
    chunk_overlap=3
)

chunks = splitter.split_text('AAA|B|C|DDD')

print(chunks)