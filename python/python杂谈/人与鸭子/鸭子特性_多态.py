# -*- encoding: utf-8 -*-
"""

PyCharm 鸭子特性_多态.py
2024年10月13日20时45分
by wenyang

"""

class Cat(object):
    def info(self):
        print("我是一只猫")
class Dog(object):
    def info(self):
        print("我是一只狗")
class Duck(object):
    def info(self):
        print("我是一只鸭子")

def main():
    animal_list = [Cat, Dog, Duck] # 此时 Cat都是变量的身份
    for animal in animal_list:
        animal().info() # 只有最后实例化的时候才会明白是一个类


if __name__ == "__main__":
    main()
