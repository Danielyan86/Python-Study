from abc import (
    abstractmethod,
    ABCMeta,
)  # 接口类中定义了一些接口名：Pay，且并未实现接口的功能，子类继承接口类，并且实现接口中的功能


class Payment(metaclass=ABCMeta):  # 抽象出的共同功能Pay
    @abstractmethod
    def pay(self, money):
        pass  # 这里面的pay 来源于下面类中的方法pay,意思把这个方法规范为统一的标准，另外建一个规范类Payment


class Alipay(Payment):
    def pay(self, money):  # 这里出现paying和我们规范的pay不一样，那么在实例化 Alipay的时候就会报错
        print(f"支付宝支付了:{10}")


class Wechat(Payment):
    def pay(self, money):
        print(f"微信支付:{money}")


def pay(pay_obj, money):
    pay_obj.pay(money)


if __name__ == "__main__":
    # p = Payment()  # 接口类不能直接实例化
    Ali = Alipay()
    pay(Ali, "10")
    # p = Alipay()  # 实例化的时候就会报错
