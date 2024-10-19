# -*- encoding: utf-8 -*-
"""

PyCharm demo.py
2024年10月19日16时17分
by wenyang

"""

b = 10
def main():
    a = 10
    print(f"全局命名空间 {globals()}")
    print(f"局部命名空间 {locals()}")


if __name__ == "__main__":
    main()
