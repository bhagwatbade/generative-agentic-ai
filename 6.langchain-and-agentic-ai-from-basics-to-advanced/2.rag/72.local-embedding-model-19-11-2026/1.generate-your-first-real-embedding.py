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

text = 'Python is popular programming language.'

vector = embeddings.embed_query(text)

print("Text:", text)
print("Type:", type(vector))
print("Dimensions:", len(vector))
print("First 5 values:", vector[:5])