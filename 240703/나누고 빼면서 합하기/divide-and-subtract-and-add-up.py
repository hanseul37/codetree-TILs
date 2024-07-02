def cal(m, sum):
    sum += arr[m-1]
    if m % 2 == 0:
        m //= 2
    else:
        m -= 1
    return m, sum

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
sum = 0
while m > 0:
    m, sum = cal(m, sum)
print(sum)