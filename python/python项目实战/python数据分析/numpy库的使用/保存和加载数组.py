# -*- encoding: utf-8 -*-
"""

PyCharm 保存和加载数组.py
2024年10月19日20时58分
by wenyang

"""
import numpy as np
def save_array():
    arr = np.random.randint(1, 100, size = (10, 9))
    np.save("array", arr)
    print(arr)
def load_array():
    print(np.load("array.npy"))
def main():
    save_array()


if __name__ == "__main__":
    main()
