n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

def win(a, b):
    if (a == '보' and b == '바위') or (a == '바위' and b == '가위') or (a == '가위' and b == '보'):
        return 1
    else:
        return 0

cases = [
    ['가위', '바위', '보'],
    ['가위', '보', '바위'],
    ['바위', '가위', '보'],
    ['바위', '보', '가위'],
    ['보', '가위', '바위'],
    ['보', '바위', '가위']
]    
max_win = 0
for case in cases:
    cnt = 0
    for a, b in arr:
        cnt += win(case[a - 1], case[b - 1])
    max_win = max(max_win, cnt)
print(max_win)