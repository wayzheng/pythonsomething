# -*- encoding: utf-8 -*-
"""

PyCharm 将列表推导式改为生成器有什么不同.py
2024年10月14日21时53分
by wenyang

"""

def main():
    nums = [x for x in range(10)]
    print(nums)
    for _ in nums:
        print(_)

    print("-" * 100)

    nums1 = (x for x in range(10))
    print(nums1)
    for _ in nums1:
        print(_)


if __name__ == "__main__":
    main()
