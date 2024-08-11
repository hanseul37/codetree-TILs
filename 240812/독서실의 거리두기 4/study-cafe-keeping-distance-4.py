n = int(input())
seats = list(input())
max_dist = 0

def nearest_dist(seats):
    dist = n
    last_person = -1
    for i in range(len(seats)):
        if seats[i] == '1':
            if last_person != -1:
                dist = min(dist, i - last_person)
            last_person = i
    return dist

for i in range(n - 1):
    for j in range(i + 1, n):
        copy_seats = seats.copy()
        if copy_seats[i] == '1' or copy_seats[j] == '1':
            continue
        copy_seats[i] = '1'
        copy_seats[j] = '1'
        dist = nearest_dist(copy_seats)
        max_dist = max(max_dist, dist)
print(max_dist)