from TraversalBinary.ITraversalBinary import ITraversalBinary
from IBinaryTree.IBinaryTree import IBinaryTree

class Inorder(ITraversalBinary):
    def traversalBinary(self, binaryTree: IBinaryTree):
        result = []
        if (binaryTree.root is None): return result

        stack = []
        currentNode = binaryTree.root

        while (stack or currentNode is not None):
            
            while (currentNode is not None):
                stack.append(currentNode)
                currentNode = currentNode.left
            

            currentNode = stack.pop()
            result.append(currentNode.value)

            currentNode = currentNode.right
        
        return result