from IBinaryTree.IBinaryTree import IBinaryTree
from IBinaryTree.BinaryTreeNode import BinaryTreeNode

class BinarySearchTree(IBinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        if (self.root is None):
            self._root = BinaryTreeNode(value)
            return
        currentNode = self.root
        while (True):
            if (value < currentNode.value):
                if (currentNode.left is not None):
                    currentNode = currentNode.left
                else:
                    currentNode.addLeftChild(BinaryTreeNode(value))
                    return
            elif (value > currentNode.value):
                if (currentNode.right is not None):
                    currentNode = currentNode.right
                else:
                    currentNode.addRightChild(BinaryTreeNode(value))
                    return
            else:
                raise ValueError("The child has already been added.")