from sortedcontainers import SortedSet
n, q = map(int, input().split())
points = list(map(int, input().split()))
nums = dict()
for i in range(n):
    nums[points[i]] = i 

for _ in range(q):
    a, b = map(int, input().split())
    print(nums[b] - nums[a] + 1)