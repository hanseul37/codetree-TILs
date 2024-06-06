arr = list(map(int, input().split()))
a = arr[0]
b = arr[1]
cnt = [0] * b
sum = 0
while a > 1:
    cnt[a % b] += 1
    a //= b
for i in range(b):
    sum += cnt[i] ** 2
print(sum)