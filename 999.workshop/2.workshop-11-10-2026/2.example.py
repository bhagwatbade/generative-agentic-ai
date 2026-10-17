from pydantic import BaseModel, Field

from langchain_openai import  ChatOpenAI
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


llm = ChatOpenAI(
    model = "gpt-4o-mini",
    api_key = os.environ.get("OPENAI_API_KEY")
)

structured_llm = llm.with_structured_output(Student)

data = input('Enter Student Information:')

result = structured_llm.invoke(data)

print(result)

print(type(result))

print("Name : ", result.name)
print("Age : ", result.age)
print("Course : ", result.course)