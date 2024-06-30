n, A = input().split()
cnt = 0
for _ in range(int(n)):
    word = input()
    if A == word:
        cnt += 1
print(cnt)