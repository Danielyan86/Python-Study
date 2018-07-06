class Node:
    def __init__(self, value=0, *nodes):
        self.value = 0
        att_value = 'A'
        if nodes:
            for node, weight in nodes:
                print(node, weight)
                setattr(self, att_value, node)
                att_value = chr(ord(att_value) + 1)
                node.value = self.value + weight


if __name__ == '__main__':
    end_node = Node()
    a_node = Node(0, end_node)
    b_node = Node(0, (a_node, 3), (end_node, 5))
    root_node = Node(0, (a_node, 6), (b_node, 2))
    print(root_node)
