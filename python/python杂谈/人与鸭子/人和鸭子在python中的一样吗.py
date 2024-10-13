# -*- encoding: utf-8 -*-
"""

PyCharm 人和鸭子在python中的一样吗.py
2024年10月13日21时06分
by wenyang

"""
class Person(object):
    def walk(self):
        print("人在走路")
    def eat(self):
        print("人在吃饭")
class Duck(object):
    def walk(self):
        print("鸭子在走")
    def eat(self):
        print("鸭子在吃东西")

class Animal(object):
    def desc(self, obj):
        obj.walk()
        obj.eat()


def main():
    # 只要有walk和eat方法 都是可以使用作为desc的参数来进行函数的调用
    animal = Animal()
    # 通过将实例化对象传入到desc方法中来进行调用
    # 在鸭子类型中 人和鸭子都是一样的
    animal.desc(Person())
    animal.desc(Duck())


if __name__ == "__main__":
    main()
