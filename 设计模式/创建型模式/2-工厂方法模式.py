"""
# 工厂方法模式
内容:定义一个用于创建对象的接口(工厂接口)，让子类决定实例化哪一个产品类。
角色:
抽象工厂角色(Creator)
具体工厂角色 (Concrete Creator)
抽象产品角色(Product)
具体产品角色(Concrete Product)

优点:
每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
隐藏了对象创建的实现细节
缺点:
每增加一个具体产品类，就必须增加一个相应的具体工厂类

## 什么时候使用？
当创建一个特别复杂对象时，（参数 比较多）而且这个对象需要频繁创建时。


"""

from 抽象类方法 import AliPay, WechatPay, Pay
from abc import ABC, abstractmethod


class BankPay(Pay):
    def pay(self, money: float):
        print(f"使用银行支付{money}元")


class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self):
        pass


class AliPayFactory(PaymentFactory):
    def create_payment(self):
        return AliPay()


class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


class HuaabeiPayFactory(PaymentFactory):
    def create_payment(self):
        return AliPay(use_huabei=True)


class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


if __name__ == "__main__":
    hf = BankPayFactory()
    pay = hf.create_payment()
    pay.pay(100)
