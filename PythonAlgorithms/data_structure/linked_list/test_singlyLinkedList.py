from unittest import TestCase
from linked_list_basic import Node, SinglyLinkedList


class TestSinglyLinkedList(TestCase):
    def setUp(self):
        self.link_list1 = SinglyLinkedList()
        for i in range(1, 6):
            self.link_list1.insert_value_to_tail(i)

    def test_find_by_value(self):
        self.assertEqual(self.link_list1.find_by_value(1).value, 1)

    def test_find_by_index(self):
        self.assertEqual(self.link_list1.find_by_index(1).value, 2)

    def test_insert_value_to_head(self):
        self.link_list1.insert_value_to_head(0)
        self.assertEqual(self.link_list1.find_by_index(0).value, 0)

    def test_insert_node_to_head(self):
        new_node = Node(0)
        self.link_list1.insert_node_to_head(new_node)
        self.assertEqual(self.link_list1.find_by_index(0).value, 0)

    def test_insert_value_to_tail(self):
        self.link_list1.insert_value_to_tail(0)
        self.assertEqual(self.link_list1.find_by_index(5).value, 0)
        self.assertFalse(self.link_list1.find_by_index(6), 0)

    def test_insert_node_to_tail(self):
        new_node = Node(0)
        self.link_list1.insert_node_to_tail(new_node)
        self.assertEqual(self.link_list1.find_by_index(5).value, 0)
