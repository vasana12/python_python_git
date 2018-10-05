import datetime

#컴퓨터의 현재시간 가져오기

now_date1 = datetime.datetime.now()
print(now_date1)

#임의의 시간 dataetime로 만들기

date= datetime.datetime(2017, 12, 16, 12, 18, 30, 900000) # 2017-12-16 12:18:30.900000
print(date)

#년, 월, 일, 시간, 분, 초, 마이크로초 가져오기
print(now_date1.year, now_date1.month, now_date1.day, now_date1.hour, now_date1.minute, now_date1.second, now_date1.microsecond)
print(date.year, date.month, date.day, date.hour, date.minute, date.second, date.microsecond)

#요일을 숫자로 가져오기
print(now_date1.weekday()) #{0: 월 ~ 6:일}
print(date.weekday())      #{0: 월 ~ 6:일}

#datetime 객체를 문자열로 변경

print(now_date1.strftime('%y %m %d %H %S %A %B'))
print(now_date1.strftime('%Y %m %d %H %S %A %B'))
print(date.strftime('%y %m %d %H %S %A %B'))
print(date.strftime('%Y %m %d %H %S %A %B'))
print(datetime.datetime.strptime("2017-01-02 14:44", "%Y-%m-%d %H:%M"))

# 몇일 차이인지 계산
dt1=datetime.datetime(2016, 2, 19,4)
dt2=datetime.datetime(2016, 1, 2, 13)
td = dt1 -dt2
print(td)

# 30일, 3600초 이후 시간 계산
t0=datetime.datetime(2017, 1, 1, 13)
d = datetime.timedelta(days=30, seconds=3600)

ti =t0+d
print(ti)