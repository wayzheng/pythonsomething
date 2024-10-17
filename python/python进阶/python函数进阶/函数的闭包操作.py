# -*- encoding: utf-8 -*-
"""

PyCharm 函数的闭包操作.py
2024年10月17日14时09分
by wenyang

"""
def outer(num, name, *args, **kwargs):
    print(num)
    print(name)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)
    def inner():
        nonlocal num
        print(num + 10)
        num +=10
        print(num)
        print(name + "hello world")
        # name += "javascript" 此时就是会发生报错 这是因为name在没有进行nonlocal声明的时候是不能在内部函数进行修改的
    inner()
    print(num)
    print(name)
def main():
    outer(10, "python", 1, 2, 3, a = 1, b = 2, c = 3)



if __name__ == "__main__":
    main()
