# -*- coding = utf-8 -*-
# @Time : 2021/4/27 23:14
# @Author : 卢佩诗
# @File : demo2.py
# @Software: PyCharm
'''
print("hello")

a = 10
print(a)


age = 18
print("我的年龄是：%d 岁" %age)
print("www","baidu","com",sep=".")
print("hello",end="")
print("world",end="\t")
print("python",end="\n")#换行
print("end")
'''

'''
password = input("请输入密码")
print("您输入的密码是：",password)


#a = 10
a = "abc"
print(type(a))


a = int("123")
b = a + 100
print(b)


if 0:
    print("True")
else :
    print("False")

import random #引入随机库

x = random.randint(0,100)
print(x)


x = input("请输入：剪刀（0）")
import random
y = random.randint(0,2)
if x<y:
    print("哈哈，你输了：")

'''

for x in range(1,10):
    print("\t")
    for y in range(1,x+1):
        result = x * y
        print("%d*%d=%d"%(y,x,x*y),end="\t")



