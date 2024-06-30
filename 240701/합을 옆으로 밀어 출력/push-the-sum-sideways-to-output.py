n = int(input())
sum = 0
for i in range(n):
    digit = int(input())
    sum += digit
sum = str(sum)
print(sum[1:] + sum[0])