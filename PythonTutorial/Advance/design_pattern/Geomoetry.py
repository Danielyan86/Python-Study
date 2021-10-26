class Geometry:
    def area(self):
        pass


class Rectangle(Geometry):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


class Square(Geometry):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length


if __name__ == '__main__':
    Rectangle1 = Rectangle(2, 5)
    print(Rectangle1.area())
    Square1 = Square(2)
    print(Square1.area())
