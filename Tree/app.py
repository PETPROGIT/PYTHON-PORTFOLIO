from BinaryTree.BinarySearchTree import BinarySearchTree
from TraversalBinary.TraversalBinary import TraversalBinary
from TraversalBinary.Preorder import Preorder
from TraversalBinary.Inorder import Inorder

bst = BinarySearchTree()
bst.insert(7)
bst.insert(6)
bst.insert(8)


traverser = TraversalBinary(bst, Inorder())

print(traverser.getTraversal())