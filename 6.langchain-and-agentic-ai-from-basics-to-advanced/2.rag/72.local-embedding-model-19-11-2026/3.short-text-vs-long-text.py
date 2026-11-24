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
    "Python",
    "Python is easy to learn.",
    "Python is widely used in AI and automation."
]

for text in texts:
    v = embeddings.embed_query(text)
    print("Characters:", len(text), "Dimensions:", len(v))