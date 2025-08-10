n = int(input())
words, dic = [], {}
for _ in range(n):
    word = input()
    word = ''.join(sorted(word))
    words.append(word)
cnt = 0
for i in range(n):
    if words[i] in dic:
        dic[words[i]] += 1
    else:
        dic[words[i]] = 1
    cnt = max(dic[words[i]], cnt)
print(cnt)    

