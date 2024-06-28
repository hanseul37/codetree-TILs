arr = input().split()
word = arr[0]
q = int(arr[1])
for _ in range(q):
    n = int(input())
    if n == 1:
        word = word[1:] + word[0]
    elif n == 2:
        word = word[-1] + word[:-1]
    elif n == 3:
        word = word[::-1]
    print(word)