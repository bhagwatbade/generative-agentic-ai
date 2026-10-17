from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    course: str

s = Student(name = "Durga", age = 46, course = "Python")

print('-----------------------------------------------------------')

print(s)
print(s.name)
print(s.age)
print(s.course)

print('-----------------------------------------------------------')

d =  s.model_dump()
print(d)
print(type(d))
print(d["name"])

print('-----------------------------------------------------------')

json_string =  s.model_dump_json()
print(json_string)
print(type(json_string))

print('-----------------------------------------------------------')
