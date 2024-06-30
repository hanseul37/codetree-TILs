word = input()
for elem in word:
    if elem.isalpha():
        print(elem.lower(), end='')
    elif elem.isdigit():
        print(elem, end='')