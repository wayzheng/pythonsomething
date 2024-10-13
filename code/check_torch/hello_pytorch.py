# -*- encoding: utf-8 -*-
"""

PyCharm hello_pytorch
2024年10月13日12时12分
by wenyang

"""
import torch
def test():
    print(f"torch的版本就是{torch.__version__}")
    print(f"hello {torch.__version__}")
    if torch.cuda.is_available():
        print("可以使用cuda")
    else:
        print("不可以使用cuda")

def main():
    test()


if __name__ == "__main__":
    main()
