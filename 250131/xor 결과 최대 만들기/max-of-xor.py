n, m = map(int, input().split())
arr = list(map(int, input().split()))
max_value = 0

def pick(idx, num):
    global max_value
    if len(num) == m:
        value = num[0]
        for i in range(1, m):
            value ^= num[i] 
        max_value = max(max_value, value)                          
    for i in range(idx + 1, n):
        num.append(arr[i])
        pick(i, num)
        num.pop()

pick(-1, [])
print(max_value)