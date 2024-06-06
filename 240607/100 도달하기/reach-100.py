n = int(input())
a = 1
b = n
while True:
    print(a, end=" ")
    if a > 100:
        break
    temp = a
    a = b
    b += temp