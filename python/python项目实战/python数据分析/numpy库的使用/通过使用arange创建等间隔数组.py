# -*- encoding: utf-8 -*-
"""

PyCharm 通过使用arange创建等间隔数组
2024年10月19日20时18分
by wenyang

"""
import numpy as np

def create_array():
    # 通过使用arange就是可以创建一个等间隔的数组 可以指定间隔
    print(np.arange(1, 100, np.pi))
    # 通过使用linspace可以创建一个已知长度的等间隔的数组
    print(np.linspace(1, 100, 100))
    # 通过使用logspace可以创建一个已知长度的等间隔的数组，且间隔是对数间隔
    print(np.logspace(1, 100, 100, base = 2, dtype = np.float32)) # 就是可以通过使用base来指定底数




def main():
    create_array()


if __name__ == "__main__":
    main()
