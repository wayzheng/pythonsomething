# -*- encoding: utf-8 -*-
"""
PyCharm random创建随机数数组
2024年10月19日20时26分
by wenyang

"""
import numpy as np

def create_random_array(size):
    """
    通过使用random创建随机数数组
    :param size: 数组的大小
    :return:
    """
    print(np.random.randint(1, 100, size = size))
    print(np.random.randn(*size)) # 传入一个元祖的时候就是需要使用*来进行解包
def main():
    create_random_array((10, 10))



if __name__ == "__main__":
    main()
