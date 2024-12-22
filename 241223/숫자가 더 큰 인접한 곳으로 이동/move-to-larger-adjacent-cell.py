n, r, c = map(int, input().split()) 
arr = [list(map(int, input().split())) for _ in range(n)]

r, c = r - 1, c - 1
direction = 0
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
ans = [arr[r][c]]
while direction < 4:
    for i in range(4):
        if not 0 <= r + dys[direction] < n and  0 <= c + dxs[direction] < n:
            direction += 1
        elif arr[r][c] >= arr[r + dys[direction]][c + dxs[direction]]:
            direction += 1
        else:
            r += dys[direction]
            c += dxs[direction]
            ans.append(arr[r][c])
            direction = 0
            break

for i in range(len(ans)):
    print(ans[i], end=' ')