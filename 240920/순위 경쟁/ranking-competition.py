n = int(input())
arr = [0, 0, 0]
winner = 'ABC'
cnt = 0
for i in range(n):
    c, s = input().split()
    if c == 'A':
        arr[0] += int(s)
    elif c == 'B':
        arr[1] += int(s)
    elif c == 'C':
        arr[2] += int(s)
    
    new_winner = ''
    if arr[0] == max(arr):
        new_winner += 'A'
    if arr[1] == max(arr):
        new_winner += 'B'
    if arr[2] == max(arr):
        new_winner += 'C'
    
    if new_winner != winner:
        cnt += 1
        winner = new_winner
print(cnt)