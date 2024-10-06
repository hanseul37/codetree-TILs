x1, y1, x2, y2 = list(map(int, input().split()))
a1, b1, a2, b2 = list(map(int, input().split()))
line = max(max(x2, a2) - min(x1, a1), max(y2, b2) - min(y1, b1))
print(line * line)