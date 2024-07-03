n = int(input())
words = [
    input() for i in range(n)
]

words.sort()

for i in range(n):
    print(words[i])