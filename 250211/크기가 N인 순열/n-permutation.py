n = int(input())
visiited = [False] * n
answer = []

def choose(cnt):
    if cnt >= n:
        for elem in answer:
            print(elem, end=' ')
        print()
        return

    for i in range(1, n + 1):
        if visiited[i - 1] == False:
            answer.append(i)
            visiited[i - 1] = True
            choose(cnt + 1)
            answer.pop()
            visiited[i - 1] = False


choose(0)