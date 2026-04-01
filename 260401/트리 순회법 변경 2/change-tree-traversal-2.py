n = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))
postorder = []
pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i
        
def build(pre_s, pre_e, in_s, in_e):
    if pre_s > pre_e or in_s > in_e:
        return
    node = preorder[pre_s]
    node_idx = pos[node]
    left_len = node_idx - in_s
    build(pre_s + 1, pre_s + left_len, in_s, node_idx - 1)
    build(pre_s + 1 + left_len, pre_e, node_idx + 1, in_e)
    postorder.append(node)

build(0, n - 1, 0, n - 1)
print(*postorder)


