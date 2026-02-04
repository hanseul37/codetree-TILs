import heapq

a, b, n = map(int, input().split())
fare, line = [], []
for _ in range(n):
    charge, _ = map(int, input().split())
    route = list(map(int, input().split()))
    route = [x - 1 for x in route]
    fare.append(charge)
    line.append(route)
a -= 1
b -= 1

graph = [[] for _ in range(1000)]
for i in range(n):
    route = line[i]
    for j in range(len(route) - 1):
        graph[route[j]].append([route[j + 1], i])

cost = [dict() for _ in range(1000)]
cost[a][-1] = [0, 0]
q = [[0, 0, a, -1]] 
while q:
    bill, time, now, bus = heapq.heappop(q)
    if cost[now].get(bus, [float('inf'), float('inf')]) < [bill, time]:
        continue
    
    for next_station, next_bus in graph[now]:
        if bus == next_bus:
            ncost = bill
        else:
            ncost = bill + fare[next_bus]
        
        if cost[next_station].get(next_bus, [float('inf'), float('inf')]) > [ncost, time + 1]:
            cost[next_station][next_bus] = [ncost, time + 1]
            heapq.heappush(q, [ncost, time + 1, next_station, next_bus])

ans = min(cost[b].values(), default=[float('inf'), float('inf')])
if ans[0] == float('inf'):
    print(-1, -1)
else:
    print(ans[0], ans[1])