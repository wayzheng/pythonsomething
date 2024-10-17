# -*- encoding: utf-8 -*-
"""

PyCharm 类方法和静态方法.py
2024年10月17日20时50分
by wenyang

"""
class Foo(object):
    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """
        定义一个实例方法 至少有一个self参数 实例方法只能被实例对象调用
        :return:
        """
        print("实例方法")

    @classmethod
    # cls指向的就是这个类本身 如果cls是一个类对象的话 那么cls就是这个类的实例对象 如果传入的就是一个类的话 那么cls就是这个类本身
    def class_func(cls):
        """
        定义一个类方法 至少有一个cls参数
        :return:
        """
        # cls就是相当于这个类本身 也就是Foo类
        print(cls.__class__.__name__)
        print("这个就是一个类方法")

    @staticmethod
    def static_func():
        print("这个就是一个静态的方法")

def main():
    ...


if __name__ == "__main__":
    main()
