n = int(input())
for i in range(0, n):
    for j in range(0, n):
        print(chr(ord('A') + i * n + j), end="")
    print()