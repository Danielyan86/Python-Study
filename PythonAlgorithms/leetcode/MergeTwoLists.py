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
        if l1 and l2:
            l1_list, l2_list = self.convert_node_into_list(l1), self.convert_node_into_list(l2)
            new_list = sorted(l1_list + l2_list)
        elif l1:
            return l1
        elif l2:
            return l2
        else:
            return None

        return self.convert_list_into_node(new_list)

    def convert_list_into_node(self, list_p):
        node_list = [ListNode(i) for i in list_p]
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        return node_list[0]

    def convert_node_into_list(self, node_p):
        converted_list = [node_p.val]
        next_node = node_p.next
        while next_node:
            converted_list.append(next_node.val)
            next_node = next_node.next
        return converted_list


if __name__ == '__main__':
    l1_2 = ListNode(2)
    l1 = ListNode(1)
    l1.next = l1_2

    l2_2 = ListNode(4)
    l2 = ListNode(1)
    l2.next = l2_2

    s_obj = Solution()
    res = s_obj.mergeTwoLists([], [])
    print(res)
