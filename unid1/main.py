from TreeNode import TreeNode
from BinarySearchTree import BinarySearchTree

# tree_array = [18, 9, 7, 12, 2, 8, 11, 25, 23, 29, 21, 24, 31]
tree_array = [100, 50, 150, 180, 200, 10, 60, 5, 20, 80, 110, 300, 350]
tree = BinarySearchTree(tree_array)

print(tree.__str__("preorder"))
print(tree.is_balanced(tree.root))
tree.balance()

print(tree.__str__("preorder"))

print(tree.is_balanced(tree.root))
