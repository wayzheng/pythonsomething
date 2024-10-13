# -*- encoding: utf-8 -*-
"""

PyCharm 鸭子类型的实例.py
2024年10月13日20时52分
by wenyang

"""
# 通过使用对象的例子来进行全面的说明鸭子类型
from abc import ABCMeta, abstractmethod

class Payment(metaclass = ABCMeta):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @abstractmethod # 表示的就是下面的方法就是必须要子啊子类进行实现的方法
    def pay(self, *args, **kwargs):
        pass

class AilPay(Payment):
    def pay(self):
        print(f"{self.name}通过使用支付宝支付了{self.money}元")

class WechatPay(Payment):
    def pay(self):
        print(f"{self.name}通过使用微信支付了{self.money}元")

class Pay(object):
    def account(self, pay_obj):
        pay_obj.pay()
def main():
    # 实例化支付对象
    alipay = AilPay("小明", 100)
    wechatpay = WechatPay("小红", 200)
    # 只要有pay方法 都是可以使用作为account的参数来进行函数的调用
    order = Pay()
    order.account(alipay)
    order.account(wechatpay)
# 多态性就是相同的函数方法触发 对于不同的类做出的不同的响应



if __name__ == "__main__":
    main()
