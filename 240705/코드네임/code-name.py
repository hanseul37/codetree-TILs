class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = []
for _ in range(5):
    codename, score = input().split()
    agents.append(Agent(codename, score))


index = 0
for i in range(1, 5):
    if int(agents[index].score) > int(agents[i].score):
        index = i

print(agents[index].codename, agents[index].score)