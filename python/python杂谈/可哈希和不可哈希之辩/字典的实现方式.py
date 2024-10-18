# -*- encoding: utf-8 -*-
"""

PyCharm 字典的实现方式.py
2024年10月18日17时20分
by wenyang

"""
class Animal(object):
    count = 0
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def __hash__(self):
        Animal.count += 1
        return hash(self.name) + 1 # 哈希值要实例对象来进行
def exp_dict():
    """
    字典的键值就是通过使用哈希来进行查找的 字典的键值就是必须要可以哈希的 否则就是会发生冲突
    :return:
    """
    # 字典的键值就是必须是一个可以哈希的对象
    # 比如数字型、字符串类型、元祖类型、自定义的类的对象等可以哈希的对象
    # 通过使用数字作为键值的字典
    d = {1: 'a', 2: 'b', 3: 'c'}
    # 通过使用字符串作为键值的字典
    e = {'a': 1, 'b': 2, 'c': 3}
    # 通过使用元祖作为键值的字典
    f = {(1, 2): 3, (4, 5): 6}
    print(d[1])
    print(e["a"])
    print(f[(1, 2)])
    a = Animal("Dog", "旺财")
    print(hash(a))
    f = {a: "hello world", "python": "javascript"}
    print(f[a])

def main():
    exp_dict()


if __name__ == "__main__":
    main()
