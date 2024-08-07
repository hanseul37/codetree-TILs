n = int(input())
a_arr, b_arr = [], []
for _ in range(n):
    a, b = list(map(int, input().split()))
    a_arr.append(a)
    b_arr.append(b)

for i in range(1, 10001):
    flag = 0
    for j in range(n):
        if not (a_arr[j] <= i * (2 ** (j + 1)) <= b_arr[j]):
            flag = 1
            break
    if flag == 0:
        print(i)
        break