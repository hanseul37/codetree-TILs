n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []
pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i

def build(in_s, in_e, post_s, post_e):
    if in_s > in_e or post_s > post_e:
        return
    node = postorder[post_e]
    node_idx = pos[node]
    left_len = node_idx - in_s
    preorder.append(node)
    build(in_s, node_idx - 1, post_s, post_s + left_len - 1)
    build(node_idx + 1, in_e, post_s + left_len, post_e - 1)

build(0, n - 1, 0, n - 1)
print(*preorder)


