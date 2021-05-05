# -*- coding = utf-8 -*-
# @Time : 2021/5/5 22:16
# @Author : 卢佩诗
# @File : 5_5.py
# @Software: PyCharm

'''
str = "cenxi"
print((str+"\t")*3)
'''

#namelist = [] #定义一个空的列表
namelist = ["校长","小李","小明"]

#print(namelist[1])
'''
for name in namelist:
    print(name)

print(len(namelist))  #获取长度




length = len(namelist)
i = 0
while i<length:
    print(namelist[i])
    i += 1


#增  【append】
nametemp = input("请输入名字：")
namelist.append(nametemp)  #追加元素

for name in namelist:
    print(name)


a = [1,2]
b = [3,4]
a.append(b)
print(a)

a.extend(b)
print(a)
'''

moviename = ["aa","bb","cc","dd"]


for name in moviename:
    print(name)

#moviename.pop()
#del moviename[2]
#moviename.remove("bb")
moviename[1] = "ee"

print(moviename)