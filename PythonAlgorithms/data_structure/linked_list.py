class Node:
    def __init__(self, value=None, nextnode=None):
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

    def inter_nodes(self, node):
        print(node)
        if node._nextnode:
            self.inter_nodes(node._nextnode)


class LinkedList:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.root = Node()  # 初始化头结点和末尾节点，当只有一个元素是同一个节点，可以理解成给头尾节点取别名，注意头结点为一个值为空的节点
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("Full")

        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:  # 如果为节点为空，则表示当前节点是root节点。因为root节点初始化时候置为空，
            self.root.next = node
        else:  # 如果不为空，则当前节点不是root
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def iter_node(self):
        curnode = self.root.next  # 跳过了根节点
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):  # 重写内置iter方法，方便外部使用for关键字调用，返回值
        for node in self.iter_node():
            yield node.value


def test_LinkedList():
    list_obj = LinkedList(5)
    list_obj.append(1)
    list_obj.append(2)
    list_obj.append(3)
    num = 0
    for value in list_obj:
        if num == 0:
            assert value == 1
        elif num == 1:
            assert value == 2
        num = num + 1


if __name__ == '__main__':
    one_way_list = create_one_way_linked_list([i for i in range(10)])
    one_way_list.inter_nodes(one_way_list.head_node)
    list_obj = LinkedList(4)
    list_obj.append(1)
    list_obj.append(2)
    test_LinkedList()
