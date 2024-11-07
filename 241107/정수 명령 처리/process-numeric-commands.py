class Stack:
    def __init__(self):     
        self.items = []
                
    def push(self, item):       
        self.items.append(item)

    def pop(self):          
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def size(self):       
        return len(self.items)
                
    def empty(self):   
        if self.items:
            return 0
        else:
            return 1
                
    def top(self):              
        if self.empty():
            raise Exception("Stack is empty")        
        return self.items[-1]

s = Stack()
n = int(input())
for i in range(n):
    command = list(input().split())
    if command[0] == 'push':
        s.push(command[1])
    elif command[0] == 'pop':
        print(s.pop())
    elif command[0] == 'size':
        print(s.size())
    elif command[0] == 'empty':
        print(s.empty())
    elif command[0] == 'top':
        print(s.top())