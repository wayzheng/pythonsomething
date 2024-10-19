# -*- encoding: utf-8 -*-
"""

PyCharm nolocal关键字和global关键字.py
2024年10月19日21时06分
by wenyang

"""
import numpy as np
a = 100
# 如果要实现一个装饰器 计算一个函数的执行的次数 就是需要通过一个count俩进行计数 count需要再函数执行完成之后会进行加一操作
def count(func):
    count = 0
    def wrapper(*args, **kwargs):
        # nonlocal关键字作用就是在内部函数使用 声明外部函数的局部变量 这样就可以在内部函数中对外部函数的局部变量进行修改
        nonlocal count
        count += 1
        print("*" * 10 + "函数执行的次数就是" + str(count) + "*" * 10)
        return func(*args, **kwargs)
    return wrapper
@count
def filter_func(*args, **kwargs):
    print(*args)
    nums = filter(lambda x: x > 10, args)
    return list(nums)

def main():
    list_items = list(range(100))
    print(list_items)
    print(filter_func(*list_items))
    print(list(filter(lambda x: x > 10, list_items)))



if __name__ == "__main__":
    main()
