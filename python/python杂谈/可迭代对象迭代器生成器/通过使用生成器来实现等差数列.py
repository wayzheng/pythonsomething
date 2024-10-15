# -*- encoding: utf-8 -*-
"""

PyCharm 通过使用生成器来实现等差数列
2024年10月15日21时30分
by wenyang

"""
def ArithmeticSequenceFunc(first, diff):
    temp = first
    while True:
        yield temp
        temp += diff
        yield temp
        temp += 2 * diff
        yield temp
        temp += 3 * diff
        return "hello world"
        # return "hello world" 如果在调用next()函数的时候 从上一次的暂停的位置 继续向下执行的时候 遇不到yield函数 那么就是会产生异常
        # 如果在调用next()函数的时候 从上一次的暂停的位置 继续向下执行的时候 遇到了return函数 那么也会产生异常
def main():
    As = ArithmeticSequenceFunc(21, 2)
    print(next(As))
    print(next(As))
    print(next(As))
    try:
        print(next(As))
    except StopIteration as ret:
        # 此时就是可以通过使用这种方式来获取return 函数的返回值
        print(ret.value)

if __name__ == "__main__":
    main()
