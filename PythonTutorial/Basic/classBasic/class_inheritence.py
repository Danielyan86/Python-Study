class Car:
    condition = "new"

    def __init__(self, model="default", color="default", speed="default"):
        print("initialize the ElectricCar")
        self.model = model
        self.color = color
        self.mpg = speed

    def display_car(self):
        return "This is a {0} {1} with {2} MPG. ".format(self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"

    def show_feature(self):
        print("this is a car")


# inheritence
class ElectricCar(Car):
    def __init__(self, model, color, speed, battery_type):
        print("initialize the ElectricCar")
        # super(ElectricCar, self).__init__(model, color, speed) #python2 way
        super().__init__(model, color, speed)
        self.battery_type = battery_type


class OilCar(Car):
    # 调用父类的初始化方法
    def __init__(self, model, color, speed, oil_type=97):
        print("initialize the OilCar")
        super().__init__(model, color, speed)
        self.oil_type = oil_type

    # 直接覆盖父类的方法
    def drive_car(self):
        self.condition = "used OilCar"


# multiple inheritence
class MixedCar(ElectricCar, OilCar):
    # depth-first, left-to-right,

    def show_feature(self):
        print("this is a MixedCar")


if __name__ == '__main__':
    Tesla = ElectricCar("SUV", "red", "40", "new")
    print(Tesla.display_car())
    Tesla.show_feature()

    Toyota = MixedCar("SUV", "red", "40", "new")
    Toyota.drive_car()
    print(MixedCar.mro())
    print(Toyota.condition)
    #
    # Ford = OilCar("truck", "blue", "30", "used")
    # Ford.display_car()
