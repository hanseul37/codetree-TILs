class Number:
    def __init__(self, value, location):
        self.value = value
        self.location = location

numbers = []

n = int(input())
elements = list(map(int, input().split()))
for i in range(n):
    numbers.append(Number(elements[i], i))

numbers.sort(key=lambda x:(x.value, x.location))

locations = [0 for i in range(n)]
for index, number in enumerate(numbers):
    locations[number.location] = index + 1

for location in locations:
    print(location, end=" ")