 # Implement the remove node method without helper functions

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):

        left = str(self.left) if self.left else ""
        right = str(self.right) if self.right else ""

        return f"{self.data}<{left}><{right}>#"


class Tree:

    def __init__(self):
        self._root_node = None


    def insert(self, value):

        new_node = Node(value)

        if self._root_node is None:
            self._root_node = new_node
            return

        current = self._root_node

        while True:

            if value < current.data:

                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    return

                current = current.left

            else:

                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    return

                current = current.right


    def _find(self, value):

        current = self._root_node

        while current:

            if value == current.data:
                return current

            elif value < current.data:
                current = current.left

            else:
                current = current.right

        return None


    def delete_node(self, value):

        node = self._find(value)

        if node is None:
            return


        if node.left is None:

            if node.parent is None:
                self._root_node = node.right
                if node.right:
                    node.right.parent = None

            elif node == node.parent.left:
                node.parent.left = node.right
                if node.right:
                    node.right.parent = node.parent

            else:
                node.parent.right = node.right
                if node.right:
                    node.right.parent = node.parent


        elif node.right is None:

            if node.parent is None:
                self._root_node = node.left
                if node.left:
                    node.left.parent = None

            elif node == node.parent.left:
                node.parent.left = node.left
                if node.left:
                    node.left.parent = node.parent

            else:
                node.parent.right = node.left
                if node.left:
                    node.left.parent = node.parent


        else:

            successor = node.right

            while successor.left:
                successor = successor.left

            if successor.parent != node:

                if successor.right:
                    successor.right.parent = successor.parent

                if successor == successor.parent.left:
                    successor.parent.left = successor.right
                else:
                    successor.parent.right = successor.right

                successor.right = node.right
                successor.right.parent = successor

            if node.parent is None:
                self._root_node = successor
            elif node == node.parent.left:
                node.parent.left = successor
            else:
                node.parent.right = successor

            successor.parent = node.parent
            successor.left = node.left
            successor.left.parent = successor