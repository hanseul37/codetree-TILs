ans = False
for _ in range(5):
    n = int(input())
    if n % 3 != 0:
        ans = True
if ans == True:
    print(0)
else:
    print(1)