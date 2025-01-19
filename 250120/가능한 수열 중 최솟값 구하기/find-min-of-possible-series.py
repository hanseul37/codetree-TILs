n = int(input())
find = 0

def pattern(num):
    for i in range(1, len(num) // 2 + 1):
        for j in range(len(num) - i):
            arr1 = num[j:j + i]
            arr2 = num[j + i:j + 2 * i]
            if arr1 == arr2:
                return True
    return False

def simul(num):
    global find
    if find == 1:
        return

    if pattern(num):
        return
    if len(num) == n:
        for elem in num:
            print(elem, end='')
        find = 1
        return 
    for i in range(4, 7):
        num.append(i)
        simul(num)
        num.pop()

simul([])
