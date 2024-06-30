word = input()
for elem in word:
    if elem.isalpha():
        print(elem.upper(), end="")