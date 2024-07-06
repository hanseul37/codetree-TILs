class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
people = []
for i in range(n):
    name, height, weight = input().split()
    people.append(Person(name, int(height), int(weight)))

people.sort(lambda x:x.height)

for i in range(n):
    print(people[i].name, people[i].height, people[i].weight)