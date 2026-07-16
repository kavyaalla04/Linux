from typing import TypedDict

class Student(TypedDict):
    id: int
    name: str
    age: int

student1 = Student(id= 1, name= "John Doe", age= 20)
student2 = Student(id= 2, name= "Jane Smith", age= 22)

print(student1)
print(student2)
