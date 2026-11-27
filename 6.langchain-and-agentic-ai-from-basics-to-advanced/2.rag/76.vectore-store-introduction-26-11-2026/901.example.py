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

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.vectorstores import FAISS

from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

texts = [
    "Python is a programming language",
    "Java is an object-oriented language",
    "FAISS is used for similarity search"
]

vector_store = FAISS.from_texts(texts, embeddings)

query = "What is FAISS?"

docs = vector_store.similarity_search(query, k=1)

context = docs[0].page_content

llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


prompt = f"Answer using this context: {context}\nQuestion: {query}"

response = llm.invoke(prompt)

print(parser.invoke(response))