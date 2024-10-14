# -*- encoding: utf-8 -*-
"""

PyCharm 生成器的引例.py
2024年10月14日19时48分
by wenyang

"""


def main():
    point_x_y_list = [] # 定义一个列表来存储每一个点的坐标位置
    i = 0
    x = 0
    while i < 5:
        y = 2 * x + 1
        point_x_y_list.append((x, y))
        x = y
        i += 1
    print(point_x_y_list)

if __name__ == "__main__":
    main()
