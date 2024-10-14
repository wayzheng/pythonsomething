# -*- encoding: utf-8 -*-
"""

PyCharm 学生管理系统.py
2024年10月14日19时07分
by wenyang

"""


class StudentSystem(object):
    def __init__(self):
        self.stus = []
        self.index = 0

    def add(self):
        """
        添加新的学生信息
        :return:
        """
        name = input("请输入学生的姓名:\n")
        while True:
            try:
                age = int(input("请输入学生的年龄:\n"))
                break
            except ValueError:
                print("请输入正确的年龄")
        address = input("请输入学生的地址:\n")
        stu = {}
        stu["name"] = name
        stu["age"] = age
        stu["address"] = address
        self.stus.append(stu)

    # 定义__iter__方法 实现迭代器对象
    def __iter__(self):
        return self

    # 通过使用__next__方法实现迭代器对象
    def __next__(self):
        if self.index < len(self.stus):
            stuone = self.stus[self.index]
            self.index += 1
            return stuone
        else:
            raise StopIteration


def main():
    stu_sys = StudentSystem()
    for i in range(3):
        stu_sys.add()
# 直接就是可以来通过for循环来遍历对象
    for stu in stu_sys:
        for key, value in stu.items():
            print(f"{key} => {value}")
        print("*" * 100)


if __name__ == "__main__":
    main()
