import unittest
from src.MWayTreeNode import *


class TestMWayTreeNode(unittest.TestCase):
    def test1(self):
        """
        Test node constructor.
        :return:
        """
        node = MWayTreeNode(10, 3)

        self.assertEqual([None, 10, None], node.data)
        self.assertEqual(None, node.parent)
        self.assertEqual(3, node.paths)
        self.assertEqual(None, node.first_pointer)
        self.assertEqual(None, node.last_pointer)
        self.assertEqual(10, node.min)
        self.assertEqual(10, node.max)
        self.assertEqual(False, node.is_full)
        self.assertEqual(1, node.__sizeof__())

    def test2(self):
        """
        Test inserting data to a node
        :return:
        """
        node = MWayTreeNode(10, 3)
        node.insert_value_pos(5, 0)

        self.assertEqual([None, 5, None, 10, None], node.data)
        self.assertEqual(True, node.is_full)

    def test3(self):
        """
        Test inserting data to a node
        :return:
        """
        node = MWayTreeNode(10, 3)
        node.insert_value_pos(15, 1)

        self.assertEqual([None, 10, None, 15, None], node.data)
        self.assertEqual(True, node.is_full)

    def test4(self):
        """
        Insert data to a node
        :return:
        """
        node = MWayTreeNode(10, 4)
        node.insert_value_pos(5, 0)
        node.insert_value_pos(15, 2)

        self.assertEqual([None, 5, None, 10, None, 15, None], node.data)

    def test5(self):
        """
        Insert data using the insert_value(self, value) method.
        :return:
        """
        node = MWayTreeNode(10, 4)
        node.insert_value(5)
        node.insert_value(15)

        self.assertEqual([None, 5, None, 10, None, 15, None], node.data)


if __name__ == '__main__':
    unittest.main()
