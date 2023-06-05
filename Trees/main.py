from BinarySearchTree import BinarySearchTree

tree_array = [100, 50, 150, 180, 200, 10, 60, 5, 20, 80, 110, 300, 350]
tree = BinarySearchTree(tree_array)

# tree = BinarySearchTree()
# tree.insert(100)
# tree.insert(50)
# tree.insert(10)

print(tree.__str__("inorder"))
