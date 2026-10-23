import os
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()
import importlib
ChatGoogleGenerativeAI = importlib.import_module("langchain_google_genai").ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

from langchain_core.prompts import (
    PromptTemplate
)
from langchain_core.output_parsers import(
    StrOutputParser
)
from langchain_core.runnables import(
    RunnableParallel
)

parser = StrOutputParser()

blog_prompt = PromptTemplate.from_template(
    '''
    Prepare a blog outline about {topic}.
    Give a title, short introduction,
    5 headings and a short conclusion.
    Use simple English
    '''
)

social_prompt = PromptTemplate.from_template(
    '''
    Write a LinkedIn post about {topic}.
    Start with an attractive opening.
    Give 3 points, one call to action
    and 3 relevant hashtags.
    Keep it within 100 words.
    '''
)

email_prompt = PromptTemplate.from_template(
    '''
    Write a marketing email about {topic}.
    Give a subject, friendly greeting,
    3 benefits and a call to action.
    Use simple English. Do not invent
    dates, prices or offers.
    '''
)

blog_chain = blog_prompt | model | parser
social_chain = social_prompt | model | parser
email_chain = email_prompt | model | parser

studio = RunnableParallel(
    blog_outline = blog_chain,
    social_post = social_chain,
    marketing_email = email_chain,
)

print('\nAI CONTENT STUDIO')
topic = input('Enter a topic: ').strip()
if not topic:
    topic = 'Benefits of Learning Python'

print('Generating content. Please wait...')
result = studio.invoke({'topic': topic})

for key_name, title in [
    ('blog_outline', 'BLOG OUTLINE'),
    ('social_post', 'SOCIAL MEDIA POST'),
    ('marketing_email', 'MARKETING EMAIL'),
]:
    print('\n' + "" * 30)
    print(title)
    print("=" * 30)
    print(result[key_name])

folder = Path('AI_Content_Studio_Outputs')
folder.mkdir(exist_ok=True)

for key_name in result:
    filename = folder / (key_name + '.txt')
    filename.write_text(
        result[key_name],
        encoding='utf-8',
    )

print('\nAll three files saved in:')
print(folder.resolve())

# Topic : Benefits of Learning Python
