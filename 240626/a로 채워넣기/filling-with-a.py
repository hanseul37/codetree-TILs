word = input()
arr = list(word)
arr[1] = 'a'
arr[-2] = 'a'
word = ''.join(arr)
print(word)