def swap(a:int, b:int):
    n, m = b, a
    return n, m

n, m = list(map(int, input().split()))
n, m = swap(n, m)
print(n, m)