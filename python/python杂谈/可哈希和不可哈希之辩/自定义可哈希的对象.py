# -*- encoding: utf-8 -*-
"""

PyCharm 自定义可哈希的对象
2024年10月18日17时12分
by wenyang

"""
class Student(object):
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def desc(self):
        return f"{self.name} - {self.age}"

    def __hash__(self):
        Student.count += 1
        return Student.count + 1000

s1 = Student("Alice", 20)
s2 = Student("Bob", 21)


def main():
    print(hash(s1))
    print(hash(s2))


if __name__ == "__main__":
    main()
