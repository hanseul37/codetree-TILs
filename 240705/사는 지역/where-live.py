class User:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

    def __lt__(self, other):
        return self.name < other.name

n = int(input())
users = []
for _ in range(n):
    name, addr, city = input().split() 
    users.append(User(name, addr, city))

users.sort()
print('name ' + users[-1].name)
print('addr ' + users[-1].addr)
print('city ' + users[-1].city)