class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError('The first name must a string')

        if len(value) == 0:
            raise ValueError('The first name cannot be empty')

        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError('The last name must a string')

        if len(value) == 0:
            raise ValueError('The last name cannot be empty')

        self._last_name = value


if __name__ == '__main__':
    jonny = Person("Jonny", "wang")
    jonny.first_name = ""  # exception will be thrown
