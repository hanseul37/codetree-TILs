n = int(input())
cups = []
for _ in range(n):
    cup = list(map(int, input().split()))
    cups.append(cup)

max_cnt = 0
for i in range(3):
    location = [0] * 3
    location[i] = 1
    cnt = 0
    for j in range(n):
        temp = location[cups[j][0] - 1]
        location[cups[j][0] - 1] = location[cups[j][1] - 1]
        location[cups[j][1] - 1] = temp
        if location[cups[j][2] - 1] == 1:
            cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)