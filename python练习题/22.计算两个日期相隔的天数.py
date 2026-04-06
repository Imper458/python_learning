import datetime
# birthday = datetime.date(2001, 11, 22,)

birthday = "2001-11-22"
birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d")
print(birthday, type(birthday))

cur_time = datetime.datetime.now()

delta_time = cur_time - birthday
print(delta_time.days/365)
