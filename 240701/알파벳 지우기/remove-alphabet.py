word1 = input()
word2 = input()
arr1 = []
arr2 = []

for elem in word1:
    if elem.isdigit():
        arr1.append(elem)
for elem in word2:
    if elem.isdigit():
        arr2.append(elem)

word1 = ''.join(arr1)
word2 = ''.join(arr2)
print(int(word1) + int(word2))