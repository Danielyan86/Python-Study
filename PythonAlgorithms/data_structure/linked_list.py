class Node:
    def __init__(self, value, nextnode=None):
        self.value = value
        self._nextnode = nextnode  # python 对象传值，其实传递的就是对象引用，实现了类似指针的效果

    def __str__(self):
        return str(self.value)


class create_one_way_linked_list:
    def __init__(self, values_list):
        self.head_node = Node(values_list[0])
        if len(values_list) > 1:
            self.create_list(self.head_node, values_list)

    def create_list(self, node, value_list):  # 通过递归方式创建单项链表
        value_list = value_list[1:]
        node._nextnode = Node(value_list[0])
        if len(value_list) > 1:
            self.create_list(node._nextnode, value_list)
        else:
            return

    def travers_link_list(self, node):
        print(node)
        if node._nextnode:
            self.travers_link_list(node._nextnode)


if __name__ == '__main__':
    one_way_list = create_one_way_linked_list([i for i in range(10)])
    one_way_list.travers_link_list(one_way_list.head_node)
