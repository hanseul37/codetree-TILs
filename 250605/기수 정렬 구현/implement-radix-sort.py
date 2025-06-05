n = int(input())
arr = list(map(int, input().split()))

def radix_sort(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)

        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        exp *= 10
    return arr
sorted_arr = radix_sort(arr)
print(*sorted_arr)
