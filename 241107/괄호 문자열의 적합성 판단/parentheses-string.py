word = input()
arr = []
flag = 0
for i in range(len(word)):
    if word[i] == '(':
        arr.append('(')
    else:
        if len(arr) == 0:
            flag = 1
            break
        else:
            arr.pop()

if flag or len(arr):
    print('No')
else:
    print('Yes')