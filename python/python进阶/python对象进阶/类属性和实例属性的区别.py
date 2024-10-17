# -*- encoding: utf-8 -*-
"""

PyCharm 类属性和实例属性的区别.py
2024年10月17日20时36分
by wenyang

"""
# 类属性和实例属性的区别
# 最本质的区别就是保存的位置不同
class Person(object):
    name = "wenyang" # 这里定义的就是类属性 就是所有的实例对象都是共享的 对于一个类来说 只有一个name类属性 所有的实例对象都是共享的
    count = 0
    def __init__(self, name, age):
        # 但是对于实例属性来说 每一个实例对象的属性都是独立的
        self.name = name
        self.age = age
        Person.count += 1

    def show_info(self):
        print(f"{self.name}的年龄是{self.age}")
        print(f"人数就是{self.count}")
        print(f"{Person.name}")

def main():
    person = Person("wenyang", 18)
    person.show_info()
    person1 = Person("xiaoming", 20)
    person1.show_info()


if __name__ == "__main__":
    main()
