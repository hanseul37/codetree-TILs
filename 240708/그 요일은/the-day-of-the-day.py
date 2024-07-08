m1, d1, m2, d2 = list(map(int, input().split()))
m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
A = input()

sum = 0
for i in range(m1, m2):
    sum += m[i - 1]

sum -= d1
sum += d2

count = 0
for i in range(1, sum + 1):
    if A == day[i % 7]:
        count += 1

print(count)