class Student():
    #name,age,course是类的变量，是这个类共同拥有的变量
    #变量的定义位置和方法，直接定义
    #不需要前缀
    name = 'xxx'
    age = 18
    course = 'python'
    #定义类中的函数一般需要有self关键字，其余与普通函数相同
    def giveMeMoney(self,n,a):#self 表示giveMeMoney，self.age声明的是实例的变量，如果不声明，则自动使用类的变量
        self.name = n
        self.age = a
        print('study python need money ')
        print(self.name,self.age)#如果没声明，实例变量可以调用类的变量
        return None
    def func():
        #类方法中不允许访问实例的任何内容
        #如果使用类里面的内容，有两种方法
        print(Student.name,__class__.age)
        return None

    #定义一个学生类
# 定义一个对象,中文可以当变量名，但不推荐
x = Student()#实例化一个叫x的学生
x.giveMeMoney('xxxxxs','48488')
Student.func()
Student.__dict__
############################################
#构造函数
class Student ():
    name = "no name"
    age = 0
    #构造函数的名称固定，写法相对固定
    def __init__(self):
        print('我是构造函数')
#继承
class Person():
    name = 'person1'
    age = 19
class Teacher(Person):
    #父类写在类定义的时候的括号里
    print('hhds')
    def teach(self):
        print("study harder")
    pass
class OldBrother():
    print("i m ur old brother")
    def protect(self):
        print("dont worry")
t = Teacher()
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(t.name)
print(Teacher.name)
class Kid(OldBrother,Teacher):#可以有多个父类，但是可能会有问题，不鼓励使用
    print("i m kid")
child = Kid()
child.teach()
child.protect()
# 利用issubclass检测是否是子类
print(issubclass(Kid,Teacher))
print(issubclass(Kid,Person))
print("------------------------------------")
# 构造函数的继承
# 构造函数默认继承，子类会默认继承父类的构造函数，此时要补足参数
class Persons():
    def __init__(self,name,age):
        print(name ,age)
class Teachers(Persons):
    pass
t = Teachers('sad',15)
class People(Person):
    name = "ljr"# name是公有的
    __age = 21# 此时age是私有的
p = People()
print(p.name)
class Personnn():
    def __init__(self):
        pass
    def __setattr__(self, key, value):
        print("这是魔术方法__setattr__的案例",key)
        #下面语句会导致死循环
        #self.key = value
        #这种情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(key,value)
p = Personnn()
p.vvvalue = 'something'
class Pperson():
    # 实例方法
    def eat(self):
        print(self)
        print("实例方法")
    # 类方法
    # 类方法第一个参数用cls，区别于self
    @classmethod
    def  play(cls):
        print(cls)
        print("这是一个类方法")
    # 静态方法
    # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print('这是静态方法')
p2 = Pperson()
p2.eat()
Pperson.say()
p2.say()
Pperson.play()
