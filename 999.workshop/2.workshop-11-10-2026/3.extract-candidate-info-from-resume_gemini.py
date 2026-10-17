import os

import importlib
ChatGoogleGenerativeAI = importlib.import_module("langchain_google_genai").ChatGoogleGenerativeAI
from dotenv import load_dotenv

from pydantic import BaseModel, Field

class Candidate(BaseModel):
    name: str = Field(
        description="Name of the person"
    )
    profession: str = Field(
        description="Profession or job role"
    )
    city: str | None = Field(
        default=None,
        description="City where the person lives"
    )
    experience: int | None = Field(
        default=None,
        description="Years of professional experience"
    )
    skills: list[str] = Field(
        description="Professional skills mentioned in the text"
    )
    email: str | None = Field(
        default=None,
        description="Email address if mentioned"
    )
    mobile: str | None = Field(
        default=None,
        description="Mobile number if mentioned"
    )

load_dotenv()
llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite"),
    google_api_key=os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY"),
)

structured_llm = llm.with_structured_output(Candidate)
text = input("Enter candidate information: ")

print("text :", text)

instruction = f"""
Extract candidate information from the text below.
Rules:
- Use only information available in the text.
- Do not invent missing information.
- If optional information is unavailable, return None.
Text:
{text}
"""
result = structured_llm.invoke(instruction)
print("\nEXTRACTED INFORMATION")
print("Name :", result.name)
print("Profession :", result.profession)
print("City :", result.city)
print("Experience :", result.experience)
print("Skills :", result.skills)
print("Email :", result.email)
print("Mobile :", result.mobile)
print("\nPYTHON DICTIONARY")
print(result.model_dump())
print("\nJSON STRING")
print(result.model_dump_json())
