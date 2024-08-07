n = int(input())
seats = input()
min_dist = 0
for i in range(n):
    if seats[i] == '0':
        copy_seats = list(seats)
        copy_seats[i] = '1'
        dist = n
        cnt = 0
        for j in range(1, n):
            if copy_seats[j] == '0':
                cnt += 1
            else:
                dist = min(dist, cnt)
                cnt = 0
            if j + 1 == n:
                dist = min(dist, cnt)
        min_dist = max(min_dist, dist)
print(min_dist + 1)