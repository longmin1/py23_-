"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""


# 生成器
def provide():
    for i in range(1, 10):
        print("start")
        # # yield相当于 return , 暂停，记住上一次的执行位置
        yield i
        print("end")


# provide()
p = provide()
print("第一次")
print(next(p))
print("第二次")
print(next(p))
print("第三次")
print(next(p))
