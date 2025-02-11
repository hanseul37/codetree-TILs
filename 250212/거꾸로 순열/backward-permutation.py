n = int(input())
visited = [False] * n
answer = []

def choose(cnt):
    if cnt >= n:
        for elem in answer:
            print(elem, end=' ')
        print()

    for i in range(n, 0, -1):
        if visited[i - 1] == False:
            answer.append(i)
            visited[i - 1] = True
            choose(cnt + 1)
            answer.pop()
            visited[i - 1] = False

choose(0)

 