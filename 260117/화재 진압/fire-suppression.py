n, m = map(int, input().split())
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))
max_time, station = 0, 0
for fire in fires:
    while station < m - 1 and abs(stations[station] - fire) > abs(stations[station + 1] - fire):
        station += 1
    max_time = max(abs(stations[station] - fire), max_time)
print(max_time)