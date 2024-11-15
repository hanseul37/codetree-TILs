n = int(input())
arr = []
count = 0

def check(array):
    point = 0
    while point < len(array):
        cnt = 1
        while point + cnt < len(array) and array[point] == array[point + cnt]:
            cnt += 1
        if array[point] != cnt:
            return False
        point += cnt
    return True
        
def choose(num):
    global count
    if num == n: 
        if check(arr):
            count += 1
        return
        
    for i in range(1, 5):
        arr.append(i)
        choose(num + 1)
        arr.pop()

choose(1)
print(count)
