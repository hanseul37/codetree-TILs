n = int(input())
arr = ['0'] * 101
for _ in range(n):
    location, alpha = input().split()
    arr[int(location)] = alpha

G_max = 0
for start in range(101):
    for end in range(start, 101):
        if arr[start] == 'G' and arr[end] == 'G':
            flag = 0
            for i in range(start + 1, end):
                if arr[i] == 'H':
                    flag = 1
                    break
            if flag == 0:
                G_max = max(G_max, end - start)

H_max = 0
for start in range(101):
    for end in range(start, 101):
        if arr[start] == 'H' and arr[end] == 'H':
            flag = 0
            for i in range(start + 1, end):
                if arr[i] == 'G':
                    flag = 1
                    break
            if flag == 0:
                H_max = max(H_max, end - start)

GH_max = 0
for start in range(101):
    for end in range(start, 101):
        if arr[start] != '0' and arr[end] != '0':
            g_count, h_count = 0, 0
            for i in range(start, end + 1):
                if arr[i] == 'G':
                    g_count += 1
                elif arr[i] == 'H':
                    h_count += 1
            if g_count == h_count and g_count != 0:
                GH_max = max(GH_max, end - start)

print(max(G_max, H_max, GH_max))