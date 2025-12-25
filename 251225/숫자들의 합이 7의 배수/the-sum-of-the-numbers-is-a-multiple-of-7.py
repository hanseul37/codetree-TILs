n = int(input())
first = [-1] * 7
first[0] = 0
prefix, max_len = 0, 0
for i in range(1, n + 1):
    prefix = (int(input()) + prefix) % 7
    if first[prefix] == -1:
        first[prefix] = i
    else:
        max_len = max(i - first[prefix], max_len)
print(max_len)