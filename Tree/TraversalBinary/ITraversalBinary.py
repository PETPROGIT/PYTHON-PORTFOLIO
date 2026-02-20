from abc import ABC, abstractmethod
from IBinaryTree.IBinaryTree import IBinaryTree

class ITraversalBinary(ABC):
    @abstractmethod
    def traversalBinary(self, binaryTree: IBinaryTree) -> list:
        pass