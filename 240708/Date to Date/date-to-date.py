m1, d1, m2, d2 = list(map(int, input().split()))
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum = 0 
for i in range(m1, m2+1):
    sum += m[i - 1]

sum -= d1
sum -= (m[i - 1] - d2)

print(sum + 1)