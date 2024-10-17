# -*- encoding: utf-8 -*-
"""

PyCharm filter函数.py
2024年10月17日17时11分
by wenyang

"""

def main():
    nums = range(100)
    even_nums = filter(lambda x: x % 2 == 0, nums) # 此时就是会返回使得后面的表达式结果为真的元素的值 返回的也是一个惰性的迭代器
    print()
    print(type(even_nums))
    print(list(even_nums))
    print(list(even_nums))


if __name__ == "__main__":
    main()
