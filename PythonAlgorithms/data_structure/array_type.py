# 用list创建一个仿数组数据结构，不是真正的数组
class user_array:
    def __init__(self, capacity: int):
        self._data = []
        self.capacity = capacity
        self._count = 0

    def __getitem__(self, index: int):
        if 0 <= index < self._count:
            return self._data[index]

    def find(self, index: int):
        return self._data[index]

    def update(self, index: int, value: int):
        if 0 <= index < self._count:
            self._data[index] = value
        else:
            raise AssertionError("index is out of range")

    def delete_element(self, index: int):
        if index > self._count or index < 0:  # 超出现有数组索引值范围，抛出异常
            raise AssertionError("index is out of range")
        if self._count == 0:
            raise AssertionError("array is empty")
        else:
            self._data = self._data[:index] + self._data[index + 1 : -1]
            self._count = self._count - 1

    # 中间插入一个元素
    def insert_element(self, index: int, value: int):
        if index > self._count or index < 0:  # 超出现有数组索引值范围，抛出异常
            raise AssertionError("index is out of range")
        if index == 0:
            self._data = [value] + self._data
        elif index == self._count:
            self._data.append(value)
        elif 0 < index < self._count:
            self._data = self._data[:index] + [value] + self._data[index:]
        self._count = self._count + 1

    def insert_to_tail(self, element: int):
        if self._count < self.capacity:
            self._data.append(element)
            self._count = self._count + 1
        else:
            raise AssertionError("index is out of range")

    def return_array(self):
        return self._data

    def empty_arry(self):
        self._data = []
        self._count = 0
        self.capacity = 0


def test_user_arrry():
    my_array = user_array(10)
    my_array.insert_element(0, 1)
    assert my_array.find(0) == 1
    assert my_array[0] == 1
    my_array.insert_element(1, 2)
    assert my_array.find(1) == 2
    my_array.insert_to_tail(3)
    assert my_array._count == 3
    my_array.insert_to_tail(5)
    my_array.return_array()
    my_array.delete_element(0)
    my_array.return_array()


if __name__ == "__main__":
    my_array = user_array(10)
    my_array.insert_element(0, 1)
    print(my_array.return_array())
    my_array.insert_element(1, 2)
    for i in range(3, 6):
        my_array.insert_to_tail(i)
    print(my_array.return_array())
    my_array.delete_element(2)
    print(my_array.return_array())
