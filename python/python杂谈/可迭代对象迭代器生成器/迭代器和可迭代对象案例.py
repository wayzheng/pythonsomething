# -*- encoding: utf-8 -*-
"""

PyCharm 迭代器和可迭代对象案例.py
2024年10月14日16时43分
by wenyang

"""
class Mylist(object):
    """自定义个一个可迭代对象"""
    def __init__(self):
        self.list = []

    def add(self, item):
        self.list.append(item)

    def __iter__(self):
        # 将对象作为参数传递
        return MyIterator(self)

class MyIterator(object):
    """自定义个一个迭代器"""
    def  __init__(self, mylist):
        self.index = 0
        self.list = mylist

    def __next__(self):
        if self.index < len(self.list.list):
            item = self.list.list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self



def main():
    mylist = Mylist()
    for i in range(10):
        mylist.add(i)
    mylist_iterator = iter(mylist)
    while True:
        try:
            print(next(mylist_iterator))
        except StopIteration:
            break
    print("*" * 100)
    # print(next(mylist_iterator)) 此时会发生报错
    for i in mylist:
        print(i)



if __name__ == "__main__":
    main()
