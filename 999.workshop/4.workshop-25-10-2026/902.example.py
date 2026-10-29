import os


from langchain_core.messages import SystemMessage, HumanMessage


#################################################################
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
#################################################################

chain = model | parser



response1 = chain.invoke(
    """
    My name is Ravi.
    I am preparing for python Developer interview.
    Please acknowledge this.
   """
)

print('\nFirst response')
print("=" * 30)
print(response1)

response2 = chain.invoke(
    """
    What is my name?.
    Which interview am I preparing for?.
   """
)

print('\nSecond response')
print("=" * 30)
print(response2)

