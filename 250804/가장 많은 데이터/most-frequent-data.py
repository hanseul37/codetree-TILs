n = int(input())
data = {}
max_cnt = 0
for _ in range(n):
    word = input()
    if word in data:
        data[word] += 1
    else:
        data[word] = 1
    max_cnt = max(data[word], max_cnt)
    
print(max_cnt)