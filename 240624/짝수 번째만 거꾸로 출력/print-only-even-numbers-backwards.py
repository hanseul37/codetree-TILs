arr = list(input())
for i in range(len(arr) - 1, -1, -1):
    if i % 2 == 1:
        print(arr[i], end="")