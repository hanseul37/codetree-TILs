n, m = list(map(int, input().split()))
a, b = [], []
a_point, b_point = 0, 0
for _ in range(n):
    v, t = list(map(int, input().split()))
    for i in range(t):
        a_point += v
        a.append(a_point)
    
for _ in range(m):
    v, t = list(map(int, input().split()))
    for i in range(t):
        b_point += v
        b.append(b_point)

lead = ''
cnt = 0
for i in range(len(a)):
    if a[i] > b[i]:
        now_lead = 'A'
    elif a[i] < b[i]:
        now_lead = 'B'
    else: 
        now_lead = lead
    
    if lead != now_lead:
        lead = now_lead
        cnt += 1

if cnt != 0:
    print(cnt - 1)
else:
    print(0)