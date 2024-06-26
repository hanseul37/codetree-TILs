words = input().split()
word1 = list(words[0])
word2 = list(words[1])
word2[0] = word1[0]
word2[1] = word1[1]
word = "".join(word2)
print(word)