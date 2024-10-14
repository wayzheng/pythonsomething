# -*- encoding: utf-8 -*-
"""

PyCharm 通过迭代器来实现生成多个数据.py
2024年10月14日20时03分
by wenyang

"""
class Pointxy(object):
    """
    通过使用迭代器来实现生成多个数据
    """
    def __init__(self):
        self.x = 0
        self.k = 2
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        temp_y = self.k * self.x + self.b
        temp_point_x_y = (self.x, temp_y)
        self.x = temp_y
        return temp_point_x_y

    def chang_k(self, k):
        self.k = k

    def change_b(self, b):
        self.b = b

class Fb(object):
    def __init__(self):
        self.a, self.b = 1, 1
        self.index = 1

    # 就是调佣iter()函数返回的迭代器就是自己
    def __iter__(self):
        return self

    # 通过使用迭代器方式来生成多个数据 方法虽然可以但是比较繁琐和麻烦
    def __next__(self):
        if self.index == 1:
            self.index += 1
            return self.a
        elif self.index ==2:
            self.index += 1
            return self.b
        else:
            # 通过使用这种方式可以减少数据的内存占用
            self.index += 1
            # 表示的就是存储数据的方式
            self.a, self.b = self.b, self.a + self.b
            # 然后就是返回的得到的结果
            return self.b
def main():
    point = Pointxy()
    print(next(point))
    print(next(point))
    for i in range(100):
        print(next(point))

    fb = Fb()
    for i in range(10):
        print(next(fb))

if __name__ == "__main__":
    main()
