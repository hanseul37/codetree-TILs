import sys
sys.set_int_max_str_digits(1000000)

n = int(input())
cnt = 0
for i in range(1, n + 1):
    num = str(i)
    if '3' in num or '6' in num or '9' in num or i % 3 == 0:
        cnt += 1
print(cnt)        
