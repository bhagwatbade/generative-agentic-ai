from langchain_huggingface import HuggingFaceEmbeddings

local_embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector = local_embeddings.embed_query(
    "Python is a programming language."
)

print("Type:", type(vector))
print("Dimensions:", len(vector))
print("First 5 values:", vector[:5])