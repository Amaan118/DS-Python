class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # Each node which is to be inserted have color Red


class RBT:
    def __init__(self):
        self.tree = Node(0)

    def single_left_rotate(self, node):
        right_node = node.right
        node.right = right_node.left

        if right_node.left != self.TNULL:
            right_node.left.parent = node

        right_node.parent = node.parent
