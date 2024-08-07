n = int(input())
seats = input()
min_dist = n
for i in range(n):
    if seats[i] == '0':
        copy_seats = list(seats)
        copy_seats[i] = '1'
        dist = 0
        cnt = 0
        for j in range(n):
            if copy_seats[j] == '0':
                cnt += 1
            else:
                dist = max(dist, cnt)
                cnt = 0
            if j + 1 == n:
                dist = max(dist, cnt)
        min_dist = min(min_dist, dist)
print(min_dist - 1)