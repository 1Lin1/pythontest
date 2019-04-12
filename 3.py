# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:32:38 2019

@author: Administrator
"""

import math
a=float(input("请输入三角形边长a:"))
b=float(input("请输入三角形边长b:"))
c=float(input("请输入三角形边长c:"))
h=(a+b+c)/2
area=math.sqrt(h*(h-a)*(h-b)*(h-c))
long=a+b+c
if (a+b>c and b+c>a and a+c>b):
    print (str.format("三边分别为: a={0},b={1},c={2}",a,b,c))
    print (str.format("三角形的周长={0},三角形的面积 ={1}",long,area))
else:
    print ("不可构成三角形")