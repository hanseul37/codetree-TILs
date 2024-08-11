n = int(input())
arr = list(map(int, input().split()))

for i in range(1, 1000):
    number = []
    number.append(i)
    flag = 0
    while len(number) < n:
        if arr[len(number) - 1] - number[-1] < 1 or arr[len(number) - 1] - number[-1] in number:
            flag = 1
            break
        number.append(arr[len(number) - 1] - number[-1])
    if flag == 0:
        for j in range(len(number)):
            print(number[j], end=' ')
        break