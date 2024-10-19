# -*- encoding: utf-8 -*-
"""

PyCharm 内置的命名空间.py
2024年10月19日14时51分
by wenyang

"""
# 内置命名空间就是通过使用builtins模块来实现的
import builtins

def main():
    # 将所有的内置函数和内置对象都放在了 builtins 模块中
    for i in dir(builtins):
        print(i)

    print(len(dir(builtins)))
    print("dir" in dir(builtins))

if __name__ == "__main__":
    main()
