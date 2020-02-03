'''
class Test():
    def __init__(self):
        self.age = 11111.111
    def fget(self):
        print("这是读操作")
        return self.age
    def fset(self,age):
        self.age = int(age)
        print("这是对变量操作")
    def fdel(self):
        pass
    age1 = property(fget,fset,fdel,'这是说明文档')#property的四个参数顺序是固定的
name = Test()
print(name.age)
name.age1 = 18.1777
print(name.age1)
'''
'''
#抽象类的实现
import abc
#声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):#括号内参数是规定的
    # 定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass
    # 定义抽象类方法
    @abc.abstractclassmethod
    def drink():
        pass
    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass
'''
# 自己组装一个类
class Lei():
    pass
def func(name):
    print("woleiwa ",name)
func("naruto")
Lei.func = func
#函数名当作变量,类绑定函数可以，如果变量绑定则要借助工具from types import MethodType
'''
a = Lei()
a.func = MethodType(func,Lei)
'''
a = Lei()
a.func()
#用type创建一个类
def keybord(self):
    print("i m keybord")
def screen(self):
    print("i m screen ")
A = type("ClassName",(object,),{"class_keybord":keybord,"class_screen":screen})
a = A()
a.class_keybord()
a.class_screen()#可以想正常访问一样使用类
# 元类演示
# 元类写法是固定的，必须继承自type
# 元类一半以MetaClass结尾
class YuanLeiMetaClass(type):
    #主要以下写法
    def __new__(cls, name,bases,attrs):
        print("这是个元类")
        attrs['id'] = '11111111'#用元类创建的所有类，都有'id'这个属性
        return  type.__new__(cls,name,bases,attrs)
# 元类定义完就可以使用，使用注意写法
class CreateClass(object,metaclass=YuanLeiMetaClass):
    pass
c = CreateClass()
print(c.id)