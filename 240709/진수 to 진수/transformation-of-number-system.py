a, b = list(map(int, input().split()))
n = input()
num = 0
arr = [int(bit) for bit in n]
for i in range(len(arr)):
    num = num * a + arr[i]

new_arr = []
while num >= b:
    new_arr.append(num % b)
    num //= b
if num != 0:
    new_arr.append(num)
 
for bit in new_arr[::-1]:
    print(bit, end='')