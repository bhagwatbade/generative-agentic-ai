
#################################################################
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
#################################################################

response = llm.invoke('Provide Python top 5 interview questions without answers')

print(type(response))
print(response.content[0]['text'])
