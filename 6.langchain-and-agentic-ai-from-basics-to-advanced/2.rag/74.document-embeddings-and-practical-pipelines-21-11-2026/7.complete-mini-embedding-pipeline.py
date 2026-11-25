#################################################################
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model=os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

#################################################################

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

documents = [
    Document(page_content="Python is used in automation and AI.",
             metadata={"source": "python_course.txt"}),
    Document(page_content="LangChain helps build LLM applications.",
             metadata={"source": "langchain_course.txt"})
]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=60, chunk_overlap=10
)

chunks = splitter.split_documents(documents)

texts = [chunk.page_content for chunk in chunks]

vectors = embeddings.embed_documents(texts)

if len(chunks) != len(vectors):
    raise ValueError("Chunk count and embedding count differ")

records = [
    {"chunk_id": i, "text": chunk.page_content,
     "metadata": chunk.metadata.copy(), "embedding": vector}
    for i, (chunk, vector) in enumerate(zip(chunks, vectors), 1)
]

print("Documents:", len(documents), "Chunks:", len(chunks))

print("Vectors:", len(vectors), "Records:", len(records))

for rec in records:
    print(rec["chunk_id"], rec["metadata"],
          len(rec["embedding"]))