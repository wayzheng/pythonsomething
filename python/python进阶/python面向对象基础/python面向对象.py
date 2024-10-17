# -*- encoding: utf-8 -*-
"""

PyCharm python面向对象.py
2024年10月17日19时05分
by wenyang

"""
class Student(object):
    """
    定义一个学生类
    """
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def change_score(self, score):
        self.score = score


def main():
    stu1 = Student("wenyang", 18, 100)


if __name__ == "__main__":
    main()
