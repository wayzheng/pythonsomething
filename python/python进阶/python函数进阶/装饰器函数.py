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

@outer1(3)
def func1():
    print("*" * 10)
def main():
    func()
    func1()


if __name__ == "__main__":
    main()
