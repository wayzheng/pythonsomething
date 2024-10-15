# -*- encoding: utf-8 -*-
"""

PyCharm 生成器.py
2024年10月14日19时35分
by wenyang

"""
class GeometricSequence(object):
    def __init__(self, first, geo):
        self.first = first
        self.geo = geo
        self.index = 0
        self.temp = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            self.index += 1
            return self.temp
        else:
            self.index += 1
            self.temp *= self.geo
            return self.temp
# 通过使用生成器来实现多个等比数列
def GeometricSequenceFunc(first, geo):
    index = 0
    while True:
        temp = first * geo ** index
        index += 1
        yield temp
def main():
    geose_2 = GeometricSequence(23, 2)
    print(next(geose_2))
    print(next(geose_2))
    print(next(geose_2))
    gsf = GeometricSequenceFunc(23, 2)
    print(next(gsf))
    print(next(gsf))
    print(next(gsf))


if __name__ == "__main__":
    main()
