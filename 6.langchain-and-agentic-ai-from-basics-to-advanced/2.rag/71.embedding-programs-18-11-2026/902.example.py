
#################################################################
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model=os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    output_dimensionality=256
)

#################################################################

text = 'Python is popular programming language'

#text = 'java'

vector = embeddings.embed_query(text)

print(len(vector))
print(vector)
