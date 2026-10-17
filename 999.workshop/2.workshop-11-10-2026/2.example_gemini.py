from pydantic import BaseModel, Field
import importlib
ChatGoogleGenerativeAI = importlib.import_module("langchain_google_genai").ChatGoogleGenerativeAI

import os

class Student(BaseModel):
    name: str | None = Field(
        default = None,
        description = "Name of the Student",
    )
    age: int = Field(
        description = "Age of the Student",
    )
    course: str = Field(
        description = "Course required for the Student",
    )

llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
        google_api_key=os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY"),
)

structured_llm = llm.with_structured_output(Student)

data = input('Enter Student Information:')


result = structured_llm.invoke(data)

print(result)

print(type(result))

print("Name : ", result.name)
print("Age : ", result.age)
print("Course : ", result.course)