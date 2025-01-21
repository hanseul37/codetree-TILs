n, m = map(int, input().split())
arr = []
 
def pick(idx, num):
    if num == m:
        for elem in arr:
            print(elem, end=' ')
        print()

    for i in range(idx + 1, n + 1):
        arr.append(i)
        pick(i, num + 1)
        arr.pop() 

pick(0, 0)
