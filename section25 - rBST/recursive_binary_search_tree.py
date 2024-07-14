class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class rBST:  # in each node, n.left is smaller than n.value and n.right is bigger than n.value
    def __init__(self):
        self.root = None
        self.height = 0

    def __r_contains(self, c_node: Node, value: int):
        if not c_node:
            return False
        else:
            if c_node.value == value:
                return True

            if c_node.value > value:
                return self.__r_contains(c_node.left, value)
            else:  # only left > condition, equal is contain in the above code
                return self.__r_contains(c_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, c_node: Node, value: int):
        if not c_node:
            return Node(value)
        else:
            if c_node.value > value:
                c_node.left = self.__r_insert(c_node.left, value)
            elif c_node.value < value:
                c_node.right = self.__r_insert(c_node.right, value)

            return c_node

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


    def __delete_node(self, c_node: Node, value: int):
        if not c_node:
            return None

        if value < c_node.value:
            c_node.left = self.__delete_node(c_node.left, value)
        elif value > c_node.value:
            c_node.right = self.__delete_node(c_node.right, value)
        else:
            """
            There are 4 conditions:
            1. delete a leaf node
            2. delete a node with one child on the left
            3. delete a node with one child on the right
            4. delete a node with two children
            """
            if not c_node.left and not c_node.right:
                return None
            elif not c_node.left:
                c_node = c_node.right
            elif not c_node.right:
                c_node = c_node.left
            else:
                c_node.value = self.min_value(c_node.right)
                c_node.right = self.__delete_node(c_node.right, c_node.value)  # delete the node with the min value
        return c_node

    def delete_node(self, value):
        return self.__delete_node(self.root, value)

    def min_value(self, c_node: Node):
        while c_node.left:
            c_node = c_node.left
        return c_node.value
