class BinTreeNode():
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class binaryTree():

    def __init__(self,rootid):
        self.left=None
        self.right=None
        self.rootid=rootid

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def getNodeValue(self,value):
        self.rootid=value

    def insertLeft(self,newNode):
        if self.left==None:
            self.left=binaryTree(newNode)
        else:
            tree=binaryTree(newNode)
            self.left=tree
            tree.left=self.left

    def insertRight(self,newNode):
        if self.right==None:
            self.right=binaryTree(newNode)
        else:
            tree=binaryTree(newNode)
            self.right=tree
            tree.right=self.right

    def printTree(tree):
        if self.left==None:
            printTree(tree.getLeftChild)
            print(tree.getNodeValue)
            printTree(tree.getRightChild)

    def preorderTrav(subtree):
        if subtree is not None:
            print(subtree.data)
            preorderTrav(subtree.left)
            preorderTrav(subtree.right)

    def inorderTrav(subtree):
        if subtree is not None:
            inorderTrav(subtree.left)
            print(subtree.data)
            inorderTrav(subtree.right)

    def postorderTrav(subtree):
        if subtree is not None:
            postorderTrav(subtree.left)
            postorderTrav(subtree.right)
            print(subtree.data)

            
tree=binaryTree(50)
tree.insertRight(10)
tree.insertLeft(15)
tree.insertLeft(8)

print(printTree(tree))

































    
