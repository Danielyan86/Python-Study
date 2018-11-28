from unittest import TestCase
from linked_list_basic import Node, SinglyLinkedList
from linked_list_method import reverse_linked_list, detect_the_loop


class Test_linked_list_Method(TestCase):

    def setUp(self):
        self.link_list1 = SinglyLinkedList()
        for i in range(1, 6):
            self.link_list1.insert_value_to_tail(i)

    def test_reverse_linked_list(self):
        h = reverse_linked_list(self.link_list1._head)
        self.assertEqual(h.value, 5)
        next_node = h.nextnode
        self.assertEqual(next_node.value, 4)

    def test_detect_the_loop(self):
        self.assertFalse(detect_the_loop(self.link_list1._head))
