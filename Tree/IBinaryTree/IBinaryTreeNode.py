from abc import abstractmethod
from ITree.ITreeNode import ITreeNode

class IBinaryTreeNode(ITreeNode):
    def __init__(self, value):
        super().__init__(value)
        self._left: 'IBinaryTreeNode' = None
        self._right: 'IBinaryTreeNode' = None
    
    @property
    def left(self) -> 'IBinaryTreeNode':
        return self._left
    
    @property
    def right(self) -> 'IBinaryTreeNode':
        return self._right
    
    @abstractmethod
    def addLeftChild(self, leftChild: 'IBinaryTreeNode'):
        pass

    @abstractmethod  
    def addRightChild(self, rightChild: 'IBinaryTreeNode'):
        pass
