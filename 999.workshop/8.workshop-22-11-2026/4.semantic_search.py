#################################################################
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model=os.getenv("GEMINI_EMBEDDING_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
#################################################################

import math
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def cosine_similarity(a, b):
    if len(a) != len(b):
        raise ValueError("Vector dimensions must match")
    dot_product = sum(x * y for x, y in zip(a, b))
    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    return dot_product / (magnitude_a * magnitude_b)


loader = PyPDFLoader("company_policy.pdf")

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=40
)

chunks = splitter.split_documents(documents)

chunk_texts = [chunk.page_content for chunk in chunks]

chunk_vectors = embeddings.embed_documents(chunk_texts)

question = input("Enter your company policy question: ").strip()

if not question:
    raise ValueError("Question cannot be empty")

question_vector = embeddings.embed_query(question)

results = []
for index, vector in enumerate(chunk_vectors):
    score = cosine_similarity(question_vector, vector)
    results.append((score, index))

results.sort(key=lambda item: item[0], reverse=True)
top_matches = results[:3]

print("\nTOP 3 RELEVANT POLICY CHUNKS")
print("=" * 60)

for rank, (score, index) in enumerate(top_matches, start=1):
    chunk = chunks[index]
    page_number = chunk.metadata.get("page", 0) + 1
    print(f"\nMATCH {rank}")
    print("Similarity Score:", round(score, 4))
    print("PDF Page:", page_number)
    print("Policy Content:")
    print(chunk.page_content)
