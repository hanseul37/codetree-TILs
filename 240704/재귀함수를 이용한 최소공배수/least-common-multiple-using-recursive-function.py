def lcm(n: int):
    if n == 1:
        return arr[0]
    elif n == 2:
        sum = arr[0]
        while sum % arr[1] != 0:
            sum += arr[0]
        return sum
    else:
        sum = lcm(n - 1)
        while sum % arr[n - 1] != 0:
            sum += lcm(n - 1)
        return sum

n = int(input())
arr = list(map(int, input().split()))
print(lcm(n))