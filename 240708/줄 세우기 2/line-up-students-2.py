class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

students = []
n = int(input())
for i in range(n):
    height, weight = list(map(int, input().split()))
    students.append(Student(height, weight, i + 1))

students.sort(key=lambda x:(x.height, -x.weight))

for student in students:
    print(student.height, student.weight, student.number)