import os

'''
from getpass import getpass
from langchain_openai import ChatOpenAI
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
# STEP 3 - ASK ONE INTERVIEW QUESTION
# ========================================
response = llm.invoke(
    """
    Ask one basic Python interview question
    suitable for a fresher.
    Do not give the answer.
     """
)
# ========================================
# STEP 4 - DISPLAY RESPONSE AND TYPE
# ========================================
print("\nAI INTERVIEWER")
print("=" * 30)
print(parser.invoke(response))
print("\nRESPONSE TYPE")
print("=" * 30)
print(type(response))