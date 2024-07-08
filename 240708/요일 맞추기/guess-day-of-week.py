m1, d1, m2, d2 = list(map(int, input().split()))
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum = 0

if m1 < m2:
    for i in range(m1, m2):
        sum += m[i - 1]
    sum -= d1
    sum += d2
else:
    for i in range(m2, m1):
        sum += m[i - 1]
    sum -= d2
    sum += d1

if sum % 7 == 0:
    print('Mon')
elif sum % 7 == 1:
    print('Tue')
elif sum % 7 == 2:
    print('Wed')
elif sum % 7 == 3:
    print('Thu')
elif sum % 7 == 4:
    print('Fri')
elif sum % 7 == 5:
    print('Sat')
else:
    print('Sun')