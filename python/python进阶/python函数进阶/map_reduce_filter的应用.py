# -*- encoding: utf-8 -*-
"""

PyCharm map_reduce_filter的应用.py
2024年10月17日19时23分
by wenyang

"""
from functools import reduce
def numsquare_to_str(num):
    return map(lambda x: f"{x}", map(lambda x: x ** 2, range(1, num + 1)))
def num_join(num: list[int]):
    return reduce(lambda x, y: x * 10 + y, num)
def del_phonenumbers_contain_4(phone_numbers: list[str]):
    return filter(lambda x: "4" not in x, phone_numbers)
def main():
    print(list(numsquare_to_str(10)))
    print(num_join(list(range(1, 9))))
    print(list(del_phonenumbers_contain_4(["1234", "5678", "123456789"])))



if __name__ == "__main__":
    main()
