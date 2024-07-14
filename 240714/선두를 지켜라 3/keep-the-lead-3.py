N, M = list(map(int, input().split()))
A, B = [], []
a_point, b_point = 0, 0
for _ in range(N):
    v, t = list(map(int, input().split()))
    for _ in range(t):
        a_point += v
        A.append(a_point)

for _ in range(M):
    v, t = list(map(int, input().split()))
    for _ in range(t):
        b_point += v
        B.append(b_point)

lead = ''
cnt = 0
for i in range(len(A)):
    if lead == 'A':
        if A[i] < B[i]:
            lead = 'B'
            cnt += 1
        elif A[i] == B[i]:
            lead = 'AB'
            cnt += 1
    elif lead == 'B':
        if B[i] < A[i]:
            lead = 'A'
            cnt += 1
        elif A[i] == B[i]:
            lead = 'AB'
            cnt += 1
    else:
        if A[i] > B[i]:
            lead = 'A'
            cnt += 1
        elif A[i] < B[i]:
            lead = 'B'
            cnt += 1

print(cnt)