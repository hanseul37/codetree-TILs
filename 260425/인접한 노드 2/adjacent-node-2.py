n = int(input())
values = list(map(int, input().split()))
tree, dp, choice = [[] for _ in range(n)], [[0, 0] for _ in range(n)], []
for _ in range(n - 1): 
    v1, v2 = map(int, input().split()) 
    tree[v1 - 1].append(v2 - 1) 
    tree[v2 - 1].append(v1 - 1)

def dfs(node, parent):
    dp[node] = [0, values[node]] 
    for next_node in tree[node]: 
        if next_node != parent: 
            dfs(next_node, node) 
            dp[node][0] += max(dp[next_node][0], dp[next_node][1])
            dp[node][1] += dp[next_node][0]
        
def find_path(node, parent, flag):
    if not flag and dp[node][1] > dp[node][0]:
        choice.append(node + 1)
        flag = True
    else:
        flag = False
    for next_node in tree[node]:
        if next_node != parent:
            find_path(next_node, node, flag)

dfs(0, -1)
find_path(0, -1, False)
choice.sort()
print(max(dp[0][0], dp[0][1]))
print(*choice)