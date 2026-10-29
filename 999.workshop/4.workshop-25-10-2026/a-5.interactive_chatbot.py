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
# STEP 3 - CREATE HISTORY
# ========================================
messages = [
    SystemMessage(
        content="""
 You are a friendly AI assistant.
 Reply in simple English.
 Use the supplied conversation history.
 Do not invent missing details.
 """
    )
]

# ========================================
# STEP 4 - WELCOME MESSAGE
# ========================================
print("\nMY FIRST AI CHATBOT")
print("=" * 30)
print("Type exit to stop the conversation.")
# ========================================
# STEP 5 - INTERACTIVE CHAT LOOP
# ========================================

while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break
    if not user_input:
        print("Please enter a message.")
        continue
    messages.append(
        HumanMessage(content=user_input)
    )
    response = llm.invoke(messages)
    print("\nAI:", parser.invoke(response))
    messages.append(response)

# ========================================
# STEP 6 - HISTORY SUMMARY
# ========================================

print("\nCHAT HISTORY SUMMARY")
print("=" * 30)
print("Total Messages:", len(messages))
for message in messages:
    print(type(message).__name__)
