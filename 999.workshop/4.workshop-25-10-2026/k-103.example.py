import os
from urllib import response

from langchain_core import messages
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


messages = [
    SystemMessage(
        content='''
        You are a helpful AI assistant.
        
        use the supplied conversation history.
        if information is unavailable, say "I don't know"
        '''
    )

]

messages.append(HumanMessage(
    content='''
     My name is Ravi.
    I am preparing for python Developer interview.
    Please acknowledge this.
    '''
))

response1 = model.invoke(messages)

print('\nFirst response')
print("=" * 30)
print(response1)

messages.append(response1)

messages.append(HumanMessage(
    content='''
     What is my name?.
    Which interview am I preparing for?.
    '''
))

response2 = model.invoke(messages)
print('\nSecond response')
print("=" * 30)
print(response2)

messages.append(response2)

for message in messages:
    print(type(message).__name__)
    print(message.content)
    print()

print('Total msg :', len(messages))


