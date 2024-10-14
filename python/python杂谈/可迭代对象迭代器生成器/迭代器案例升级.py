# -*- encoding: utf-8 -*-
"""

PyCharm 迭代器案例升级.py
2024年10月14日17时26分
by wenyang

"""

from collections.abc import Iterable, Iterator
class Mylist(object):
    """
    自定义一个可迭代对象
    """
    def __init__(self):
        self.items = []
        self.index = 0

    def add(self, val):
        self.items.append(val)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            val = self.items[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

def main():
    mylist = Mylist()
    for i in range(10):
        mylist.add(i)
    print(type(mylist))
    if isinstance(mylist, Iterable):
        print("mylist is Iterable")
    else:
        print("最后的结果不是一个可迭代对象")
    if isinstance(mylist, Iterator):
        print("mylist is Iterator")
    else:
        print("该对象不是一个迭代器")
    for i in mylist:
        print(i)

    for i in mylist: # 此时就是不会在进行打印了这是因为在之前的for循环中 已经将结果进行迭代了
        print(i)


if __name__ == "__main__":
    main()
