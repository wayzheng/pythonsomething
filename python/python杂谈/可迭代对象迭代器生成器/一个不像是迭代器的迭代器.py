# -*- encoding: utf-8 -*-
"""

PyCharm 一个不像是迭代器的迭代器.py
2024年10月13日21时56分
by wenyang

"""
from collections import abc
class Foo(object):

    def __iter__(self):
        pass
def main():
    # Iterable就是指的就是 可迭代对象
    # 由此可以看出 只要一个对象实现了__iter__方法 那么这个对象就是一个可迭代对象
    issubclass(Foo, abc.Iterable)


if __name__ == "__main__":
    main()
