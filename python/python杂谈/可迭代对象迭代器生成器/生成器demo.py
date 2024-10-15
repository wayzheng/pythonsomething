# -*- encoding: utf-8 -*-
"""

PyCharm 生成器demo.py
2024年10月15日22时54分
by wenyang

"""
def create_point(k, b):
    x = 1
    while True:
        y = k * x + b
        yield x, y
        x = y

def main():
    cp = create_point(2, 3)
    for _ in range(5):
        print(next(cp))

    print("可迭代对象 迭代器 生成器")


if __name__ == "__main__":
    main()
