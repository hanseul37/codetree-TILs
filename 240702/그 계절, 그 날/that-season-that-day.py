def yoon(Y:int):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True
            return False
        else:
            return True
    else:
        return False
    
def check(Y:int, M:int, D:int):
    if yoon(Y) and M == 2:
        if D >= 1 and D <= 29:
            return M
        else:
            return -1
    else:
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
            if D >= 1 and D <= 31:
                return M
            else:
                return -1
        elif M == 4 or M == 6 or M == 9 or M == 11:
            if D >= 1 and D <= 30:
                return M
            else:
                return -1
        else:
            if D >= 1 and D <= 28:
                return M
            else:
                return -1

Y, M, D = list(map(int, input().split()))
ans = check(Y, M, D)
if ans >= 3 and ans <= 5:
    print('Spring')
elif ans >= 6 and ans <= 8:
    print('Summer')
elif ans >= 9 and ans <= 11:
    print('Fall')
else:
    print('Winter')