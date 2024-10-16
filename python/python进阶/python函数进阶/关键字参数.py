# -*- encoding: utf-8 -*-
"""

PyCharm 关键字参数.py
2024年10月16日22时54分
by wenyang

"""
def desc(name, *nums, **kwargs):
    """
    位置参数 可变参数 关键字参数
    :param name: 姓名
    :param nums: 数字
    :param kwargs: 关键字参数
    :return: 一个描述的字符串
    """
    total = 0
    for val in nums:
        total += val
    str = ""
    for key, value in kwargs.items():
        str += f"{key} => {value} \n"
    return f"{name} 计算的结果就是 {total} 最后的参数的字符串就是 {str}"

def main():
    # 注意关键字的键值不能与位置参数和可变参数的参数名相同
    print(desc("wenyang", 23, 24, 25, 26, 27, 28, 29, 30, name1 = "张三", age = 25, city = "北京", country = "中国"))


if __name__ == "__main__":
    main()
