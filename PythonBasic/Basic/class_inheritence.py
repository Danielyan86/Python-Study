class Car:
    condition = "new"

    def __init__(self, model="default", color="default", speed="default"):
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
        # super(ElectricCar, self).__init__(model, color, speed) #python2 way
        super().__init__(model, color, speed)
        self.battery_type = battery_type


class OilCar(Car):
    def __init__(self, model, color, speed, oil_type):
        self.battery_type = oil_type
        self.model = model
        self.color = color
        self.mpg = speed


# multiple inheritence
class MixedCar(ElectricCar, Car):
    # 广度优先搜索
    def __init__(self, model, color, speed, battery_type):
        super().__init__(model, color, speed, battery_type)

    def show_feature(self):
        print("this is a electricar")


if __name__ == '__main__':
    Tesla = ElectricCar("SUV", "red", "40", "new")
    print(Tesla.display_car())
    Tesla.show_feature()
    mixed_obj = MixedCar("SUV", "red", "40", "new")

    Ford = OilCar("truck", "blue", "30", "used")
    Ford.display_car()
