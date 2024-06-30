word = input()
cnt = 0
for elem in word:
    if elem.isdigit():
        cnt += int(elem)
print(cnt)