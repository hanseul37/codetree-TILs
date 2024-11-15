n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

for i in range(s1, e1 + 1):
    del arr[s1 - 1]
for i in range(s2, e2 + 1):
    del arr[s2 - 1]

print(len(arr))
for i in range(len(arr)):
    print(arr[i])