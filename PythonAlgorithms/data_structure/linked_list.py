from typing import Optional


class Node:
    # 假设存入的都是整数类型
    def __init__(self, value: int = None, nextnode=None):
        self.value = value
        self.nextnode = nextnode  # python 对象传值，其实传递的就是对象引用，实现了类似指针的效果

    def __str__(self):
        return str(self.value)


class SinglyLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None

    def __iter__(self):
        p = self._head
        while p:
            yield p
            p = p.nextnode

    def find_by_value(self, value: int) -> Optional[Node]:
        p = self._head
        while p and p.value != value:
            p = p.nextnode
        return p

    def find_by_index(self, index: int) -> Optional[Node]:
        p = self._head
        position = 0
        while p and position != index:
            p = p.nextnode
            position += 1
        return p

    def insert_value_to_head(self, value: int):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self, new_node: Node):
        if new_node:
            new_node.nextnode = self._head
            self._head = new_node

    def insert_value_to_tail(self, value: int):
        new_node = Node(value)
        self.insert_node_to_tail(new_node)

    def insert_node_to_tail(self, new_node: Node):
        if not self._head:
            self._head, self._tail = new_node, new_node
        else:
            self._tail.nextnode = new_node  # 在尾节点增加新节点
            self._tail = new_node  # 更新尾节点

    def insert_value_after(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_after(node, new_node)

    def insert_node_after(self, node: Node, new_node: Node):
        if not node or not new_node:
            return
        new_node.nextnode = node.nextnode
        node.nextnode = new_node

    def insert_value_before(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_before(node, new_node)

    def insert_node_before(self, node: Node, new_node: Node):
        if not self._head or not node or not new_node:
            return
        if self._head == node:
            self.insert_node_to_head(new_node)
            return
        current = self._head
        while current.nextnode and current.nextnode != node:
            current = current.nextnode
        if not current.nextnode:  # node is not even in the list
            return
        new_node.nextnode = node
        current.nextnode = new_node

    def delete_by_node(self, node: Node):
        if not self._head or not node:
            return
        if node.nextnode:
            node.value = node.nextnode.value
            node.nextnode = node.nextnode.nextnode
            return
        # node is the last one or not in the list
        current = self._head
        while current and current.nextnode != node:
            current = current.nextnode
        if not current:  # node not in the list
            return
        current.nextnode = None

    def delete_by_value(self, value: int):
        if not self._head or not value:
            return
        fake_head = Node(value + 1)
        fake_head.nextnode = self._head
        prev, current = fake_head, self._head
        while current:
            if current.value != value:
                prev.nextnode = current
                prev = prev.nextnode
            current = current.nextnode
        if prev.nextnode:
            prev.nextnode = None
        self._head = fake_head.nextnode  # in case head.value == value

    # def __repr__(self) -> str:
    #     nums = []
    #     current = self._head
    #     while current:
    #         nums.append(current.value)
    #         current = current.nextnode
    #     if len(nums) > 0:
    #         return "->".join(str(num) for num in nums)
    #     else:
    #         return ""

    def print_all(self):
        current = self._head
        if current:
            print(f"{current.value}", end="")
            current = current.nextnode
        while current:
            print(f"->{current.value}", end="")
            current = current.nextnode
        print("\n", flush=True)


class create_one_way_linked_list:
    def __init__(self, values_list):
        self.head_node = Node(values_list[0])
        if len(values_list) > 1:
            self.create_list(self.head_node, values_list)

    def create_list(self, node, value_list):  # 通过递归方式创建单项链表
        value_list = value_list[1:]
        node.nextnodenode = Node(value_list[0])
        if len(value_list) > 1:
            self.create_list(node.nextnodenode, value_list)
        else:
            return

    def inter_nodes(self, node):
        print(node)
        if node.nextnodenode:
            self.inter_nodes(node.nextnodenode)


def test_LinkedList():
    link_list1 = SinglyLinkedList()
    for i in range(1, 6):
        link_list1.insert_value_to_tail(i)
    assert link_list1.find_by_index(0).value == 1
    assert link_list1.find_by_index(2).value == 3
    assert link_list1.find_by_value(2).value == 2
    link_list1.delete_by_value(0)
    assert link_list1.find_by_index(0).value == 2
    link_list1.delete_by_node(0)
    assert link_list1.find_by_index(0).value == 3


if __name__ == '__main__':
    link_list1 = SinglyLinkedList()
    for i in range(1, 6):
        link_list1.insert_value_to_tail(i)
    assert link_list1.find_by_index(0).value == 1
    assert link_list1.find_by_index(2).value == 3
    assert link_list1.find_by_value(2).value == 2
    link_list1.delete_by_value(0)
    assert link_list1.find_by_index(0).value == 3
