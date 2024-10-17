# -*- encoding: utf-8 -*-
"""

PyCharm 实例对象通过使用实例对象和类对象进行调用.py
2024年10月17日23时25分
by wenyang

"""
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"{self.name}的年龄是{self.age}")

def main():
    student1 = Student("wenyang", 21)
    # 通过实例对象来进行调用
    student1.show_info()
    print(type(student1.show_info)) # 类型就是method类型 说明就是一个方法 method
    # 通过使用类对象来进行调用
    Student.show_info(student1)
    print(type(Student.show_info)) # 类型就是function类型 说明就是一个函数 function


if __name__ == "__main__":
    main()
