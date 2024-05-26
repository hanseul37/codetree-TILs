n = int(input())
ans = False
for i in range(2, n):
    if n % i == 0:
        ans = True
        break
if ans == True:
    print('C')
else:
    print('N')