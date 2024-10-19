# -*- encoding: utf-8 -*-
"""

PyCharm 解包的应用
2024年10月19日21时49分
by wenyang

"""
# 计算两点的距离 通过使用解包操作 就是使用负数的形式
def compute_distance(x1: tuple, x2: tuple) -> float:
    """
    计算两点之间的距离
    :param x1: 点的坐标 二维空间
    :param x2: 点的坐标 二维空间
    :return: 就是两点之间的距离
    """

    return abs(complex(*x1) - complex(*x2))
def get_first_and_last_element(*args):
    """
    使用解包来获取第一个和最后一个元素
    :param args: 序列
    :return: 一个元祖
    """
    first_element, *other_elements, last_element = args
    print(other_elements)
    return first_element, last_element

def main():
    x1 = (1, 2)
    x2 = (3, 4)
    print(compute_distance(x1, x2))
    # 通过使用round就是可以对小数进行四舍五入操作
    print(round(compute_distance(x1, x2), 3)) # 此时就是保留三位有效数字 四舍五入
    print(round(0.05, 1)) # 此时就是会返回0.1 会进行四舍五入操作
    print(get_first_and_last_element(1, 2, 3, 4, 5))
    items = range(10)
    print(get_first_and_last_element(*items)) # 传入序列的时候也要使用解包操作符来一一对应




if __name__ == "__main__":
    main()
