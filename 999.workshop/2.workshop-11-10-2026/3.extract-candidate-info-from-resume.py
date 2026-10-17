import os
from langchain_openai import ChatOpenAI
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
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)
structured_llm = llm.with_structured_output(Candidate)
text = input("Enter candidate information: ")
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
print("\nPYTHON DICTIONARY")
print(result.model_dump())
print("\nJSON STRING")
print(result.model_dump_json())
