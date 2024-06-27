q = input().split()
word = q[0]
for i in range(int(q[1])):
    arr = input().split()
    word_list = list(word)
    if arr[0] == '1':
        a = word_list[int(arr[1]) - 1]
        b = word_list[int(arr[2]) - 1]
        word_list[int(arr[1]) - 1] = b
        word_list[int(arr[2]) - 1] = a
        word = ''.join(word_list)
        print(word)
    elif arr[0] == '2':
        for i in range(len(word_list)):
            if word_list[i] == arr[1]:
                word_list[i] = arr[2]
        word = ''.join(word_list)
        print(word)