# -*- encoding: utf-8 -*-
"""

PyCharm 函数返回值作为一个内存地址.py
2024年10月17日18时21分
by wenyang

"""
def add(x, y):
    return x + y

def main():
    print(add)
    print(add(1, 3))


if __name__ == "__main__":
    main()
