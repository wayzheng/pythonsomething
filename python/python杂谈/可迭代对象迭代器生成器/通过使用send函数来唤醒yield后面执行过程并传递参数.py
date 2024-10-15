# -*- encoding: utf-8 -*-
"""

PyCharm 通过使用send函数来唤醒yield后面执行过程并传递参数.py
2024年10月15日22时01分
by wenyang

"""


def foo():
    num = 1
    while True:
        temp = yield num
        num *= temp
        print(temp)


def main():
    # 传递参数实现连乘
    f = foo()
    print(next(f))
    print(f.send(23))  # 通过迭代器.send(参数)来进行参数的传递
    print(f.send(23))


if __name__ == "__main__":
    main()
