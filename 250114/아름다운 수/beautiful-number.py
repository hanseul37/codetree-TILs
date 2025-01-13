def count_beautiful_numbers(current_length, n):
    if current_length == n:
        return 1

    cnt = 0
    for num in range(1, 5):
        if current_length + num <= n:
            cnt += count_beautiful_numbers(current_length + num, n)
    return cnt

n = int(input())
print(count_beautiful_numbers(0, n))
