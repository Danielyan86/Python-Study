class tree_node:
    '''基本单元结构，最底层的节点单元可以看子节点为None的节点'''

    def __init__(self, data, left_data=None, right_data=None):
        self.data = data
        self.left = left_data
        self.right = right_data


class b_tree:
    def create_b_tree(self):
        root_node = tree_node(0)
        root_node.left, root_node.right = tree_node(1), tree_node(2)
        root_node.left.left, root_node.left.right = tree_node(3), tree_node(4)
        root_node.right.left, root_node.right.right = tree_node(5), tree_node(6)
        self.root = root_node

    def breadth_first_search(self):
        ''' 深度搜索没法像广度搜索用递归方法直接便利，采取分层存储的方法，比如第一层的值存在key为1的list，第二层存在key为2的list，最后统一打印'''
        self.data = {}
        self.print_node_value(self.root, 0)
        print(self.data)

    def print_node_value(self, node, level=0):
        level = level + 1
        if isinstance(node, tree_node):
            if "{0}".format(level) not in self.data:
                self.data["{0}".format(level)] = []
            self.data["{0}".format(level)].append(node.data)
            if node.left:
                self.print_node_value(node.left, level)
            if node.right:
                self.print_node_value(node.right, level)
        else:
            print("input parameter type is worong")


if __name__ == '__main__':
    b_tree_obj = b_tree()
    b_tree_obj.create_b_tree()
    b_tree_obj.breadth_first_search()
    print(b_tree_obj)
