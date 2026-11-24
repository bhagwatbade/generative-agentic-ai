#################################################################
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings

small_vectors = GoogleGenerativeAIEmbeddings(
    model=os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    output_dimensionality = 256
)

#################################################################

v = small_vectors.embed_query("LangChain helps build LLM applications.")
print(len(v)) # Expected: 256
