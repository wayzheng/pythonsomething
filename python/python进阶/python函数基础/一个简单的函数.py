# -*- encoding: utf-8 -*-
"""

PyCharm 一个简单的函数.py
2024年10月17日18时30分
by wenyang

"""
# 此时这个函数定义就是一个全局的变量
a = 10
def func():
    # 此时定义的就是一个变量 就是一个局部变量
    b = 20
    print(a)

# print(b) 此时就是会报错 因为b是在函数内部的变量，所以在函数外部是无法访问的
def main():
    # print(func()) 如果函数的内部没有return 返回值 就是默认返回的值就是None
    func()
    print(func()) # 此时就是会执行函数的内部的代码 即时开始打印函数执行的返回值

if __name__ == "__main__":
    main()
