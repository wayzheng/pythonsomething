# -*- encoding: utf-8 -*-
"""

PyCharm for循环通过使用while和迭代器来实现.py
2024年10月14日14时18分
by wenyang

"""


def main():
    # 通过使用for循环来实现比遍历一个字符串和列表
    strone = "hello world"
    listone = [1, 2, 3, 4, 5, 6]
    for char in strone:
        print(char)
    for num in listone:
        print(num)
    # 通过使用while和迭代器来实现
    # 获取迭代器对象
    print("*" * 100)
    strone_iterator = iter(strone)
    listone_iterator = iter(listone)
    # 通过使用while循环和异常处理来实现
    while True:
        try:
            print(next(strone_iterator)) # 通过使用next()方法来获取下一个元素
        except StopIteration:
            print("通过使用迭代器迭代完成")
            break
    while True:
        try:
            print(next(listone_iterator))
        except StopIteration:
            print("迭代完成")
            break


if __name__ == "__main__":
    main()
