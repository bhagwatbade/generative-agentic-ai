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

import math

def cosine_similarity(a, b):
    if len(a) != len(b):
        raise ValueError("Dimensions must match")
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x * x for x in a))
    mag_b = math.sqrt(sum(y * y for y in b))
    if mag_a == 0 or mag_b == 0:
        raise ValueError("Zero vector not supported")
    return dot / (mag_a * mag_b)

s1 = "I want to learn Python."
s2 = "How can I study Python programming?"
s3 = "The weather is very hot today."

v1, v2, v3 = [embeddings.embed_query(s) for s in (s1, s2, s3)]

print("Related:", round(cosine_similarity(v1, v2), 4))

print("Unrelated:", round(cosine_similarity(v1, v3), 4))