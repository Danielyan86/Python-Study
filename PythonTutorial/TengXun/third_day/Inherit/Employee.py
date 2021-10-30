# 定义父类Employee
class Employee:  # py3中默认从object继承
    company = "haide"

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


# 定义manger类，从基类继承下来
class Manager(Employee):
    # 如果子类没有定义构造方法，则直接调用父类构造方法
    def __init__(self, name, pay):
        super().__init__(name, "mgr", pay)  # super相当于Employee
        self.manegement_level = "l1"
        # Employee.__init__(self,name, "mgr", pay)

    # 重写父类方法
    def give_raise(self, percent, bonus=0.10):
        super().give_raise(percent + bonus)

    # 新增子类方法
    def manege_team(self):
        print("manage team")


if __name__ == "__main__":
    xiaoming = Employee("xiaoming", "ma nong", 1000)  # 初始化一个父类
    xiaoma = Manager("xiao ming", 15000)  # 初始化一个子类
    xiaoma.give_raise(0.1, 0.1)  # 调用重写后子类方法
    print(xiaoma.pay)  # 调用父类属性
    print(xiaoma.company)  # 打印父类信息
    xiaoma.manege_team()  # 调用子类新增方法
    print(xiaoma.manegement_level)
