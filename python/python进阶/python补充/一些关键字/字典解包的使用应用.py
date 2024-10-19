# -*- encoding: utf-8 -*-
"""

PyCharm 字典解包的使用应用.py
2024年10月19日22时50分
by wenyang

"""
def dict_upacking_operator():
    # 解包字典操作符就是通过使用**来进行解包操作
    dict_items = {"name": "wenyang", "age": "18"}
    # print(dict_items)
    # print(**dict_items)
    print(1, 2, 3, 4, sep = ",", end = "#")
    config = {"sep": ",", "end": "#"}
    print(1, 2, 3, 4, **config)
def add(x, y, z):
    return x + y + z
def main():
    # 三种方式使用这个函数
    print(add(1, 2, 3))
    print(add(x = 1, y = 2, z = 3))
    print(add(*range(1, 4)))
    print(add(**{"x": 1, "y": 2, "z": 3}))


if __name__ == "__main__":
    main()
