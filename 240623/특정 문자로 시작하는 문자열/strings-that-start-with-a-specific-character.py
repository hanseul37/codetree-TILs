n = int(input())
arr = [
    input()
    for _ in range(n)
]
cha = input()
cnt = 0
sum = 0
for i in range(n):
    if arr[i][0] == cha:
        cnt += 1
        sum += len(arr[i])
print(f'{cnt} {sum/cnt:.2f}')