class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_list = ListNode()
        while l1.next or l2.next:
            if l1.next and l2.next:
                temp_node = ListNode()
                temp_node.val = l1.val if l1.val <= l2.val else l2.val
                new_list.next = temp_node
            elif l1.next:

            elif l2.next

    def traverse_node(self, l_node):
        return l_node.value, l_node.next


if __name__ == '__main__':
    l1_2 = ListNode(2)
    l1 = ListNode(1)
    l1.next = l1_2

    l2_2 = ListNode(4)
    l2 = ListNode(1)
    l2.next = l2_2

    s_obj = Solution()
    s_obj.mergeTwoLists(l1, l2)
