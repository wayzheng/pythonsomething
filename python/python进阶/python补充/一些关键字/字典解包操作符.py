# -*- encoding: utf-8 -*-
"""

PyCharm 字典解包操作符
2024年10月19日22时44分
by wenyang

"""
def dict_unpacking_operator():
    # 解包字典操作符就是通过使用**来进行解包操作
    dict_items = {"name": "wenyang", "age": "18"}
    # print(dict_items)
    # print(**dict_items)
    print(1, 2, 3, 4, sep = ",", end = "#")
    config = {"sep": ",", "end": "#"}
    print(1, 2, 3, 4, **config)


def main():
    dict_unpacking_operator()


if __name__ == "__main__":
    main()
