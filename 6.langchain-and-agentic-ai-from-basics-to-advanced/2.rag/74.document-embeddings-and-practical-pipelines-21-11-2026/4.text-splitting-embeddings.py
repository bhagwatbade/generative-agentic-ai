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

document = Document(
    page_content=("Python supports automation and AI. "
                  "LangChain helps create LLM applications. "
                  "LangGraph supports stateful workflows. " * 3),
    metadata={"source": "ai_courses.txt"}
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=20
)

chunks = splitter.split_documents([document])

texts = [chunk.page_content for chunk in chunks]

vectors = embeddings.embed_documents(texts)

print("Chunks:", len(chunks), "Vectors:", len(vectors))

for i, (chunk, vector) in enumerate(zip(chunks, vectors), 1):
    print(i, chunk.page_content, chunk.metadata, len(vector))