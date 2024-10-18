# -*- encoding: utf-8 -*-
"""

PyCharm 可哈希的数据类型.py
2024年10月18日16时26分
by wenyang

"""
def hashable():
    # 可哈希的数据类型如果值相同 那么它们在内存中的存储的地址就是相同的
    a = 10
    b = 10
    c = 20
    d = "hello world"
    e = "hello world"
    f = 23, 34
    g = (23, 34)
    h = 3.1415926
    print(id(a), id(b), id(c), id(d), id(e), id(f), id(g))
    print(hash(a))
    print(hash(b))
    print(hash(d))
    print(hash(h))
    a = 23
    print(id(a)) # 当改变了一个数据 就是会发生地址改变
    # print(hash([2, 3, 5, 3])) 此时就是会发生报错 这是因为列表就是一个不可哈希的数据类型
def main():
    hashable()


if __name__ == "__main__":
    main()
