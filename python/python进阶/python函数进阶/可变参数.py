# -*- encoding: utf-8 -*-
"""

PyCharm 可变参数.py
2024年10月16日22时46分
by wenyang

"""
def add(*args):
    """
    通过使用可变参数来实现多个参数的求和
    :param args: 传入的就是输入的参数任意参数
    :return: 就是所有的参数的和
    """
    total = 0
    for val in args:
        total += val
    return total
def name_add(name, *args):
    """
    可变参数必须要放在位置参数的后面
    :param name: 姓名
    :param args: 传入的参数
    :return: 就是一句话
    """
    total = 0
    for val in args:
        total += val
    return f"{name} 计算出的总和就是 {total}"
def main():
    print(add(23, 35, 56, 12))
    print(name_add("wenyang", 23,24, 52))


if __name__ == "__main__":
    main()
