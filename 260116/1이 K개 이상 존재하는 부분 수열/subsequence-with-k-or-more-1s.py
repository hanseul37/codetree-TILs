import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
cnt1 = 0
answer = N + 1

for right in range(N):
    if arr[right] == 1:
        cnt1 += 1

    while cnt1 >= K:
        answer = min(answer, right - left + 1)
        if arr[left] == 1:
            cnt1 -= 1
        left += 1

print(answer if answer != N + 1 else -1)
