arr2 = []
for i in range(2):
    arr = list(map(int, input().split()))
    arr2.append(arr)
for i in range(2):
    print(f'{sum(arr2[i])/4:.1f}', end=" ")
print()
for i in range(4):
    su = 0
    for j in range(2):
        su += arr2[j][i] 
    print(f'{su/2:.1f}', end=" ")
print()
su = 0
for i in range(2):
    su += sum(arr2[i])
print(f'{su/8:.1f}')