# -*- encoding: utf-8 -*-
"""

PyCharm 局部命名空间.py
2024年10月19日15时06分
by wenyang

"""
from functools import reduce

def main():
    a = 10
    def add(*args):
        return reduce(lambda x, y: x + y, args)
    b = add(*range(1, 20))

    print(locals())


if __name__ == "__main__":
    main()
