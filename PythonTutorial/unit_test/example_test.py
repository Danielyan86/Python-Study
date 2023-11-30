import unittest
from unittest import mock, TestCase
from unittest.mock import MagicMock, PropertyMock

import example


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_add(self):
        self.assertEqual(example.add(1, 1), 2)

    @mock.patch("example.add")
    def test_convert_result_to_string(self, add):
        add.return_value = 4
        self.assertEqual("4", example.covert_result_to_string(2, 2))

    @mock.patch("example.add", new_callable=PropertyMock)
    def test_convert_result_to_string_2(self, add):
        add.return_value = 4
        self.assertEqual("4", example.covert_result_to_string(2, 2))


if __name__ == "__main__":
    unittest.main()
