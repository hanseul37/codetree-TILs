n, l = map(int, input().split()) 
arr1 = list(map(int, input().split()))
arr2 = [x + 1 for x in arr1]

def check(arr, h):
    cnt = 0
    for elem in arr:
        if elem >= h:
            cnt += 1
    return cnt

h = 0
for i in range(1, 101):
    if check(arr1, i) >= i:
        h = i
    elif check(arr2, i) >= i and check(arr2, i) - check(arr1, i) <= l:
        h = i
print(h)