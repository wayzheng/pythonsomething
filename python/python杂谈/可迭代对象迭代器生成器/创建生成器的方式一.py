# -*- encoding: utf-8 -*-
"""

PyCharm 创建生成器的方式一.py
2024年10月14日21时46分
by wenyang

"""
from collections.abc import Iterator

def main():
    # 通过[]创建的是一个可迭代对象 而不是一个迭代器
    nums = [num for num in range(10)] # 列表推导式 list expression
    print(type(nums))
    print(isinstance(nums, Iterator))
    print(isinstance(iter(nums), Iterator))
    # 通过使用()创建的就是一个生成器对象
    nums1 = (num for num in range(10)) # 生成器表达式 generator expression
    print(type(nums1))
    print(nums1) # 生成一个生成器对象而不是一个数据


if __name__ == "__main__":
    main()
