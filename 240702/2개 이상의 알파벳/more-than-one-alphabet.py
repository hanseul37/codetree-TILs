def check(word):
    alphabet = word[0]
    for i in range(1, len(word)):
        if word[i] != alphabet:
            return True
    return False

word = input()
if check(word):
    print('Yes')
else:
    print('No')