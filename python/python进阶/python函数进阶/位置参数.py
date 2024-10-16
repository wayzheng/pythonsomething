# -*- encoding: utf-8 -*-
"""

PyCharm 位置参数.py
2024年10月16日22时39分
by wenyang

"""
# 没有默认的位置参数 多参数会报错 少参数也会报错 出现的错误报告就是SnytaxError 就是语法的错误
def add(a, b):
    return a + b
def sub(a, b):
    pass
def mul(a = 8, b = 8):
    return a * b
def main():
    # print(add(1, 3, 5))   此时就是会发生报错
    print(add(1, 3)) # 正确的使用方式就是通过这种方式来进行传递参数
    # print(sub(1)) # 此时也会发生报错
    print(mul()) # 此时就是会使用默认的参数进行运算而不会发生报错



if __name__ == "__main__":
    main()
