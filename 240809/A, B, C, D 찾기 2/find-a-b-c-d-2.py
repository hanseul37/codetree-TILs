arr = list(map(int, input().split()))
arr.sort()
flag = 0
for i in range(12):
    for j in range(i + 1, 13):
        for k in range(j + 1, 14):
            for l in range(k + 1, 15):
                if flag == 0:
                    temp = []
                    a = arr[i]
                    b = arr[j]
                    c = arr[k]
                    d = arr[l]
                    temp.append(a)
                    temp.append(b)
                    temp.append(c)
                    temp.append(d)
                    temp.append(a + b)
                    temp.append(b + c)
                    temp.append(c + d)
                    temp.append(d + a)
                    temp.append(a + c)
                    temp.append(b + d)
                    temp.append(a + b + c)
                    temp.append(a + b + d)
                    temp.append(a + c + d)
                    temp.append(b + c + d)
                    temp.append(a + b + c + d)
                    temp.sort()
                    if temp == arr:
                        print(a, b, c, d)
                        flag = 1