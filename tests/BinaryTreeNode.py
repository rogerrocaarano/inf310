import unittest
from src.BinaryTreeNode import *


class TestBinaryTreeNode(unittest.TestCase):
    def test_BinaryTreeNode_case1(self):
        """
        Test for BinaryTreeNode class.
        :return:
        """
        # Sample node data:
        node1 = BinaryTreeNode(10)
        node2 = BinaryTreeNode(5)
        node3 = BinaryTreeNode(15)

        node1.left = node2
        node1.right = node3

        # Node 2 and 3 parent should be node 1
        self.assertEqual(node2.parent, node1)
        self.assertEqual(node3.parent, node1)
        # Node 1 left and right should be node 2 and 3 respectively
        self.assertEqual(node1.left, node2)
        self.assertEqual(node1.right, node3)

    def test_BinaryTreeNode_case2(self):
        """
        Test setting left node with value more than parent.
        :return:
        """
        node1 = BinaryTreeNode(10)
        node2 = BinaryTreeNode(15)

        with self.assertRaises(AssertionError):
            node1.left = node2

    def test_BinaryTreeNode_case3(self):
        """
        Test setting right node with value less than parent.
        :return:
        """
        node1 = BinaryTreeNode(10)
        node2 = BinaryTreeNode(5)

        with self.assertRaises(AssertionError):
            node1.right = node2

    def test_BinaryTreeNode_case4(self):
        """
        Test setting left node twice.
        :return:
        """
        node1 = BinaryTreeNode(10)
        node2 = BinaryTreeNode(5)
        node3 = BinaryTreeNode(1)

        node1.left = node2
        node1.left = node3

        self.assertEqual(node1.left, node3)
        self.assertEqual(node2.parent, None)
        self.assertEqual(1, node1.children)

    def test_BinaryTreeNode_case5(self):
        """
        Test setting right node twice.
        :return:
        """
        node1 = BinaryTreeNode(10)
        node2 = BinaryTreeNode(15)
        node3 = BinaryTreeNode(20)

        node1.right = node2
        node1.right = node3

        self.assertEqual(node1.right, node3)
        self.assertEqual(node2.parent, None)
        self.assertEqual(node1.children, 1)


if __name__ == '__main__':
    unittest.main()
