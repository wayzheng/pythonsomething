# -*- encoding: utf-8 -*-
"""

PyCharm reduce函数的使用.py
2024年10月17日17时22分
by wenyang

"""
from functools import reduce

def main():
    names = ["java", "python", "javascript", "c++", "c"]
    # 通过使用reduce函数来实现一个列表中的所有的元素的操作
    result = reduce(lambda x, y: x + y + '\t', names)
    print(result)

if __name__ == "__main__":
    main()
