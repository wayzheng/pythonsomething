# -*- encoding: utf-8 -*-
"""

PyCharm 可变参数的生成器.py
2024年10月15日23时04分
by wenyang

"""
def create_point():
    x = 0
    # 初始设置k = 2 b = 1
    k = 2
    b = 1
    while True:
        y = k * x + b
        temp = yield x, y
        if temp:
            k = temp
        x = y

def main():
    cp = create_point()
    print(next(cp))
    print(next(cp))
    print(cp.send(3))
    print(cp.send(4))
    print(cp.send(5))


if __name__ == "__main__":
    main()
