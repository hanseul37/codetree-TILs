n, k = map(int, input().split())
arr = list(map(int, input().split()))
numbers = {}
for i in range(n):
    if arr[i] in numbers:
        numbers[arr[i]] += 1
    else:
        numbers[arr[i]] = 1
numbers = sorted(numbers.keys(), key=lambda x:(-numbers[x], -x))
for i in range(k):
    print(numbers[i], end = ' ')
