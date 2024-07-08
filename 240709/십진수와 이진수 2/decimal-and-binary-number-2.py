N = input()
arr = [int(bit) for bit in N]
num = 0
for i in range(len(arr)):
    num = num * 2 + arr[i]

num *= 17

new_arr = []
while num >= 2:
    new_arr.append(num % 2)
    num //= 2

if num != 0:
    new_arr.append(num)

for bit in new_arr[::-1]:
    print(bit, end='')