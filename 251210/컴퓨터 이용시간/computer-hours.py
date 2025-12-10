import heapq

n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, i + 1, 1])
    arr.append([end, i + 1, -1])
arr.sort()

free_computer= list(range(n))
heapq.heapify(free_computer)

ans = [0] * n
computer = {}
for time, person, flag in arr:
    if flag == 1:
        idx = heapq.heappop(free_computer)
        ans[person - 1] = idx + 1
        computer[person] = idx
    else:
        idx = computer.pop(person)
        heapq.heappush(free_computer, idx)

print(*ans)
