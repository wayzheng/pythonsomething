# -*- encoding: utf-8 -*-
"""

PyCharm check.py
2024年10月12日23时49分
by wenyang

"""
import torch


def main():
    print(f"hello torch {torch.__version__}") # 返回结果就是torch的版本号
    print("hello AI and hello world!")
    print(torch.cuda.is_available()) # 返回结果就是True 就是表示可以使用GPU来进行处理了 表示的就是GPU就是可以进行使用

if __name__ == "__main__":
    main()
