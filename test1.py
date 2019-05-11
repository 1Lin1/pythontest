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

#参数的顺序必须是必选参数，默认参数，可变参数，命名关键字参数，关键字参数
def f1(a,b,c=0,*args,**kw):
    print ('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=1,*,d,**kw):
    print ('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)


f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b','c',x=1,y=2,z=3)
f2(1,2,d=99,x=98,y=97,z=96)

#传入tuple 和dict
args=(1,2,3,[4,5,6,7,8])
kw={'x':11,'y':22}
f1(*args,**kw)

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
# g=(x*x for x in range(1,10))
# for i in g:
#     print(i,end=" ")

# #生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# #把list、dict、str等Iterable变成Iterator可以使用iter()函数

# print (isinstance(iter([]),Iterator))



#类和对象

# class Person:
#     def __init__(self,name,age):
#        self.name=name
#        self.age=age
#     def say_hi(self):
#         print ('你好 我叫',self.name)
# p1=Person("Jack",18)
# p1.say_hi()
#类似java中的类和对象

# class Person2:
#     count=0
#     name='Person'
# Person2.count+=1
# print (Person2.count)
# print (Person2.name)
# #类属性，静态属性

# class Person11:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name (self):
#         """lock"""
#         return self.__name

# p=Person11('王五')
# print (p.name)
# #property 的用法

# class Person12:
#     def say_hi(self,name):
#         self.name=name
#         print ('我叫'+self.name)

# p=Person12()
# p.say_hi('hah')

# class Foo:
#     className='FOO'
#     def __init__(self,name):#构造方法
#         self.name=name
#     def f1(self):   #实例方法
#         print (self.name)
#     @staticmethod
#     def f2(): #静态方法
#         print ('static')
#     @classmethod
#     def f3(cls):#类方法
#         print (cls.className)
# f=Foo('林')
# f.f1()
# Foo.f2()
# Foo.f3()

#在python中可以定义多个重名的方法，但只有最后一个生效

# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def say_hi(self):
#         print ("你好 我叫{0},今年{1}岁了".format(self.name,self.age))
# class student(Person):
#     def __init__(self,name,age,stu_id):
#         Person.__init__(self,name,age) 
#         #重点:声明派生类，必须在其构造函数调用基类的构造函数
#         self.stu_id=stu_id
#     def say_hi(self):
#         Person.say_hi(self)
#         print ("我的学号是{0}".format(self.stu_id))

# p=Person("林洹",18)
# p.say_hi()
# p2=student("hoyutim",17,201710089069)
# p2.say_hi()

# class Dime:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def area(self):
#         pass
# class Retangle:
#     def __init__(self,w,h):
#         Dime.__init__(self,w,h)
#     def area(self):
#         return self.x*self.y
# d1=Retangle(3.0,4.0)
# print (d1.area())

#4.26

# class Student():
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
# #self指向实例本身
#     def get_grade(self):
#         if self.score>=90:
#             return 'A'
#         elif self.score>=60:
#             return 'B'
#         else:
#             return 'C'
# a=Student('Lisa',99)
# b=Student('Nna',56)
# print (a.get_grade())
# print (b.get_grade())

# class Student2():
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def print_age(self):
#         print ('%s:%s'%(self.__name,self.__age))
#     def set_age(self,age):
#         self.__age=age
#     def get_age(self):
#         return self.__age
# a=Student2('LISA',12)
# b=Student2('nan',13)
# a.print_age()
# b.print_age()
# print (a.get_age())
# b.set_age(133)
# print (b.get_age())

#__name私有属性

# class Animal:
#     def run(self):
#         print ('Animal is running')

# class Dog(Animal):
#     def run(self):
#         print ('dog is running')
#         #重写继承的方法
#     def eat(self):
#         print ('dog is eat')

# class Cat(Animal):
#     def run(self):
#         print ('cat is running')
#           #重写继承的方法
#     def eat(self):
#         print ('cat is eat')
# class Timer():
#     def run(self):
#         print ('dada')
# def run_twice(animal):
#     animal.run()
#     animal.run()
# d=Dog()
# run_twice(Dog())
# run_twice(Timer())#python是动态语言，只要有run方法，都能继承
# print  (isinstance(d,Dog)) #用isinstanceo判断类型

# # 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# print (dir(d))#获得一个对象的所有属性和方法

# print (hasattr(d,'x'))#是否有x属性
# setattr(d,'x',100) #设置x属性
# setattr(d,'y',200)
# print (getattr(d,'x'))  #获取x属性
# print (getattr(d,'y',404))#获取y属性，若不存在返回404
# fn=getattr(d,'x')
# print (fn)  

# sum=d.x+d.y
# print (sum)

class Dimon:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        pass
class Circle(Dimon):
    count=0
    def __init__(self,r):
        Dimon.__init__(self,r,0)
        Circle.count+=1
    def area(self):
        return self.x*self.x*3.14
    def __del__(self):
        Circle.count-=1
    def getcount(self):
        print ('总数是',Circle.count)
class Retangle(Dimon):
    def __init__(self,w,h):
        Dimon.__init__(self,w,h)
    def area(self):
        return self.x*self.y

d1=Circle(2.0)
d2=Circle(4.0)
d1.__del__()
print (d1.getcount())

