arr = input()
n = int(input())
for elem in arr[::-1]:
    if n == 0:
        break
    print(elem, end="")
    n -= 1