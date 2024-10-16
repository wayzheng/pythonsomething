# -*- encoding: utf-8 -*-
"""

PyCharm lambda函数的使用.py
2024年10月16日23时13分
by wenyang

"""
# lambda函数就是匿名函数
# lambda函数的语法就是 lambda 参数列表:表达式


def main():
    a = lambda x, y: x + y
    print(a(10, 20))


if __name__ == "__main__":
    main()
