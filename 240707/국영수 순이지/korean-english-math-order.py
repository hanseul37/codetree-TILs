class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

students = []
n = int(input())
for _ in range(n):
    name, kor, eng, math = input().split() 
    students.append(Student(name, int(kor), int(eng), int(math)))

students.sort(key=lambda x:(-x.kor, -x.eng, -x.math))
for i in range(n):
    print(students[i].name, students[i].kor, students[i].eng, students[i].math)