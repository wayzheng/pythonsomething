# -*- encoding: utf-8 -*-
"""

PyCharm 01变量的命名的规范.py
2024年10月16日15时19分
by wenyang

"""
class Student(object):
    """
    实现一个学生的信息的类 通过使用迭代器来获取下一个元素
    """

    def __init__(self):
        self.info = []
        self.index = 0

    def add_info(self):
        person_info = {"name": input("请输入学生的姓名:\n")}
        while True:
            try:
                person_info["age"] = int(input("请输入学生的年龄:\n"))
                break
            except ValueError:
                print("输入错误请重新输入")
        self.info.append(person_info)



    def __iter__(self):
        return iter


    def __next__(self):
        if self.index < len(self.info):
            info_now = self.info[self.index]
            self.index += 1
            return info_now
        else:
            raise StopIteration



def main():
    stu = Student()
    stu.add_info()
    stu.add_info()
    stu.add_info()
    print(next(stu))


if __name__ == "__main__":
    main()
