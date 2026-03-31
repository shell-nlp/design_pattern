"""
# 简单工厂模式
内容:不直接向客户端暴露对象创建的实现细节(包括初始化)，而是通过一个工厂类来负责创建产品类的实例。
角色:
工厂角色(Creator)
抽象产品角色(Product)
具体产品角色(Concrete Product)

优点:
隐藏了对象创建的实现细节
客户端不需要修改代码
缺点:
违反了单一职责原则，将创建逻辑几种到一个工厂类里当添加新产品时，需要修改工厂类代码，违反了开闭原则

## 什么时候使用？
当客户端不知道具体创建哪个产品类时，或者当客户端只需要创建一个产品类时。

## 要点：
它们都实现了抽象产品角色(Product)的接口，它们属于同一族的产品。
"""

from typing import Literal

from 抽象类方法 import AliPay, WechatPay


class PaymentFactory:
    """使用工厂模式，这里连初始化都不让用户知道
    但是存在问题， 如果新添加一个支付方式，需要修改工厂类代码
    """

    def create_payment(self, method: Literal["ali", "wechat", "huabei"]):
        if method == "ali":
            return AliPay()
        elif method == "huabei":
            return AliPay(use_huabei=True)
        elif method == "wechat":
            return WechatPay()
        else:
            raise ValueError("不支持的支付方式")


if __name__ == "__main__":
    pf = PaymentFactory()
    pay = pf.create_payment("huabei")
    pay.pay(100)
