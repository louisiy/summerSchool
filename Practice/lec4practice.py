#!/usr/bin/python3
# 一系列练习题供参考

#1 猜猜狗狗年龄
age = int(input("请输入你家狗狗的年龄: "))
print("")

if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")

#2 for语句
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print (x)

sites = ["Baidu", "Google", "Bing", "Taobao"]
for site in sites:
    if site == "Taobao":
        print("购物网站!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")



for letter in 'Python':
    if letter == 'h':
        break
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    print('当前变量值 :', var)
    var = var - 1
    if var == 5:
        break
 # 当变量 var 等于 5 时退出循环

print('Bye')

var = 10  # 第二个实例
while var > 0:

    var = var - 1
    if var == 5:
        continue
    print('变量值 :', var)
 # 当变量 var 等于 5 时退出循环

#3练习class
class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return '这个人的名字是%s,已经有%d岁了！'%(self.name,self.age)

class people:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'this person is %s, who is %d years old' %(self.name,self.age)
a = people("xx",18)
print(a)

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('红孩儿', 10, 30)
p.speak()



# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))

# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()


#5 类的实现

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)


#计时器练习
import time
print('按下回车开始计时，按下 Ctrl + C 停止计时')
while True:
	input("")
	starttime = time.time()
	print('开始')
	try:
		while True:
		    print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
		    time.sleep(1)
	except KeyboardInterrupt:
		print('结束')
		endtime = time.time()
		print('总共的时间为:', round(endtime - starttime, 2), 'secs')
		break