import unittest
from src.BTree import BTree


class TestBTree(unittest.TestCase):
    def test1(self):
        """
        Test tree constructor.
        :return:
        """
        tree = BTree(paths=5)

        self.assertEqual(None, tree.root)
        self.assertEqual(5, tree.paths)

    def test2(self):
        tree_array = [10, 20, 30, 40]
        tree = BTree(tree_array, paths=5)

        self.assertEqual(tree.root.data[1], 10)
        self.assertEqual(tree.root.data[3], 20)
        self.assertEqual(tree.root.data[5], 30)
        self.assertEqual(tree.root.data[7], 40)
        self.assertEqual(tree.root.__sizeof__(), 4)

    def test3(self):
        tree_array = [10, 20, 30, 40, 15]
        tree = BTree(tree_array, paths=5)

        node1 = tree.root
        node2 = node1.data[0]
        node3 = node1.data[2]

        self.assertEqual(node1.data[1], 20)
        self.assertEqual(node2.data[1], 10)
        self.assertEqual(node2.data[3], 15)
        self.assertEqual(node3.data[1], 30)
        self.assertEqual(node3.data[3], 40)

    def test4(self):
        tree_array = [20, 40, 10, 30, 15, 35, 7, 26, 18]
        tree = BTree(tree_array, paths=5)

        node0_pos0 = tree.search(20)
        node1_pos0 = tree.search(7)
        node1_pos2 = tree.search(15)
        node1_pos3 = tree.search(18)
        node2_pos0 = tree.search(26)
        node2_pos1 = tree.search(30)
        node2_pos3 = tree.search(40)

        self.assertEqual(node0_pos0[1], 0)
        self.assertEqual(node1_pos0[1], 0)
        self.assertEqual(node1_pos2[1], 2)
        self.assertEqual(node1_pos3[1], 3)
        self.assertEqual(node2_pos0[1], 0)
        self.assertEqual(node2_pos1[1], 1)
        self.assertEqual(node2_pos3[1], 3)

    def test5(self):
        tree_array = [20, 40, 10, 30, 15, 35, 7, 26, 18, 22]
        tree = BTree(tree_array, paths=5)

        node0_pos0 = tree.search(20)
        node1_pos0 = tree.search(7)
        node1_pos1 = tree.search(10)
        node1_pos2 = tree.search(15)
        node1_pos3 = tree.search(18)
        node2_pos0 = tree.search(22)
        node2_pos1 = tree.search(26)
        node3_pos0 = tree.search(35)
        node3_pos1 = tree.search(40)

        self.assertEqual(node0_pos0[1], 0)
        self.assertEqual(node1_pos0[1], 0)
        self.assertEqual(node1_pos1[1], 1)
        self.assertEqual(node1_pos2[1], 2)
        self.assertEqual(node1_pos3[1], 3)
        self.assertEqual(node2_pos0[1], 0)
        self.assertEqual(node2_pos1[1], 1)
        self.assertEqual(node3_pos0[1], 0)
        self.assertEqual(node3_pos1[1], 1)

    def test6(self):
        tree_array = [20, 40, 10, 30, 15, 35, 7, 26, 18, 22, 5]
        tree = BTree(tree_array, paths=5)

        node0_pos0 = tree.search(10)
        node0_pos1 = tree.search(20)
        node0_pos2 = tree.search(30)
        node1_pos0 = tree.search(5)
        node1_pos1 = tree.search(7)
        node2_pos0 = tree.search(15)
        node2_pos1 = tree.search(18)
        node3_pos0 = tree.search(22)
        node3_pos1 = tree.search(26)
        node4_pos0 = tree.search(35)
        node4_pos1 = tree.search(40)

        self.assertEqual(node0_pos0[1], 0)
        self.assertEqual(node0_pos1[1], 1)
        self.assertEqual(node0_pos2[1], 2)
        self.assertEqual(node1_pos0[1], 0)
        self.assertEqual(node1_pos1[1], 1)
        self.assertEqual(node2_pos0[1], 0)
        self.assertEqual(node2_pos1[1], 1)
        self.assertEqual(node3_pos0[1], 0)
        self.assertEqual(node3_pos1[1], 1)
        self.assertEqual(node4_pos0[1], 0)
        self.assertEqual(node4_pos1[1], 1)


if __name__ == '__main__':
    unittest.main()
