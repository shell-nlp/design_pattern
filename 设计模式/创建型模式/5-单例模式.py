"""
单例模式
内容:保证一个类只有一个实例，并提供一个访问它的全局访问点
角色:
单例(Singleton)
优点:
对唯一实例的受控访问
单例相当于全局变量，但防止了命名空间被污染
"""
# 在python 中模块级的变量是单例的


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a
        pass


# 测试
if __name__ == "__main__":
    s1 = MyClass(10)
    s2 = MyClass(20)
    print(id(s1))
    print(id(s2))
    print(s1 is s2)
    print(s1.a)
    print(s2.a)
