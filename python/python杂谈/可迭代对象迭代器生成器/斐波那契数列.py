# -*- encoding: utf-8 -*-
"""

PyCharm 斐波那契数列.py
2024年10月14日22时08分
by wenyang

"""
# 斐波那契数列的实现方式
# 方式一 通过使用递归的方式函数式编程
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# 方式二 通过使用迭代的方式来进行
class Fib(object):
    def __init__(self):
        self.a, self.b = 1, 1
        self.index = 1
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 1:
            result = self.a
            self.index += 1
        elif self.index == 2:
            result = self.b
            self.index += 1
        else:
            result = self.a + self.b
            self.a, self.b = self.b, result
            self.index += 1
        return result
    # 简化后的代码
    class FibS(object):
        def __init__(self):
            self.num1 = 1
            self.num2 = 1

        def __next__(self):
            """
            通过使用next()函数调用来获取下一个数
            :return:
            """
            temp_num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return temp_num

        def __iter__(self):
            return self




def main():
    ...


if __name__ == "__main__":
    main()
