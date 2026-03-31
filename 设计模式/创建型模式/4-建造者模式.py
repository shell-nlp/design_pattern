""" "
# 建造者模式
内容:将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
角色:
抽象建造者(Builder)
具体建造者(Concrete Builder)
指挥者(Director)
产品(Product)

建造者模式与抽象工厂模式相似，也用来创建复杂对象。主要区别是建造者式着重一步步构造一个复杂对象，而抽象工厂模式着重于多个系列的产品对象。
优点:
隐藏了一个产品的内部结构和装配过程
将构造代码与表示代码分开
可以对构造过程进行更精细的控制

"""

from abc import ABC, abstractmethod


class Player:
    def __init__(self, face, body, arm, leg):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return f"Player(face={self.face}, body={self.body}, arm={self.arm}, leg={self.leg})"


class PalyerBuilder(ABC):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


class SexyGirlBuilder(PalyerBuilder):
    def __init__(self):
        self.player = Player("", "", "", "")

    def build_face(self):
        self.player.face = "sexy girl face"

    def build_body(self):
        self.player.body = "sexy girl body"

    def build_arm(self):
        self.player.arm = "sexy girl arm"

    def build_leg(self):
        self.player.leg = "sexy girl leg"


class MonsterBuilder(PalyerBuilder):
    def __init__(self):
        self.player = Player("", "", "", "")

    # 表示代码
    def build_face(self):
        self.player.face = "monster face"

    def build_body(self):
        self.player.body = "monster body"

    def build_arm(self):
        self.player.arm = "monster arm"

    def build_leg(self):
        self.player.leg = "monster leg"


class PlayerDirector:
    def build_player(self, builder: PalyerBuilder):  # 控制组装顺序
        # 构造代码
        builder.build_face()
        builder.build_body()
        builder.build_arm()
        builder.build_leg()
        return builder.player


if __name__ == "__main__":
    builder = SexyGirlBuilder()
    director = PlayerDirector()
    player = director.build_player(builder)
    print(player)
