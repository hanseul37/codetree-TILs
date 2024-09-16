A, B, x, y = map(int, input().split())
arr = []
arr.append(abs(A - B))
arr.append(abs(A - x) + abs(B - y))
arr.append(abs(A - y) + abs(B - x))
print(min(arr))