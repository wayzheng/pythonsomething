# -*- encoding: utf-8 -*-
"""

PyCharm 对象的基本组成和存储方式.py
2024年10月19日13时33分
by wenyang

"""
a = 10

def main():
    # 对象的基本组成就是 标识 类型 值 三个部分
    print(id(a)) # id() 函数就是用来获取对象的内存地址
    print(type(a)) # type() 函数就是用来获取对象的类型
    print(a) # 就是获取对象的值

    # 对象的存储方式有两种，一是栈存储，二是堆存储
    # 栈存储就是存储的是基本数据类型，比如 int float bool str tuple
    # 堆存储就是存储的是复杂数据类型，比如 list dict set
    # 但是在 python 中并没有栈和堆的概念，只是用来描述对象的存储方式
    # 所以在 python 中，对象的存储是通过列表来实现的，列表中存储的每一项就是一个对象的引用
    # 对象的引用就是对象的在内存中的地址
    b = a
    print(id(b)) # 所以 id() 函数返回的就是 b 和 a 的内存地址是一样的
    print(b is a) # 所以 is 运算符返回的就是 True

    # 对象的 id() 值是不一样的，因为 a 和 b 并不是同一个对象的引用
    print(hash(a))
    print(hash(b))
    print(id(a) == hash(a)) # 此时返回的就是false

if __name__ == "__main__":
    main()
