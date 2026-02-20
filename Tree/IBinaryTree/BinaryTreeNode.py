from IBinaryTree.IBinaryTreeNode import IBinaryTreeNode

class BinaryTreeNode(IBinaryTreeNode):
    def __init__(self, value):
        super().__init__(value)

    def addLeftChild(self, leftChild: 'BinaryTreeNode'):
        if (self._left is None):
            self._left = leftChild
        else:
            raise ValueError("The left child has already been added.")
        
    def addRightChild(self, rightChild: 'BinaryTreeNode'):
        if (self._right is None):
            self._right = rightChild
        else:
            raise ValueError("The right child has already been added.")