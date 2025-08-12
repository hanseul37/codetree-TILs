word = input()
dic = {}
ans = 'None'
for elem in word:
    if elem in dic:
        dic[elem] += 1
    else:
        dic[elem] = 1

for elem in word:
    if dic[elem] == 1:
        ans = elem
        break
print(ans)