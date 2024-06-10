n = int(input())
arr = list(map(int, input().split()))
cnt = n
while True:
    if cnt == 0:
        break
    for i in range(cnt):
        if arr[i] == max(arr[:cnt]):
            cnt = i
            print(i+1, end =" ")
            break