import importlib
import os

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

ChatGoogleGenerativeAI = importlib.import_module("langchain_google_genai").ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

prompt = PromptTemplate.from_template(
    "Explain {topic} in very simple english"
)

input_topic = input("Enter Topic:")
chain = prompt | model | StrOutputParser()
response = chain.invoke({"topic": input_topic})
print(response)

