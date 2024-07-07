class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = []
for _ in range(5):
    name, height, weight = input().split()
    people.append(Person(name, int(height), float(weight)))

people.sort(key=lambda x:x.name) 

print('name')
for person in people:
    print(person.name, person.height, f'{person.weight:.1f}')

print()

people.sort(key=lambda x:-x.height) 

print('height')
for person in people:
    print(person.name, person.height, f'{person.weight:.1f}')