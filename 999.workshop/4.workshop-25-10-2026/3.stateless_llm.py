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
# STEP 3 - FIRST INDEPENDENT CALL
# ========================================
response1 = llm.invoke(
    """
    My name is Ravi.
    I am preparing for a Python Developer
    interview. Please acknowledge this.
    """
)
print("\nFIRST RESPONSE")
print("=" * 30)
print(parser.invoke(response1))
# ========================================
# STEP 4 - SECOND INDEPENDENT CALL
# ========================================
response2 = llm.invoke(
    """
    What is my name?
    Which interview am I preparing for?
    Answer only using information available
    in this current request.
    If the information is not available,
    say "I don't know".
    """
)
print("\nSECOND RESPONSE")
print("=" * 30)
print(parser.invoke(response2))