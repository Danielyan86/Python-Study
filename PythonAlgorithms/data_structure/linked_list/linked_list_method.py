from typing import Optional
from linked_list import SinglyLinkedList, Node


# 反转单链表
def reverse_linked_list(head_node: Optional[Node]):
    # 需要两个指针 一个记录上一个，一个记录当前
    pre_node = None  # 前一个节点，起始值为None
    cur_node = head_node  # 类似指针效果
    res_h = None
    while cur_node:  # 赋值顺序很重要，究竟是复制还是改指向，搞清楚
        pre_node = cur_node
        cur_node = cur_node.nextnode  # current node 必须先更新，否则没法找到下一个
        pre_node.nextnode = res_h  # 前一个节点始终指向新的链表的头结点，实现反转效果,改指向
        res_h = pre_node  # 更新头结点，相当于每次从头部插入

    return res_h


if __name__ == '__main__':
    link_list1 = SinglyLinkedList()
    for i in range(1, 6):
        link_list1.insert_value_to_tail(i)
    link_list1.print_all()
    h = reverse_linked_list(link_list1._head)
    link_list1._head = h
    link_list1.print_all()
    # while h.nextnode:
    #     print(h)
    #     h = h.nextnode
