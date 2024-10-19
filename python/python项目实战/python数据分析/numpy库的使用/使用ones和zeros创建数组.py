# -*- encoding: utf-8 -*-
"""

PyCharm 使用ones和zeros创建数组
2024年10月19日20时07分
by wenyang

"""
import numpy as np

def create_array():
    # 创建一个元素都是一的数组
    ones_array = np.ones(10)
    ones_2d_array = np.ones((3, 4))
    ones_3d_array = np.ones((3, 4, 5))
    # 创建一个元素都是0的数组
    zeros_array = np.zeros(10)
    zeros_2d_array = np.zeros((3, 4))
    zeros_3d_array = np.zeros((3, 4, 5))
    # 创建一个元素都是指定元素的数组
    full_array = np.full(10, 3.14)
    full_2d_array = np.full((3, 4), 3.14)
    full_3d_array = np.full((3, 4, 5), 3.14)
    print(ones_array)
    print(ones_2d_array)
    print(ones_3d_array)
    print(zeros_array)
    print(zeros_2d_array)
    print(zeros_3d_array)
    print(full_array)
    print(full_2d_array)
    print(full_3d_array)
def main():
    create_array()


if __name__ == "__main__":
    main()
