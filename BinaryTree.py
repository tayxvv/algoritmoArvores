from Node import Node

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertNode(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertNodeRecursive(self.root, value)

    def insertNodeRecursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insertNodeRecursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insertNodeRecursive(node.right, value)

    def printTree(self):
        if self.root is not None:
            self.printTreeRecursive(self.root, 0)

    def printTreeRecursive(self, node, level):
        if node is not None:
            self.printTreeRecursive(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.printTreeRecursive(node.left, level + 1)

    def search(self, value):
        if self.root is not None:
            return self.searchRecursive(self.root, value)
        else:
            return False

    def searchRecursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self.searchRecursive(node.left, value)
        else:
            return self.searchRecursive(node.right, value)

    def deleteNode(self, value):
        if self.root is not None:
            self.root = self.deleteNodeRecursive(self.root, value)

    def deleteNodeRecursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self.deleteNodeRecursive(node.left, value)
        elif value > node.value:
            node.right = self.deleteNodeRecursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self.findMin(node.right)

            node.value = successor.value

            node.right = self.deleteNodeRecursive(node.right, successor.value)

        return node

    def findMin(self, node):
        while node.left is not None:
            node = node.left
        return node       
    
    def destroyTree(self):
        self.destroyTreeRecursive(self.root)
        self.root = None

    def destroyTreeRecursive(self, node):
        if node:
            self.destroyTreeRecursive(node.left)
            self.destroyTreeRecursive(node.right)
            del node