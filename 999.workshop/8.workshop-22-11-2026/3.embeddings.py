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

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("company_policy.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=40
)

chunks = splitter.split_documents(documents)
chunk_texts = [chunk.page_content for chunk in chunks]

chunk_vectors = embeddings.embed_documents(chunk_texts)

print("COMPANY POLICY EMBEDDINGS")
print("=" * 50)
print("Total Chunks:", len(chunks))
print("Total Vectors:", len(chunk_vectors))
print("Vector Dimensions:", len(chunk_vectors[0]))
print("\nFIRST CHUNK:")
print(chunk_texts[0])
print("\nFIRST 10 EMBEDDING VALUES:")
print(chunk_vectors[0][:10])
print("\nText Type:", type(chunk_texts[0]))
print("Vector Type:", type(chunk_vectors[0]))