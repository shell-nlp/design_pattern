"""
抽象类方法
"""

from abc import ABC, abstractmethod


class Pay(ABC):
    @abstractmethod
    def pay(self, money: float):
        pass


class AliPay(Pay):
    def __init__(self, use_huabei: bool = False):
        self.use_huabei = use_huabei

    def pay(self, money: float):
        if self.use_huabei:
            print(f"使用花呗支付{money}元")
        else:
            print(f"使用支付宝支付{money}元")

    pass


class WechatPay(Pay):
    def pay(self, money: float):
        print(f"使用微信支付{money}元")


if __name__ == "__main__":
    a = AliPay()
