# -*- encoding: utf-8 -*-
"""

PyCharm 递归函数的应用.py
2024年10月17日13时53分
by wenyang

"""
# 递归函数的应用
def factorial(n):
    """
    实现一个阶乘函数 通过使用递归的方式来进行实现
    :param n:  就是阶乘的数
    :return: 返回的就是阶乘的结果 也就是 n!
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """
    通过递归来实现一个菲波那切数列
    :param n: 就是项数
    :return: 返回的就是第n项的值
    """
    if n == 2 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print(factorial(23))
    print(fibonacci(10))


if __name__ == "__main__":
    main()
