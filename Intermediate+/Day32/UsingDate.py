import datetime as dt


today=dt.datetime.today()
month=today.month
year=today.year
weekday=today.weekday()
print(weekday)


birthday=dt.datetime(year=2004,month=5,day=16)
print(birthday)