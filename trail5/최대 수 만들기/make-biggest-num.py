n = int(input())
arr = [input() for _ in range(n)]
arr.sort(key=lambda x:x * 9, reverse=True)
print(''.join(arr))