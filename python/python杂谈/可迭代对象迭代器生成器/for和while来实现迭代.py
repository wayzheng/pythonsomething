# -*- encoding: utf-8 -*-
"""

PyCharm for和while来实现迭代.py
2024年10月13日22时03分
by wenyang

"""


def main():
    message = "hello world"
    # 通过for循环来实现迭代
    for char in message:
        print(char)
    print("*" * 20)
    message_iter = iter(message) # 会返回一个迭代器
    while True:
        try:
            print(next(message_iter))
        except StopIteration:
            break



if __name__ == "__main__":
    main()
