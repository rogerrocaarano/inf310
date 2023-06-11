import unittest
from src.MWayTree import *


class TestMWayTree(unittest.TestCase):
    def test1(self):
        """
        Test tree constructor.
        :return:
        """
        tree = NWayTree(m_ways=3)

        self.assertEqual(None, tree.root)
        self.assertEqual(3, tree.m_ways)

    def test2(self):
        """
        Test inserting data to a tree
        :return:
        """
        tree = NWayTree(m_ways=3)
        tree.insert(10)

        self.assertEqual(10, tree.root.data[1])
        self.assertEqual(1, tree.root.__sizeof__())

    def test3(self):
        """
        Test inserting data to a tree
        :return:
        """
        tree = NWayTree(m_ways=3)
        tree.insert(10)
        tree.insert(5)

        self.assertEqual(5, tree.root.data[1])
        self.assertEqual(10, tree.root.data[3])
        self.assertEqual(2, tree.root.__sizeof__())

    def test4(self):
        """
        Test inserting an array of data to a tree
        :return:
        """
        tree_array = [100, 50, 150, 25]
        tree = NWayTree(tree_array, m_ways=5)

        self.assertEqual(25, tree.root.get_value(0))
        self.assertEqual(50, tree.root.get_value(1))
        self.assertEqual(100, tree.root.get_value(2))
        self.assertEqual(150, tree.root.get_value(3))
        self.assertEqual(4, tree.root.__sizeof__())

    def test5(self):
        """
        Test inserting an array of data to a tree
        :return:
        """
        tree_array = [100, 50, 150, 25, 110]
        tree = NWayTree(tree_array, m_ways=4)

        self.assertEqual(50, tree.root.get_value(0))
        node_25 = tree.root.data[0]
        self.assertEqual(25, node_25.get_value(0))
        node_110 = tree.root.data[4]
        self.assertEqual(110, node_110.get_value(0))

    def test6(self):
        """
        Test inserting a more complex array of data to a tree
        :return:
        """
        tree_array = [50, 100, 150, 23, 25, 30, 55, 60, 70, 56, 170]
        tree = NWayTree(tree_array, m_ways=4)

        node_25 = tree.root.data[0]
        node_60 = tree.root.data[2]
        node_170 = tree.root.data[6]
        node_56 = node_60.data[2]

        self.assertEqual(50, tree.root.get_value(0))
        self.assertEqual(60, node_60.value(1))
        self.assertEqual(170, node_170.value(0))
        self.assertEqual(56, node_56.value(0))


if __name__ == '__main__':
    unittest.main()
