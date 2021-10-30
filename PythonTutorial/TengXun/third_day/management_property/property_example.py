class House:

    def __init__(self, price):
        self._price = price  # 在 Python 中，按照惯例，当你在一个名字上添加前导下划线时，你就是在告诉其他开发者，它不应该在类之外被直接访问或修改。如果有中介（getters 和 setters）的话，它只能通过中介来访问。

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter  # 等价于 H=H.delter
    def price(self):
        del self._price


if __name__ == '__main__':
    my_house = House(100000)
    print(my_house.price)  # will call the price function under the     @property
    my_house.price = 0  # will call the function under the   @price.setter

