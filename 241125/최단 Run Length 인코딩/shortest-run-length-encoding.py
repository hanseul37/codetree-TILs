A = input()

run_length = len(A) * 2
for i in range(1, len(A) + 1):
    copy_A = list(A)
    for j in range(i):
        temp = copy_A[-1]
        for k in range(len(A) - 1, 0, -1):
            copy_A[k] = copy_A[k - 1]
        copy_A[0] = temp
    
    point = copy_A[0]
    cnt, length = 1, ''
    for j in range(1, len(copy_A)):
        if point != copy_A[j]:
            length += point
            length += str(cnt)
            cnt = 1
            point = copy_A[j]
        else:
            cnt += 1
    if cnt != 0:
        length += point
        length += str(cnt)
    run_length = min(run_length, len(length))

print(run_length)
