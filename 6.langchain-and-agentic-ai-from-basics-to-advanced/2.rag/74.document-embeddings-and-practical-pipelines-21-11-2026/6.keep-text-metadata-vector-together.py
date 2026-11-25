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
    Document(page_content="Python is easy.",
             metadata={"source": "python.txt"}),
    Document(page_content="Java is used in business.",
             metadata={"source": "java.txt"})
]

vectors = embeddings.embed_documents(
    [doc.page_content for doc in documents]
)

records = [
    {"text": doc.page_content,
     "metadata": doc.metadata.copy(), "embedding": vector}
    for doc, vector in zip(documents, vectors)
]

for record in records:
    print(record["text"], record["metadata"],
          len(record["embedding"]))
