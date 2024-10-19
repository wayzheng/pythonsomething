# -*- encoding: utf-8 -*-
"""

PyCharm 具体数据创建数据.py
2024年10月19日19时55分
by wenyang

"""
import numpy as np

def main():
    list_item = [23, 3, 5, 7]
    tuple_item = (23, 4, 5, 3)
    print(np.array(list_item))
    print(np.array(tuple_item))
    print(type(np.array(list_item)))
    # 通过这种方式得到的结果是一样的这是因为创建的是一个临时的数组 使用完之后就是会别销毁
    print(id(np.array(list_item)))
    print(id(np.array(tuple_item)))
    list_array = np.array(list_item)
    tuple_array = np.array(tuple_item)
    print(list_array)
    print(tuple_array)
    # 此时的到的id即时不一样的
    print(id(list_array))
    print(id(tuple_array))



if __name__ == "__main__":
    main()
