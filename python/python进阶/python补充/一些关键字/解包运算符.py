# -*- encoding: utf-8 -*-
"""

PyCharm 解包运算符
2024年10月19日21时37分
by wenyang

"""
import numpy as np
def unpacking_operator():
    # 解包运算符就是使用*来进行解包 可以对序列进行解包
    list_items = np.ones(10).tolist()
    list_items_tuple = tuple(list_items)
    print(list_items)
    # 如果不想要中括号就是可以是使用*来进行解包操作
    print(*list_items)
    print(list_items_tuple)
    print(*list_items_tuple)
    print("hello world")
    print(*"hello world") # 字符串也可以使用解包操作


def main():
    unpacking_operator()


if __name__ == "__main__":
    main()
