class Node:
    def __init__(self, val):
        self.data = val
        self.left =None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def _insert(self, node, val):
        newNode = Node(val)
        if val > node.data:
            if node.right == None:
                node.right = newNode
            else:
                self._insert(node.right, val)
        else:
            if node.left == None:
                node.left = newNode
            else:
                self._insert(node.left, val)

    def insert(self, val):
        newNode = Node(val)
        if self.root == None:
            self.root = newNode
        else:
            self._insert(self.root, val)


def preOrder(node):
    if node!= None:
        print(node.data)
        preOrder(node.left)
        preOrder(node.right)

def Test():
    a = BSTree()
    a.insert(10)
    a.insert(5)
    a.insert(12)
    a.insert(1)
    a.insert(3)
    a.insert(6)
    a.insert(11)
    a.insert(13)
    preOrder(a.root)

Test()


