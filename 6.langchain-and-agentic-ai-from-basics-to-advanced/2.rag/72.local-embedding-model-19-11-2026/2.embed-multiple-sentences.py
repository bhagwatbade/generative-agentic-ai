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

sentences = [
    "I want to learn Python.",
    "I want to study Python programming.",
    "The weather is very hot today."
]

for sentence in sentences:
    v = embeddings.embed_query(sentence)
    print(sentence, len(v), v[:3])
