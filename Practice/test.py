class Test:
    def prt(self):
        print(self)
        print(self.__class__)
        print(self.__class__.__name__)

t = Test()
t.prt()
print(Test.__class__)
print(Test().__class__)
print(Test().__class__()) #返回了类的一个新实例
print(Test.__class__(Test))