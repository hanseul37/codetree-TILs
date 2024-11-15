K, N = map(int, input().split())
arr = []
def choose(n):
    if len(arr) == N:
        for elem in arr:
            print(elem, end=' ')
        print()
        return

    for i in range(1, K + 1):
        arr.append(i)
        choose(n + 1)
        arr.pop()

choose(1) 