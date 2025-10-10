from functools import cmp_to_key

n = int(input())
arr = [input() for _ in range(n)]

def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1  
    
arr.sort(key=cmp_to_key(compare))
print(''.join(arr))
