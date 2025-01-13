def is_beautiful_number(num):
    s = str(num)
    cnt = 0
    while cnt < len(s):
        target = s[cnt]
        if not ('1' <= target <= '4'):
            return False
        if len(s) - cnt < int(target):
            return False
        for _ in range(int(target)):
            if s[cnt] != target:
                return False
            cnt += 1
    return True

n = int(input())
start = 10 ** (n - 1)
end = 10 ** n
beautiful_cnt = 0
for num in range(start, end):
    if is_beautiful_number(num):
        beautiful_cnt += 1

print(beautiful_cnt)
