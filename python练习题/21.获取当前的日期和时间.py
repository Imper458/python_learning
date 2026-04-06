import datetime
now = datetime.datetime.now()
print(now, type(now))

str_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(str_time, type(str_time))

print("year", now.year)
print("month", now.month)
print("day", now.day)
print("hour", now.hour)
print("minute", now.minute)
print("second", now.second)


