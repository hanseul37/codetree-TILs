n, k, T = input().split()
arr1 = [input() for i in range(int(n))]
arr2 = []
for elem in arr1:
    if elem.startswith(T):
        arr2.append(elem)
arr2.sort()
print(arr2[int(k) - 1])