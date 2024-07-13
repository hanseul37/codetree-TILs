class Shake:
    def __init__(self, t, x, y):
        self.t = t
        self.x =x
        self.y = y
    
N, K, P, T = list(map(int, input().split()))
timeline = []
infection = [0 for _ in range(N)]
infection[P - 1] = 1
count = [0 for _ in range(N)]
for _ in range(T):
    t, x, y = list(map(int, input().split()))
    timeline.append(Shake(t, x, y))

timeline.sort(key=lambda x:x.t)

for time in timeline:
    if infection[time.x - 1] != 0:
        if count[time.x - 1] < 2:
            infection[time.y - 1] = 1
            count[time.x - 1] += 1
    if infection[time.y - 1] != 0:
        if count[time.y - 1] < 2:
            infection[time.x - 1] = 1
            count[time.y - 1] += 1

for infect in infection:
    print(infect, end='')