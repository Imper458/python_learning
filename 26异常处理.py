import traceback

try:
    f = open('test.txt')
    s = f.readline()
    num = int(s.strip())
    print(num)
except FileNotFoundError:
    print(traceback.format_exc())
    print('文件不存在')
except ValueError:
    print(traceback.format_exc())
    print('值不对，不能转换')
except Exception:
    print(traceback.format_exc())
else:
    print('没有异常，很高兴')
finally:
    if f:
        print('不管有没有异常都执行')
        f.close()

print('程序完成')