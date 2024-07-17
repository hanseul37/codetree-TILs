n = int(input())
arr = []
for _ in range(n):
    num = input()
    arr.append(num)


max_value = -1
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            carry = 0
            max_len = max(len(arr[i]), len(arr[j]), len(arr[k]))
            for l in range(max_len):
                arr[i] = arr[i].zfill(max_len)
                arr[j] = arr[j].zfill(max_len)
                arr[k] = arr[k].zfill(max_len)
                if int(arr[i][-(l + 1)]) + int(arr[j][-(l + 1)]) + int(arr[k][-(l + 1)]) >= 10:
                    carry = 1
            if carry == 0:
                sum = int(arr[i]) + int(arr[j]) + int(arr[k])
                if max_value < sum:
                    max_value = sum

print(max_value)