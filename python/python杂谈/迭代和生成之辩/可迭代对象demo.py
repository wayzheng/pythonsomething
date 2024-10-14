# -*- encoding: utf-8 -*-
"""

PyCharm 可迭代对象demo.py
2024年10月14日14时00分
by wenyang

"""
from collections.abc import Iterable, Iterator

class Iterable_one(object):
    # 定义__iter__方法 使得这个对象可以通过调用这个方法来产生一个迭代器对象
    def __iter__(self):
        pass
    def __repr__(self):
        return "Iterable_one()"
    def __str__(self):
        return "一个可迭代对象"
    # 通过使用__call__可以使得这个对象变得像一个函数一样可以进行遍历
    def __call__(self):
        return "调用了这个对象"



def main():
    # 实例化一个可迭代对象
    iterable = Iterable_one()
    # 判断这个对象是否是一个可迭代对象
    print(isinstance(iterable, Iterable)) # 返回结果就是一个True 就是表示当前对象就是一个可迭代对象 通过实例化类得到的结果就是一个可迭代对象
    print(type(iterable))
    print(iterable)
    print(iterable())


if __name__ == "__main__":
    main()