a, b = input().split()
a_arr = []
b_arr = []
for elem in a:
    if elem.isdigit():
        a_arr.append(elem)
    else:
        break

for elem in b:
    if elem.isdigit():
        b_arr.append(elem)
    else:
        break

a = ''.join(a_arr)
b = ''.join(b_arr)
print(int(a) + int(b))