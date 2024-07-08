m1, d1, m2, d2 = list(map(int, input().split()))
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
A = input()

sum = 0
for i in range(m1, m2):
    sum += m[i - 1]

sum -= d1
sum += d2
sum += 1

print(sum // 7 + 1)