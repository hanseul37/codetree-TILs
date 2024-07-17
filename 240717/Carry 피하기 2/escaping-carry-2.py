import sys

n = int(input())
arr = []
for _ in range(n):
    num = input()
    arr.append(num)


max = -sys.maxsize
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            carry = 0
            for l in range(min(len(arr[i]), len(arr[j]), len(arr[k]))):
                if int(arr[i][-(l + 1)]) + int(arr[j][-(l + 1)]) + int(arr[k][-(l + 1)]) >= 10:
                    carry = 1
            if carry == 0:
                sum = int(arr[i]) + int(arr[j]) + int(arr[k])
                if max < sum:
                    max = sum
print(max)