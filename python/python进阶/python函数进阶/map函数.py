# -*- encoding: utf-8 -*-
"""

PyCharm map函数.py
2024年10月17日16时49分
by wenyang

"""


def main():
    names = ["java", "python", "javascript", "c++", "c"]
    # 在每一个字符的后面加上一个换行符
    new_names = list(map(lambda x: x + "\n", names))
    for name in new_names:
        print(name)
    # 通过可以将函数作为一个参数传递给map函数
    def double(x):
        return x * 2
    double_names = map(double, names) # 此时就是会返回一个map对象 而不是一个列表
    print(type(double_names))
    print(double_names)
    print(list(double_names))
    # 由于map是一个惰性的迭代器 所以在已经将double_names转换为列表的时候 就是已经将迭代器中的所有的元素都已经进行迭代完成了
    double_names_list = list(double_names)
    print(double_names_list)
    for i in double_names_list:
        print(i)

if __name__ == "__main__":
    main()
