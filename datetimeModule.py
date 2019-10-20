import datetime

print(datetime.datetime.today())
now = datetime.datetime.today()
other = datetime.datetime(1995,3,12,22,10)
print(now - other)
print(datetime.timedelta(18901,55597,42100)) #days, time and milliseconds
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.timezone)