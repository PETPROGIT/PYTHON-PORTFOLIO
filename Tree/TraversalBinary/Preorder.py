from TraversalBinary.ITraversalBinary import ITraversalBinary
from IBinaryTree.IBinaryTree import IBinaryTree

class Preorder(ITraversalBinary):
    def traversalBinary(self, binaryTree: IBinaryTree) -> list:
        result = []
        if (binaryTree.root is None): return result

        stack = [binaryTree.root]
        while (stack):
            currentNode = stack.pop()
            result.append(currentNode.value)
            if (currentNode.right is not None): stack.append(currentNode.right)
            if (currentNode.left is not None): stack.append(currentNode.left)

        return result