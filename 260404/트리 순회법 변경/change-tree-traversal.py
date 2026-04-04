import sys
sys.setrecursionlimit(10**6)

n = int(input())
preorder = list(int(input()) for _ in range(n))

def postorder(pre_s, pre_e):
    if pre_s > pre_e:
        return
    node = preorder[pre_s]
    node_idx = pre_s + 1
    while node_idx <= pre_e and node > preorder[node_idx]:
        node_idx += 1
    postorder(pre_s + 1, node_idx - 1)
    postorder(node_idx, pre_e)
    print(node)

postorder(0, n - 1)

