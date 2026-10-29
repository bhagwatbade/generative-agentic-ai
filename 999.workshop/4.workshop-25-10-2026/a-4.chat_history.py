import os
from getpass import getpass
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage, HumanMessage
)

'''
# ========================================
# STEP 1 - GET OPENAI API KEY
# ========================================
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    api_key = getpass(
        "Enter your OpenAI API key: "
    ).strip()
if not api_key:
    raise ValueError(
        "OpenAI API key is required."
    )
# ========================================
# STEP 2 - CREATE CHAT MODEL
# ========================================
llm = ChatOpenAI(
    model="gpt-5.4-mini",
    api_key=api_key
)
'''

# ========================================
# STEP 1 - CREATE CHAT MODEL
# ========================================

#################################################################
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

# ========================================
# STEP 3 - CREATE CONVERSATION HISTORY
# ========================================
messages = [
    SystemMessage(
        content=
        '''
         You are a helpful AI assistant.
         Use the supplied conversation history.
         If information is unavailable,
         say "I don't know".
        '''
    )
]
# ========================================
# STEP 4 - ADD FIRST USER MESSAGE
# ========================================
messages.append(
    HumanMessage(
        content=
        '''
        My name is Ravi.
        I am preparing for a Python
        Developer interview.
        '''
    )
)

# ========================================
# STEP 5 - FIRST AI RESPONSE
# ========================================
response1 = llm.invoke(messages)
print("\nFIRST RESPONSE")
print("=" * 30)
print(parser.invoke(response1))
messages.append(response1)
# ========================================
# STEP 6 - SECOND USER MESSAGE
# ========================================
messages.append(
    HumanMessage(
        content="""
 What is my name?
 Which job interview am I
 preparing for?
 """
    )
)

# ========================================
# STEP 7 - SECOND CALL WITH HISTORY
# ========================================
response2 = llm.invoke(messages)
print("\nSECOND RESPONSE")
print("=" * 30)
print(parser.invoke(response2))
messages.append(response2)
# ========================================
# STEP 8 - INSPECT MESSAGE HISTORY
# ========================================
print("\nCONVERSATION HISTORY")
print("=" * 30)
for message in messages:
    print()
    print(type(message).__name__)
    print(parser.invoke(message))

print("\nTOTAL MESSAGES:", len(messages))
