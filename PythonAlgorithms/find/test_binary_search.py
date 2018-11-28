from unittest import TestCase

import binary_search


class TestBinary_search(TestCase):

    def test_binary_search(self):
        number_list, number = list(range(1000000)), 3334
        self.assertEqual(binary_search.binary_search(number_list, number), number)
