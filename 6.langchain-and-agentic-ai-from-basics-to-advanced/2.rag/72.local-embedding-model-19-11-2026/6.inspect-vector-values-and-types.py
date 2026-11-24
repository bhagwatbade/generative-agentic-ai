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

vector = embeddings.embed_query("AI is changing software.")

print(type(vector)) # list
print(len(vector)) # 3072 with default settings
print(type(vector[0])) # float

for i, value in enumerate(vector[:5], start=1):
    print(i, value)
