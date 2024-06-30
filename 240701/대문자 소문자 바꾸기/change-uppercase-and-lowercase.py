word = input()
for elem in word:
    if ord(elem) > ord('A') and ord(elem) < ord('Z'):
        print(elem.lower(), end='')
    elif ord(elem) > ord('a') and ord(elem) < ord('z'):
        print(elem.upper(), end='')