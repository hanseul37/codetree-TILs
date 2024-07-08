n = int(input())
arr = []
while n >= 2:
    arr.append(n % 2)
    n //= 2
arr.append(n)

for num in arr[::-1]:
    print(num, end='')