word = list(input())
while len(word) > 1:
    n = int(input())
    if n > len(word):
        word.pop(-1)
    else:
        word.pop(n)
    print(''.join(word))