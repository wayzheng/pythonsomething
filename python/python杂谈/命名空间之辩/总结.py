# -*- encoding: utf-8 -*-
"""

PyCharm 总结
2024年10月19日16时04分
by wenyang

"""
import random, copy

def func1():
    b = 20
    print(f"全局变量 {globals()}")
    print(f"局部变量 {locals()}")

def func2():
    a = 10
    print(f"全局变量 {globals()}")
    print(f"局部变量 {locals()}")

def add(*args):
    print(f"全局变量 {globals()}")
    print(f"局部变量 {locals()}")
    return sum(args)
def main():
    func1()
    func2()
    print(f"全局变量 {globals()}")
    print(f"局部变量 {locals()}")
    print(dir(copy))
    print(dir(random))
    print(add(*range(1, 100)))



if __name__ == "__main__":
    main()
