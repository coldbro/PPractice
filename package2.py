import package1
import sys
print(type(sys.path))
print(sys.path)
# 列表类型，可以用for循环遍历
for p in sys.path:
    print(p)
stu = package1.Student()
stu.say()
package1.sayHello()