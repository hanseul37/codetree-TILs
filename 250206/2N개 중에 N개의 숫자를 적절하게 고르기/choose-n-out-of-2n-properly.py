n = int(input())
a = list(map(int, input().split()))

min_diff = sum(a)

def track(a1, a2, idx):
    global min_diff
    
    if len(a1) + len(a2) >= len(a):
        min_diff = min(min_diff, abs(sum(a1) - sum(a2)))

    if len(a1) != len(a) / 2:
        a1.append(a[idx])
        track(a1, a2, idx + 1)
        a1.pop()
    
    if len(a2) != len(a) / 2:
        a2.append(a[idx])
        track(a1, a2, idx + 1)
        a2.pop()

track([], [], 0)
print(min_diff)
