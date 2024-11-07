from collections import deque

class Queue:
    def __init__(self):       
        self.dq = deque()
                
    def push(self, item):      
        self.dq.append(item)

    def pop(self):              
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq.popleft()

    def size(self):       
        return len(self.dq)
                
    def empty(self):      
        if self.dq:
            return 0
        else:
            return 1     
                
    def front(self):           
        if self.empty():
            raise Exception("Queue is empty")       
        return self.dq[0]

q = Queue()             
n = int(input())
for i in range(n):
    command = list(input().split())
    if command[0] == 'push':
        q.push(command[1])
    elif command[0] == 'pop':
        print(q.pop())
    elif command[0] == 'size':
        print(q.size())
    elif command[0] == 'empty':
        print(q.empty())
    elif command[0] == 'front':
        print(q.front())