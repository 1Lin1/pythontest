# L=['a','b','c','d']
# L.append('e')
# print (L)

# s={1,2,3}
# print (s)
# 默认参数的函数，调用时可以不用写
# def enroll (name,gender,city="sz",age="10"):
#     print ("name:",name)
#     print ("gender:",gender)
#     print ("city:",city)
#     print ("age:",age)
# enroll("Jack","F")

# None 为不可变对象，调用多少次都可以


# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('end')
#     print(L)


# add_end([1, 2, 3])


# # # *为可变参数，即可传入0或任意多个参数
# def cal(*nums):
#     sum = 0
#     for i in nums:
#         sum = sum+i
#     print(sum)


# cal(1, 2, 3)

# # 传入一个list

# # newnum=[3,4,5]
# # cal(*newnum)

# # # #关键字参数 **
# def person (name,age,**kw):
#     print (name,age,'other:',kw)
# person ('Jack',24,city='bj',job='student')

# # # #关键字参数扩展功能
# # extra={'city':'sd','Job':'CEO'}
# # person('Jack','M',city=extra['city'],Job=extra['Job'])

# # # #简化写法
# # person('Hoyutim','F',**extra)

# #命名关键字参数 ,*限制只能传入city和job


# def person2(name, age, *, city, job):
#     print(name, age, city, job)


# person2('BOB', 24, city='bj', job='student')



# # 如果函数已经定义了一个可变参数，则后面的关键字参数不需加*
# def person3(name, age, *args, sex,city, job):
#     print(name, age, args, sex,city, job)
# numms=[1,2,3]
# person3 ('Jack',24,*numms,sex='f',city='bj',job='Ceo')

# def person4(name,age,*,city='bj',job):
#     print (name,age,city,job)
# person4('Jack',24,job='STUDENT')

# #参数的顺序必须是必选参数，默认参数，可变参数，命名关键字参数，关键字参数
# def f1(a,b,c=0,*args,**kw):
#     print ('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

# def f2(a,b,c=1,*,d,**kw):
#     print ('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)


# f1(1,2)
# f1(1,2,c=3)
# f1(1,2,3,'a','b','c',x=1,y=2,z=3)
# f2(1,2,d=99,x=98,y=97,z=96)

# #传入tuple 和dict
# args=(1,2,3,[4,5,6,7,8])
# kw={'x':11,'y':22}
# f1(*args,**kw)

# #多个参数的乘法
# def product(x,*y):
#     s=1
#     n=len(y)
#     while n>0:
#         n=n-1
#         s=s*y[n]
#     print  (x*s)
# #j加入range要用*号
# product (5,*range(2,5))

#4.14

#同时引用两个变量
# for x,y in [(1,1),(2,2),(3,3)]:
#     print (x,y)

# #找最大值和最小值
# def findMaxAndMin(L):
#     if L==[]:
#         return (None,None)
#     max=L[0]
#     min=L[0]
#     for x in L:
#         if max<x:
#             max=x
#         if min>x:
#             min=x
#     return (max,min)

# print (findMaxAndMin([1,3,5,7,11,8,6,4,20,-1]))

# L=[x**3 for x in range(1,11) if x%2==0]
# print (L)

# #双层循环，输出全排列
# L=[m+n for m in 'ABC' for n in 'XYZ']
# print (L)

# #for 循环可以用到多个变量
# d={'x':'A','Y':'B'}
# for k,v in d.items():
#     print (k,'=',v)

# #所以，列表生成也可以用两个变量
# L=[k+'='+v for k,v in d.items()]
# print (L)

# #字母小写
# # L=['HELLO','Linhuan']
# # L=[s.lower() for s in L]
# # print (L)

# #istance判断是否为字符串
# L1=['Hello','World',18]
# L2=[s.lower() for s in L1 if isinstance(s,str)]
# print (L2)

# #生成器g 用()表示 打印不能直接用g
g=(x*x for x in range(1,10))
for i in g:
    print(i,end=" ")

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
#把list、dict、str等Iterable变成Iterator可以使用iter()函数

from collections import Iterator
print (isinstance(iter([]),Iterator))


