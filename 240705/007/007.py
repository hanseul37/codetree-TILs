class Secret:
    def __init__(self, code, location, time):
        self.code = code
        self.location = location
        self.time = time

word = input().split()
obj = Secret(word[0], word[1], word[2])
print('secret code : ' + obj.code)
print('meeting point : ' + obj.location)
print('time : ' + obj.time)