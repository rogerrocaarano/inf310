import unittest
from Trees.BinarySearchTree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def test_inorder_traversal(self):
        tree_array = [100, 50, 150, 180, 200, 10, 60, 5, 20, 80, 110, 300, 350]
        tree = BinarySearchTree(tree_array)
        ordered_tree = list()
        tree.in_order(tree.root, ordered_tree)
        self.assertEqual(ordered_tree.__str__(),
                         "[5, 10, 20, 50, 60, 80, 100, 110, 150, 180, 200,"
                         " 300, 350]")

    def test_preorder_traversal(self):
        tree_array = [100, 50, 150, 180, 200, 10, 60, 5, 20, 80, 110, 300, 350]
        tree = BinarySearchTree(tree_array)
        ordered_tree = list()
        tree.pre_order(tree.root, ordered_tree)
        self.assertEqual(ordered_tree.__str__(),
                         "[100, 50, 10, 5, 20, 60, 80, 150, 110, 180, 200,"
                         " 300, 350]")

    def test_postorder_traversal(self):
        tree_array = [100, 50, 150, 180, 200, 10, 60, 5, 20, 80, 110, 300, 350]
        tree = BinarySearchTree(tree_array)
        ordered_tree = list()
        tree.post_order(tree.root, ordered_tree)
        result = [5, 20, 10, 80, 60, 50, 110, 350, 300, 200, 180, 150, 100]
        self.assertEqual(result, ordered_tree)  # Root


if __name__ == '__main__':
    unittest.main()
