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

question = "What is Python?"
docs = ["Python is a language.", "Java is a language."]

query_vector = embeddings.embed_query(question)

doc_vectors = embeddings.embed_documents(docs)

print(type(query_vector), len(query_vector))

print(type(doc_vectors), len(doc_vectors))

print(type(doc_vectors[0]), len(doc_vectors[0]))