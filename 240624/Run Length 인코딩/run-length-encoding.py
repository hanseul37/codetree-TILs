A = list(input())
point = A[0]
cnt = 1
encoded = ""
for elem in A[1:]:
    if elem == point:
        cnt += 1
    else:
        encoded += point
        encoded += str(cnt)

        point = elem
        cnt = 1

encoded += point
encoded += str(cnt)

print(len(encoded))
print(encoded)