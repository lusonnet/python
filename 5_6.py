# -*- coding = utf-8 -*-
# @Time : 2021/5/6 22:20
# @Author : 卢佩诗
# @File : 5_6.py
# @Software: PyCharm
'''
namelist = ["校长","小李","小明"]
#查

finename = input("请输入：")

if finename in namelist:
    print("找到了")
else:
    print("没有")

a = ["a","b","c","a","b"]

print(a.index("a",1,4))


schoolname = [["北京大学","清华大学"],["aa","bb"],["cc","dd"]]
print(schoolname[0][0])

teachername =
'''
import random

office = [[],[],[]]
names = ["a","b","c","d","e","f","g","h"]
for name in names:
    index = random.randint(0,2)
    office[index].append(name)
for offices in office:
    print(offices)









import random
office = [[],[],[]]
name = ["a","b","c","d","e","f","g","h"]

for names in name:
    index = random.randint(0,2)
    office[index].append(name)

for offices in office:
    print(offices)