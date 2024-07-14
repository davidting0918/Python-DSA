class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
        else:
            temp = self.root
            while True:
                if value == temp.value:
                    return False

                elif value < temp.value:
                    if not temp.left:
                        temp.left = node
                        break
                    temp = temp.left

                else:
                    if not temp.right:
                        temp.right = node
                        break
                    temp = temp.right

        return True

    def contains(self, value):
        if not self.root:
            return False

        else:
            temp = self.root
            while temp:
                if value > temp.value:
                    temp = temp.right
                elif value < temp.value:
                    temp = temp.left
                else:
                    return True

            return False

    def bfs(self):  # Breadth First Search
        c_node = self.root
        queues = []
        values = []

        queues.append(c_node)

        while len(queues) > 0:
            c_node = queues.pop(0)  # First in first out
            values.append(c_node.value)

            if c_node.left:
                queues.append(c_node.left)

            if c_node.right:
                queues.append(c_node.right)

        return values

    def dfs_pre_order(self):  # Depth First Search preorder
        values = []

        def traverse(c_node: Node):
            values.append(c_node.value)

            if c_node.left:
                traverse(c_node.left)
            if c_node.right:
                traverse(c_node.right)
        traverse(self.root)

        return values

    def dfs_post_order(self):  # Depth First Search post order
        values = []

        def traverse(c_node: Node):
            if c_node.left:
                traverse(c_node.left)

            if c_node.right:
                traverse(c_node.right)
            values.append(c_node.value)

        traverse(self.root)
        return values

    def dfs_in_order(self):  # Depth First Search post order
        values = []

        def traverse(c_node: Node):
            if c_node.left:
                traverse(c_node.left)
            values.append(c_node.value)
            if c_node.right:
                traverse(c_node.right)
        traverse(self.root)
        return values