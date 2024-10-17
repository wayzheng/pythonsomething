# -*- encoding: utf-8 -*-
"""

PyCharm 可迭代对象和迭代器和生成器.py
2024年10月17日14时21分
by wenyang

"""


# 可迭代对象就是可以通过使用for循环来进行遍历的对象
# 通过使用while循环来实现for循环的功能

class Stu_Sys(object):
    def __init__(self):
        self.stu = []

    def add_info(self):
        info = {}
        name = input("请输入学生的姓名:\n")
        info["name"] = name
        while True:
            try:
                age = int(input("请输入学生的年龄:\n"))
                break
            except ValueError:
                print("请输入一个整数年龄!")
        info["age"] = age
        self.stu.append(info)

    def __iter__(self):
        return Stu_Iter(self.stu)

class Stu_Iter(object):
    def __init__(self, stu):
        self.stu = stu
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.stu):
            result = self.stu[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


# 一个生成器
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b



def main():
    fib_one = fib()
    print(next(fib_one))
    print(next(fib_one))
    print(next(fib_one))


if __name__ == "__main__":
    main()
