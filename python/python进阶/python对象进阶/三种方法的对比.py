# -*- encoding: utf-8 -*-
"""

PyCharm 三种方法的对比.py
2024年10月17日23时42分
by wenyang

"""
class Person(object):
    name = "wenyang"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 实例化方法
    def show_info(self):
        print(f"{self.name}的年龄就是{self.age}")

    # 使用类方法
    @classmethod
    def say_hello(cls):
        print(cls.name)
        print("hello")

    # 使用静态方法
    @staticmethod
    def say_hi():
        print("hi")

def main():
    stu1 = Person("wenyang", 21)
    print(stu1.name)
    print(Person.name)
    stu1.show_info()
    Person.say_hello()
    stu1.say_hi()
    print(type(stu1.say_hi)) # 此时就是一个函数function的类型
    print(type(Person.say_hello)) # 此时就是一个方法method的类型



if __name__ == "__main__":
    main()
