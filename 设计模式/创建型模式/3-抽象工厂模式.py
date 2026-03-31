"""
# 抽象工厂模式

内容:定义一个工厂类接口，让工厂子类来创建一系列相关或相互依赖的对象。
例:生产一部手机，需要手机壳、CPU、操作系统三类对象进行组装，其中每类对象都有不同的种类。对每个具体工厂，分别生产一部手机所需要的三个对象。
相比工厂方法模式，抽象工厂模式中的每个具体工厂都生产一套产品。

角色:
抽象工厂角色(Creator)
具体工厂角色(Concrete Creator)
抽象产品角色(Product)
具体产品角色 (Concrete Product)
客户端(Client)
优点:
将客户端与类的具体实现相分离
每个工厂创建了一个完整的产品系列，使得易于交换产品系列有利于产品的一致性(即产品之间的约束关系)
缺点:
难以支持新种类的(抽象)产品

## 什么时候使用？



"""

from abc import ABC, abstractmethod


# ---- 抽象产品----
class PhoneShell(ABC):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(ABC):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(ABC):
    @abstractmethod
    def show_os(self):
        pass


# --- 抽象工厂---
class PhoneFactory(ABC):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# --- 具体产品 ----


class SmallShell(PhoneShell):
    def show_shell(self):
        print("小手机壳")


class BigShell(PhoneShell):
    def show_shell(self):
        print("大手机壳")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("骁龙CPU")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")


class AndroidOS(OS):
    def show_os(self):
        print("安卓操作系统")


class iOSOS(OS):
    def show_os(self):
        print("iOS操作系统")


# --- 具体工厂 ----
class MiPhoneFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()

    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return AndroidOS()


# --- 客户端 ----


class Phone:
    def __init__(self, factory: PhoneFactory):
        self.shell = factory.make_shell()
        self.cpu = factory.make_cpu()
        self.os = factory.make_os()

    def show_phone(self):
        self.shell.show_shell()
        self.cpu.show_cpu()
        self.os.show_os()


def make_phone(factory: PhoneFactory):
    return Phone(factory)


if __name__ == "__main__":
    p = make_phone(MiPhoneFactory())
    p.show_phone()
