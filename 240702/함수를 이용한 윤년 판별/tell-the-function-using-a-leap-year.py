def yoon(y:int):
    if y % 4 != 0:
        return False
    elif y % 100 == 0 and y % 400 != 0:
        return False
    return True

y = int(input())
if yoon(y):
    print('true')
else:
    print('false')