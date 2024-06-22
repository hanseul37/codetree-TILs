a = input()
b = input()
c = input()
if len(a) > len(b) and len(a) > len(c):
    if len(b) > len(c):
        print(len(a) - len(c))
    else:
        print(len(a) - len(b))
elif len(b) > len(a) and len(b) > len(c):
    if len(a) > len(c):
        print(len(b) - len(c))
    else:
        print(len(b) - len(a))
else:
    if len(a) > len(b):
        print(len(c) - len(b))
    else:
        print(len(c) - len(a))