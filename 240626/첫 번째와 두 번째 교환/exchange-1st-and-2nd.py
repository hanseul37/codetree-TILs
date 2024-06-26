word = input()
arr = list(word)
first = arr[0]
second = arr[1]
for i in range(len(arr)):
    if arr[i] == first:
        arr[i] = second
    elif arr[i] == second:
        arr[i] = first
new_word = ''.join(arr)
print(new_word)