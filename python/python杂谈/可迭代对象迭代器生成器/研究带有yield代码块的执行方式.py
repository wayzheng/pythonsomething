# -*- encoding: utf-8 -*-
"""

PyCharm 研究带有yield代码块的执行方式.py
2024年10月15日21时09分
by wenyang

"""
def fib_generator():
    print("__1__")
    num1 = 1
    num2 = 1
    while True:
        print("__2__")
        temp_num = num1
        print("__3__")
        num1, num2 = num2, num1 + num2
        print("__4__")
        yield temp_num # 此时就是会创建一个生成器对象
        print("__5__")

def main():
    fib = fib_generator() # 此时就是会创建一个生成器对象
    print(next(fib))
    print(next(fib))
    print(next(fib))


if __name__ == "__main__":
    main()
