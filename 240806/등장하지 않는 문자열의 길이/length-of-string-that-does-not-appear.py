n = int(input())
word = input()

max_length = 0
for i in range(1, n + 1):
    for j in range(n - i):
        flag = 1
        first = []
        for k in range(j, j + i):
            if not (ord(word[k]) + 1 == ord(word[k + 1])):
                flag = 0
                break
            first.append(word[k])
        if flag == 1:
            first_str = ''.join(first)
            second = word[j + i:]
            if first_str in second:
                max_length = i

print(max_length + 1)