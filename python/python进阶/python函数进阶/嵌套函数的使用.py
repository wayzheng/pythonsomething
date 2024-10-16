# -*- encoding: utf-8 -*-
"""

PyCharm 嵌套函数的使用.py
2024年10月16日23时08分
by wenyang

"""
def inner():
    a = 10
    def inner1():
        b = 20
        print(a + b)
        return a + b
    # return a + b 此时就是会发生报错 这是因为b是在inner1函数中定义的 所以在inner函数中是无法访问到的 即时外部函数无法访问到内部函数的变量 但是内部函数可以访问到外部函数的变量
    return inner1() # 这种操作即时闭包函数的操作 外部函数可以访问到内部函数的变量
def main():
    print(inner())


if __name__ == "__main__":
    main()
