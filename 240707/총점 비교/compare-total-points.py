class Student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
students = []
n = int(input())
for _ in range(n):
    name, sub1, sub2, sub3 = input().split()
    students.append(Student(name, sub1, sub2, sub3))

students.sort(key=lambda x:int(x.sub1) + int(x.sub2) + int(x.sub3))

for i in range(n):
    print(students[i].name, students[i].sub1, students[i].sub2, students[i].sub3)