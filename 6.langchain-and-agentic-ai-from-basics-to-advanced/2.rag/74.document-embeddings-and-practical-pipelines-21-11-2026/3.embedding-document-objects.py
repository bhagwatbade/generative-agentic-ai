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

documents = [
    Document(page_content="Python is easy to learn.",
             metadata={"source": "python.txt", "course": "Python"}),
    Document(page_content="Java supports OOP.",
             metadata={"source": "java.txt", "course": "Java"}),
    Document(page_content="LangChain builds LLM apps.",
             metadata={"source": "langchain.txt", "course": "AI"})
]

texts = [doc.page_content for doc in documents]

vectors = embeddings.embed_documents(texts)

for doc, vector in zip(documents, vectors):
    print(doc.page_content, doc.metadata, len(vector))