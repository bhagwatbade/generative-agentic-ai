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

texts = ["Python", "Java", "AI", "Machine Learning"]
vectors = embeddings.embed_documents(texts)
expected_dimensions = 3072
assert len(texts) == len(vectors), "Count mismatch"
for i, vector in enumerate(vectors, 1):
    assert len(vector) == expected_dimensions, f"Wrong size: {i}"
    print(f"Vector {i}: {len(vector)} dimensions - Valid")
print("All embeddings validated successfully.")
