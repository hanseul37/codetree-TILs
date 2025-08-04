n, m = map(int, input().split())
words, digits = {}, {}
for i in range(n):
    word = input()
    words[word] = i
    digits[i] = word

for i in range(m):
    word = input()
    if word.isdigit():
        print(digits[int(word) - 1])
    else:
        print(words[word] + 1)


