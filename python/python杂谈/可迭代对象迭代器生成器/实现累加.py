# -*- encoding: utf-8 -*-
"""

PyCharm 实现累加.py
2024年10月15日22时38分
by wenyang

"""
def add():
    sum = 0
    while True:
        x = yield sum
        sum += x


def main():
    bar = add()
    print(next(bar)) # 此时就是返回值就是0 如果此时就是开始调用send的话就是会报错 因为此时x的值是一个None None不能加上一个int类型的值
    print(bar.send(23))
    print(bar.send(32))


if __name__ == "__main__":
    main()
