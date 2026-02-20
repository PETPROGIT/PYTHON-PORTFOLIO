from abc import abstractmethod
from ITree.ITree import ITree

class IBinaryTree(ITree):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def insert(self, value):
        pass