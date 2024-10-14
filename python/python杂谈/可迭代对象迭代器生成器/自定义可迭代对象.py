# -*- encoding: utf-8 -*-
"""

PyCharm 自定义可迭代对象.py
2024年10月14日16时06分
by wenyang

"""
# 定义一个可迭代对象的类
class MyIterable(object):
    def __init__(self, *numbers):
        self.number = list(numbers)
    def add(self, number):
        self.number.append(number)
    def __iter__(self):
        # 标记用当前类创建出来的对象一定是一个可迭代对象
        # 当调用iter()函数的时候 这个方法会自动调用 他返回自己指定的那个迭代器
        return MyIterator(self.number)
# 定义一个迭代器对象的类
class MyIterator(object):
    def __init__(self, numbers):
        # 保存可迭代对象的数据
        self.numbers = numbers
        # 设置索引
        self.index = 0

    def __next__(self):
        # 标记当前类创建出来的对象 (还需要__iter__方法) 是一个迭代器对象
        # 当调用next方法的时候 就是会调用__next__方法 就是使用next(迭代器对象)的时候 这个方法就是会自动调用 他返回一个数据
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        # 迭代结束的时候 就是会抛出一个异常 这个异常叫StopIteration
        else:
            raise StopIteration
    def __iter__(self):
        return self

def main():
    myiterable = MyIterable(1, 3, 5, 7, 9)
    myiterator = iter(myiterable)
    print(type(myiterator)) # 表示就是一个迭代器这个对象
    print(type(myiterable)) # 表示的就是一个可迭代对象
    while True:
        try:
            print(next(myiterator))
        except StopIteration:
            break
    myiterable.add(11) # 添加上这个元素之后下面的句子还是会发生报错 这是因为迭代器已经经实例化完毕 之后再添加 就是需要在重新实例化一遍
    # print(next(myiterator)) 此时就是会发生报错 就是StopIteration错误



if __name__ == "__main__":
    main()
