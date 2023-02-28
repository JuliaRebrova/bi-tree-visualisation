from tree_drawer import TreeDrawer


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self) -> None:
        self.root = None

tree = Tree()

tree.root = Node(data = 0)
tree.root.left = Node(data = -1)
tree.root.left.left = Node(data = -2)
tree.root.left.right = Node(data = -0.5)

tree.root.right = Node(data = 1)
tree.root.right.left = Node(data = 0.5)
tree.root.right.right = Node(data = 3)

drawer = TreeDrawer(tree.root)
drawer.show_plot()