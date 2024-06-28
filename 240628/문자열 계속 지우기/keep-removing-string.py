A = list(input())
B = list(input())
flag = 0
for _ in range(len(A)):
    for i in range(len(A)):
        if A[i] == B[0] and len(A) - i >= len(B):
            flag = 1
            for j in range(1, len(B)):
                if A[i+j] != B[j]:
                    flag = 0
            if flag == 1:
                for _ in range(len(B)):
                    A.pop(i)
                break
print(''.join(A))