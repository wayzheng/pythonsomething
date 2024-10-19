# -*- encoding: utf-8 -*-
"""

PyCharm sorted函数的使用
2024年10月19日23时03分
by wenyang

"""


def main():
    # sorted函数可以对所有的可迭代对象进行排序操作，包括列表、元组、字符串、字典等。
    list_items = [12, 3, 5, 7, 9]
    sorted_items = sorted(list_items)
    print(sorted(list_items))
    print(sorted(list_items, reverse = True))
    print(sorted("hello world"))
    print(sorted((23, 5, 9, 32, 23)))
    # 通过使用key参数就是可以使用规则来进行排序 key可以是一个函数 也可以是一个lambda表达式
    dict_items = {"name": "wenyang", "age": 18, "gender": "male"}
    print(sorted(dict_items.items(), key = lambda x: x[0].upper(), reverse = True))
    for item in dict_items.items():
        print(item) # 返回的就是一个元祖 键值对组成的数组




if __name__ == "__main__":
    main()
