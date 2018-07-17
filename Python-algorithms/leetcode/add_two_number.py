# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list, l2_list = [], []
        # if isinstance(l1, ListNode):

        l1_list.append(l1.val)
        next_node = l1.next
        if next_node:
            while next_node.next:
                l1_list.append(next_node.val)
                next_node = next_node.next
            l1_list.append(next_node.val)
            # if isinstance(l2, ListNode):

        l2_list.append(l2.val)
        next_node = l2.next
        if next_node:
            while next_node.next:
                l2_list.append(next_node.val)
                next_node = next_node.next
            l2_list.append(next_node.val)
        print(l1_list, l2_list)
        l1_str = ""
        for i in l1_list[::-1]:
            l1_str = l1_str + str(i)
        l2_str = ""
        for i in l2_list[::-1]:
            l2_str = l2_str + str(i)
        res = str(int(l1_str) + int(l2_str))

        node_list = [ListNode(int(i)) for i in res[::-1]]
        for i in range(0, len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        return node_list[0]


if __name__ == '__main__':
    last_node = ListNode(3)
    middle_node = ListNode(4)
    middle_node.next = last_node
    l1 = ListNode(2)
    l1.next = middle_node
    last_node = ListNode(4)
    middle_node = ListNode(6)
    middle_node.next = last_node
    l2 = ListNode(5)
    l2.next = middle_node
    s_obj = Solution()
    print(s_obj.addTwoNumbers(ListNode(0), ListNode(0)))
