import os
from dotenv import load_dotenv
from langchain_core import prompts
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

import importlib
ChatGoogleGenerativeAI = importlib.import_module("langchain_google_genai").ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def get_ai_response_text(content):
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        text_parts = []
        for item in content:
            if isinstance(item, str):
                text_parts.append(item)
            elif isinstance(item, dict) and item.get("type") == "text":
                text = item.get("text", "")
                if text:
                    text_parts.append(text)
        if text_parts:
            return "\n".join(part.strip() for part in text_parts if part.strip())
    return str(content).strip()

#-------------------------- dynamic prompt -----------------------------------------

'''
response = model.invoke(
  'write 5 benefit of learning python.'
)
print('\nAI Response:')
print('-------------------------')
print(get_ai_response_text(response.content))

'''
#---------------------------- dynamic prompt with  PromptTemplate ---------------------------------------
'''
prompt = PromptTemplate.from_template('write 5 benefit of learning {topic}.')
topic = input('Enter topic: ')
prompt_value = prompt.invoke({'topic': topic}) # if used chain not required
response = model.invoke(prompt)  # if used chain not required
print('\nAI Response:')
print('-------------------------')
print(get_ai_response_text(response.content))
'''

#---------------------------- Langchain  RunnableSequence---------------------------------------

prompt = PromptTemplate.from_template('write 5 benefit of learning {topic}.')

topic = input('Enter topic: ')

parser = StrOutputParser()

chain = prompt | model | parser

print('\nAI Response:')
print('-------------------------')
print(chain.invoke({'topic': topic}))

#-------------------------------------------------------------------



