class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

words = input().split()
obj = Bomb(words[0], words[1], words[2])
print('code : ' + obj.code)
print('color : ' + obj.color)
print('second : ' + obj.second)