def find(n: int):
    if n == 1:
        return arr[0]
    return max(find(n - 1), arr[n - 1])

n = int(input())
arr = list(map(int, input().split()))
print(find(n))