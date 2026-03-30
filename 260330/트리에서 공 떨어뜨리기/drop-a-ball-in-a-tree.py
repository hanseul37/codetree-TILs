n = int(input())
tree = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    tree[i] = list(map(int, input().split()))
k = int(input())
node = 1
while True:
    left, right = tree[node]
    if left == -1 and right == -1:
        break
    elif left != -1 and right != -1:
        if k % 2 == 1:
            node = left
            k = k // 2 + 1
        else:
            node = right 
            k //= 2
    elif left == -1:
        node = right
    else:
        node = left
print(node)
