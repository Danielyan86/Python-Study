class Car:
    def __init__(self, brand, speed, color, price):
        self.brand = brand
        self.speed = speed
        self.color = color
        self.price = price


class CarInfo:

    def __init__(self):
        self.lst = []

    def add_car(self, car: Car):
        self.lst.append(car)

    def get_all(self):
        return self.lst

    def print_all_infor(self):
        if self.lst:
            print("print all cars information")
            for item in self.lst:
                print(f"brand: {item.brand}, speed: {item.speed}, color: {item.color}, price: {item.price}")
        else:
            print("car list is empty, there is no information to print")


if __name__ == '__main__':
    c = CarInfo()
    bmw = Car('bmw', 300, 'red', '200000')
    porsche = Car('porsche', 100, 'blue', 1000)
    c.add_car(bmw)
    c.add_car(porsche)
    c.print_all_infor()
