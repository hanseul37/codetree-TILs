class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

    def __lt__(self, other):
        return self.date < other.date

n = int(input())
datas = []
for _ in range(n):
    date, day, weather = input().split()
    datas.append(Data(date, day, weather))

datas.sort()

for i in range(n):
    if datas[i].weather == 'Rain':
        print(datas[i].date, datas[i].day, datas[i].weather)
        break