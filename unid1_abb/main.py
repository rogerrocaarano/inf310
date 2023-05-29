from binarysearchtree import TreeNode
from binarysearchtree import BinarySearchTree

tree_array = [18, 9, 7, 12, 2, 8, 11, 25, 23, 29, 21, 24, 31]
tree = BinarySearchTree()

for i in tree_array:
    tree.insert(i)

tree_list = list()
tree.pre_order(tree.root, tree_list)
print(tree_list)

tree.delete(18)
tree_list = list()
tree.pre_order(tree.root, tree_list)
print(tree_list)
