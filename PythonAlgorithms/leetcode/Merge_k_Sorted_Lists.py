# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists:
            temp_list = list(filter(lambda x: x != None, lists))  # 过滤出空链表,返回是一个迭代器，需要转化成列表，否则下一句判断空列表无法生效
            if temp_list:
                temp_list = map(self.convert_node_into_list, temp_list)
                extend_list = []
                for item in temp_list:
                    extend_list.extend(item)
                extend_list = sorted(extend_list)
                return self.convert_list_into_node(extend_list)

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
    # l1.next = l1_2

    l2_2 = ListNode(4)
    l2 = ListNode(1)
    l2.next = l2_2

    s_obj = Solution()
    res = s_obj.mergeKLists([l1, l2])
    print(res)
