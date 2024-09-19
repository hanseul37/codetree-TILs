n = int(input())
arr = [0, 0]
point = ''
cnt = 0
for i in range(n):
    c, s = input().split()
    if c == 'A':
        arr[0] += int(s)
    else: 
        arr[1] += int(s)
        
    if arr[0] == arr[1] and point != 'AB':
        cnt += 1
        point = 'AB'
    elif arr[0] > arr[1] and point != 'A':
        cnt += 1
        point = 'A'
    elif arr[0] < arr[1] and point != 'B':
        cnt += 1
        point = 'B'
print(cnt)