import datetime

def get_diff_time(input_time, del_time):

    print(del_time)
    aim_time = input_time - del_time
    print(aim_time)


input_time = input("请输入日期，格式为:2001-11-11:")
input_time = datetime.datetime.strptime(input_time, "%Y-%m-%d")
get_diff_time(input_time, datetime.timedelta(days=7))
