# -*- encoding: utf-8 -*-
"""

PyCharm 通过生成器创建随机数数组.py
2024年10月19日20时46分
by wenyang

"""
import numpy as np

# 通过生成器创建随机数数组
def create_random_array_by_generator(size):
    # 创建一个生成器
    rng = np.random.default_rng(2323)
    # 通过生成器创阿金整数 指定上下界
    print(rng.integers(1, 100, size = size))
    # 通过生成器创建一个标准正态分布的数组
    print(rng.standard_normal(size = size))
    # 通过生成器创建指定上下界的均匀分布的数组
    print(rng.uniform(1, 100, size = size))
    # 高斯分布数组
    print(rng.normal(0, 3, size = size))



def main():
    create_random_array_by_generator((10, 10))


if __name__ == "__main__":
    main()
