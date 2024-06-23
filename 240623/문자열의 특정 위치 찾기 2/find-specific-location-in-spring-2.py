cha = input()
arr = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0
for i in range(5):
    if arr[i][2] == cha or arr[i][3] == cha:
        cnt += 1
        print(arr[i])
print(cnt)