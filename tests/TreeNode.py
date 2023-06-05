import unittest
from Trees.TreeNode import BinaryTreeNode


class TestTreeNode(unittest.TestCase):
    def test_BinaryTreeNode(self):
        # Sample node data:
        node1 = BinaryTreeNode(10)
        node2 = BinaryTreeNode(5)
        node3 = BinaryTreeNode(15)

        node1.add_child(node2)
        node1.add_child(node3)

        # Node 2 and 3 parent should be node 1
        self.assertEqual(node2.parent, node1)
        self.assertEqual(node3.parent, node1)
        # Node 1 left and right should be node 2 and 3 respectively
        self.assertEqual(node1.left, node2)
        self.assertEqual(node1.right, node3)

    def test_BinaryTreeNode_Right(self):
        # Sample node data:
        node1 = BinaryTreeNode(10)
        node2 = BinaryTreeNode(100)

        node1.add_child(node2)

        # Node 1 right should be node 2
        self.assertEqual(node1.right, node2)
        # Node 2 parent should be node 1
        self.assertEqual(node2.parent, node1)

    def test_BinaryTreeNode_Left(self):
        # Sample node data:
        node1 = BinaryTreeNode(10)
        node2 = BinaryTreeNode(5)

        node1.add_child(node2)

        # Node 1 left should be node 2
        self.assertEqual(node1.left, node2)
        # Node 2 parent should be node 1
        self.assertEqual(node2.parent, node1)

    def test_BinaryTreeNode_FullNode(self):
        # Sample node data:
        node1 = BinaryTreeNode(10)
        node2 = BinaryTreeNode(5)
        node3 = BinaryTreeNode(15)

        node1.add_child(node2)
        node1.add_child(node3)

        node4 = BinaryTreeNode(100)
        node5 = BinaryTreeNode(1)
        try:
            node1.add_child(node4)
        except Exception as e:
            self.assertEqual(e.args[0], "Right node already set")
        try:
            node1.add_child(node5)
        except Exception as e:
            self.assertEqual(e.args[0], "Left node already set")


if __name__ == '__main__':
    unittest.main()
