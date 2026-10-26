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
        Reply in simple english.
        use the supplied conversation history.
        if information is unavailable, say "I don't know"
        '''
    )

]

while True:
    user_input = input('\nYou: ').strip()
    if user_input.lower() == 'exit':
        break

    messages.append(HumanMessage(content=user_input))

    response = chain.invoke(messages)
    print('AI Response',response)
    messages.append(response)