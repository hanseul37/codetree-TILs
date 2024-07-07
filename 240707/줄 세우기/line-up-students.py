class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

students = []
n = int(input())
for i in range(n):
    height, weight = input().split()
    students.append(Student(int(height), int(weight), i + 1))

students.sort(key=lambda x:(-x.height, -x.weight, x.number))

for student in students:
    print(student.height, student.weight, student.number)