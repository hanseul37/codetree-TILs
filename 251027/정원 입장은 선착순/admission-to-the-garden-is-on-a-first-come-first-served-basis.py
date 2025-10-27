import heapq

n = int(input())
pq = []
for i in range(n):
    ai, ti = map(int, input().split())
    heapq.heappush(pq, (ai, i, ti))

ai, idx, ti = heapq.heappop(pq)
waiting = [(idx, ai, ti)]
time, max_waiting = ai, 0
while waiting:
    idx, ai, ti = heapq.heappop(waiting)
    max_waiting = max(time - ai, max_waiting)
    time += ti
    while pq:
        if pq[0][0] <= time:
            wait = heapq.heappop(pq)
            heapq.heappush(waiting, (wait[1], wait[0], wait[2]))
        else:
            break
print(max_waiting)