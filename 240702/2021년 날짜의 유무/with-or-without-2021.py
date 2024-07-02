def check(M:int, D:int):
    if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
        if D >= 1 and D <= 31:
            return True
        else:
            return False
    elif M == 2:
        if D >= 1 and D <= 28:
            return True
        else:
            return False
    elif M == 2 or M == 4 or M == 6 or M == 9 or M == 11:
        if D >= 1 and D <= 30:
            return True
        else:
            return False
    else:
        return False

M, D = list(map(int, input().split()))
if check(M, D):
    print('Yes')
else:
    print('No')