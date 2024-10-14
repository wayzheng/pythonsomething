# -*- encoding: utf-8 -*-
"""

PyCharm 通过使用生成器来完成斐波那契数列.py
2024年10月14日22时39分
by wenyang

"""
def fib_generator():
    num1 = 1
    num2 = 1
    while True:
        temp_num = num1
        num1, num2 = num2, num1 + num2
        yield temp_num # 此时就是会创建一个生成器对象
        # 只要有yield就是会创建一个生成器对象 然后就是可以通过使用next()函数来获取下一个值 通过这个函数返回的对象的类型就是一个生成器对象
        # 也就是说 有yield函数 就是一个生成器对象

def main():
    #  通过使用生成器来完成斐波那契书写
    fib = fib_generator()
    print(fib) # 此时fib就是一个生成器对象 就是返回的结果就是一个生成器对象
    # 然后通过使用next()函数就是可以获取下一个值
    print(next(fib))
    print(next(fib))
    # 在硬件允许的情况下 可以无限的获取下一个值 就是fib此时就是一个生成器 生成器是一个迭代器对象 也是一个可迭代对象 可以通过使用next()函数来获取下一个值
    for i in range(10):
        print(next(fib))

if __name__ == "__main__":
    main()
