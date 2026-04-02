'''
复杂列表

'''
students = [
    {'sno':10,'sname':'小张','sgrade':98},
    {'sno':14,'sname':'小a','sgrade':99},
    {'sno':12,'sname':'小b','sgrade':8},
]

result = sorted(students,key=lambda x:x['sno'])

print(f'source:{students},\nsort:{result}')
print(students[0]['sgrade'])