k = int(input())
tree = [[] for _ in range(k)]
arr = list(map(int, input().split()))

def build(t, depth):
    if not t:
        return
    mid = len(t) // 2
    tree[depth].append(t[mid])
    build(t[:mid], depth + 1)
    build(t[mid + 1:], depth + 1)

build(arr, 0)
for i in range(k):
    print(*tree[i])