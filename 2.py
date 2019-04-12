# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:25:56 2019

@author: Administrator
"""
for i in range(1,10):
    s=" "
    for j in range(1,10):
        s+=str.format("{0:1}*{1:1}={2:<2} ",i,j,i*j)
    print(s)

print('上三角输出')
a = 1
while a <=9:    #外层循环控制行数
    b = 1
    while b <= a:   #内层循环控制列数
        print("%d*%d=%d\t" % (a, b, a*b), end="")
        b = b + 1
    print()     # 换行
    a = a + 1
    
print('下三角输出')
for i in range(1,10):
    for k in range(1,i):
        print(end="       ")
    for j in range(i,10):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print("")
    

