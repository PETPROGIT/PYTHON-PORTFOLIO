from TraversalBinary.ITraversalBinary import ITraversalBinary
from IBinaryTree.IBinaryTree import IBinaryTree
from TraversalBinary.Preorder import Preorder

class TraversalBinary:
    def __init__(self, binaryTree: IBinaryTree, traversal: ITraversalBinary = Preorder()):
        self._binaryTree = binaryTree
        self._traversal = traversal
    
    @property
    def binaryTree(self):
        return self._binaryTree
    
    @binaryTree.setter
    def binaryTree(self, binaryTree: IBinaryTree):
        self._binaryTree = binaryTree

    @property
    def traversal(self):
        return self._traversal
    
    @traversal.setter
    def traversal(self, traversal: ITraversalBinary):
        self._traversal = traversal

    def getTraversal(self, traversal: ITraversalBinary = None) -> list:
        if (traversal is None):
            return self._traversal.traversalBinary(self.binaryTree)
        else:
            return traversal.traversalBinary(self.binaryTree)