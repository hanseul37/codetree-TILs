arr = input().split()
a, b = int(arr[0]), int(arr[1])
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
cnt = 0
for i in range(a):
	success = True
	for j in range(b):
		if i + j >= a:
			success = False
			break
		if aa[i + j] != bb[j]:
			success = False
			break
	if success:
		print("Yes")
        cnt = 1
		break
if cnt == 0:
    print("No")