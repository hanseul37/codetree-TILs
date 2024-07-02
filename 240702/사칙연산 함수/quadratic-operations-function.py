def plus(a, c):
    return a + c
def minus(a, c):
    return a - c
def mul(a, c):
    return a * c
def div(a, c):
    return a // c 

a, o, c = input().split()
a = int(a)
c = int(c)
if o == '+':
    print(f'{a} {o} {c} = {plus(a,c)}')
elif o == '-':
    print(f'{a} {o} {c} = {minus(a,c)}')
elif o == '*':
    print(f'{a} {o} {c} = {mul(a,c)}')
elif o == '/':
    print(f'{a} {o} {c} = {div(a,c)}')
else:
    print('False')