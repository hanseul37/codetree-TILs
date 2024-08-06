n = int(input())
word = input()

max_length = 0
for i in range(1, n + 1):
    for j in range(n - i):
        first = []
        for k in range(j, j + i):
            first.append(word[k])
        first_str = ''.join(first)
        second = word[j + i:]
        if first_str in second:
            max_length = i
            break

print(max_length + 1)