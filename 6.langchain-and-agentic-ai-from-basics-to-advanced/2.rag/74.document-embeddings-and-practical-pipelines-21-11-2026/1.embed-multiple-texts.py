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

texts = [
    "Python is a programming language.",
    "Java is used in enterprise applications.",
    "LangChain helps build LLM applications."
]

vectors = embeddings.embed_documents(texts)

print("Total texts:", len(texts))
print("Total vectors:", len(vectors))

for i, vector in enumerate(vectors, start=1):
    print(i, "dimensions:", len(vector), "first 5:", vector[:5])