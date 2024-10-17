# -*- encoding: utf-8 -*-
"""

PyCharm 装饰器函数.py
2024年10月16日23时16分
by wenyang

"""
# 装饰器函数的三种使用方式
# 1 只是对函数进行功能上的拓展
def outer(funcone):
    def wrapper():
        print("开始执行函数")
        funcone()
        print("函数执行结束")
    return wrapper

@outer
def func():
    print("*" * 10)
# 传递参数 扩展功能的时候 传递参数
def outer1(times):
    def outer1(func):
        # 通过*args 和 **kwargs 来接受参数然后传递
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        return wrapper
    return outer1
# 通过一个装饰器函数来实现计算函数执行的次数的功能
def outer2(func):
    """
    通过一个装饰器函数来实现计算函数执行的次数的功能
    :param func: 就是要被装饰的函数
    :return: 返回的就是一个函数对象
    """
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f"函数执行了{count}次")
    return wrapper
@outer1(3)
def func1():
    print("*" * 10)
# 装饰器如果没有参数要进行传递的时候 就是不需要在()内部加上参数
@outer2
def bar(message):
    print("hello world" + message)
def main():
    func()
    func1()
    bar("javascript")
    bar("javascript")


if __name__ == "__main__":
    main()
