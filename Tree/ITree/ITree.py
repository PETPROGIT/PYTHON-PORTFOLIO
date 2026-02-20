from abc import ABC, abstractmethod
from ITree.ITreeNode import ITreeNode

class ITree(ABC):
    def __init__(self):
        self._root: ITreeNode = None
    
    @property
    def root(self) -> ITreeNode:
        return self._root
    
    @abstractmethod
    def insert(self, value):
        pass