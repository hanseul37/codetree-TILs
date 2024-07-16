n = input().strip()
max_value = 0

for i in range(len(n)):
    temp = list(n)
    
    if temp[i] == '0':
        temp[i] = '1'
    else:
        temp[i] = '0'
    
    c_sum = 0
    for j in range(len(temp)):
        c_sum += int(temp[j]) * (2 ** (len(temp) - 1 - j)) 

    if max_value < c_sum:
        max_value = c_sum

print(max_value)