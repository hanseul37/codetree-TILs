arr = input().split()
a = ord(arr[0])
b = ord(arr[1])
print(a+b, end=" ")
if a > b:
    print(a - b)
else:
    print(b - a)