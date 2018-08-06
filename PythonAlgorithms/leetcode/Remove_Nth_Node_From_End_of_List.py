class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head_list = self.convert_node_into_list(head)
        head_list.pop(len(head_list) - n)
        if head_list:
            return self.convert_list_into_node(head_list)
        else:
            return None

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
    l1_3 = ListNode(3)
    l1_2 = ListNode(2)
    l1_2.next = l1_3
    l1 = ListNode(1)
    l1.next = l1_2
    s_obj = Solution()
    res = s_obj.removeNthFromEnd(l1, 3)
