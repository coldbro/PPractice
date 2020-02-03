# 包含一个学生类
# 一个sayhello函数
# 一个打印语句
class Student():
    def __init__(self,name = "no name",age =18):
        self.name = name
        self.age = age
    def say(self):
        print("my name is {0}".format(self.name))

def sayHello():
    print("nihao ")
#if __name__ == "__main__":
    # 此判断语句建议一直作为程序的入口
    # 在别的文件中调用时候，避免模块代码被导入的时候被动执行的问题
print("打印一句话")