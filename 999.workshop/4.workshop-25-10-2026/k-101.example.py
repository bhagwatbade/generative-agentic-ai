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


messages = [
    SystemMessage(
        content='''
        You are a friendly and professional python interviewer.
        
        The candidate is fresher.
        Ask one basic python question.
        Use simple English.
        Do not provide the answer.
        Wait for the candidate's answer.
        '''
    ),
    HumanMessage(
        content='Start my Python interview.'
    )

]

chain = model | parser

response = chain.invoke(messages)

print(response)