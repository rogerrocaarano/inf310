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
        tree_array = [20, 40, 10, 30, 15, 35, 7, 26, 18, 22]
        tree = BTree(tree_array, paths=5)
        tree.insert(5)

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

    def test7(self):
        tree_array = [20, 40, 10, 30, 15, 35, 7, 26, 18, 22, 5]
        tree = BTree(tree_array, paths=5)
        tree_array = [42, 13, 46, 27, 8]
        tree.insert(tree_array)

        node0_pos0 = tree.search(10)
        node0_pos1 = tree.search(20)
        node0_pos2 = tree.search(30)
        node1_pos0 = tree.search(5)
        node1_pos1 = tree.search(7)
        node1_pos2 = tree.search(8)
        node2_pos0 = tree.search(13)
        node2_pos1 = tree.search(15)
        node2_pos2 = tree.search(18)
        node3_pos0 = tree.search(22)
        node3_pos1 = tree.search(26)
        node3_pos2 = tree.search(27)
        node4_pos0 = tree.search(35)
        node4_pos1 = tree.search(40)
        node4_pos2 = tree.search(42)
        node4_pos3 = tree.search(46)

        self.assertEqual(node0_pos0[1], 0)
        self.assertEqual(node0_pos1[1], 1)
        self.assertEqual(node0_pos2[1], 2)
        self.assertEqual(node1_pos0[1], 0)
        self.assertEqual(node1_pos1[1], 1)
        self.assertEqual(node1_pos2[1], 2)
        self.assertEqual(node2_pos0[1], 0)
        self.assertEqual(node2_pos1[1], 1)
        self.assertEqual(node2_pos2[1], 2)
        self.assertEqual(node3_pos0[1], 0)
        self.assertEqual(node3_pos1[1], 1)
        self.assertEqual(node3_pos2[1], 2)
        self.assertEqual(node4_pos0[1], 0)
        self.assertEqual(node4_pos1[1], 1)
        self.assertEqual(node4_pos2[1], 2)
        self.assertEqual(node4_pos3[1], 3)

    def test8(self):
        tree_array = [20, 40, 10, 30, 15, 35, 7, 26, 18, 22, 5]
        tree_array = tree_array + [42, 13, 46, 27, 8]
        tree = BTree(tree_array, paths=5)
        tree.insert(32)

        node0_pos0 = tree.search(10)
        node0_pos1 = tree.search(20)
        node0_pos2 = tree.search(30)
        node0_pos3 = tree.search(40)
        node1_pos0 = tree.search(5)
        node1_pos1 = tree.search(7)
        node1_pos2 = tree.search(8)
        node2_pos0 = tree.search(13)
        node2_pos1 = tree.search(15)
        node2_pos2 = tree.search(18)
        node3_pos0 = tree.search(22)
        node3_pos1 = tree.search(26)
        node3_pos2 = tree.search(27)
        node4_pos0 = tree.search(32)
        node4_pos1 = tree.search(35)
        node5_pos0 = tree.search(42)
        node5_pos1 = tree.search(46)

        self.assertEqual(node0_pos0[1], 0)
        self.assertEqual(node0_pos1[1], 1)
        self.assertEqual(node0_pos2[1], 2)
        self.assertEqual(node0_pos3[1], 3)
        self.assertEqual(node1_pos0[1], 0)
        self.assertEqual(node1_pos1[1], 1)
        self.assertEqual(node1_pos2[1], 2)
        self.assertEqual(node2_pos0[1], 0)
        self.assertEqual(node2_pos1[1], 1)
        self.assertEqual(node2_pos2[1], 2)
        self.assertEqual(node3_pos0[1], 0)
        self.assertEqual(node3_pos1[1], 1)
        self.assertEqual(node3_pos2[1], 2)
        self.assertEqual(node4_pos0[1], 0)
        self.assertEqual(node4_pos1[1], 1)
        self.assertEqual(node5_pos0[1], 0)
        self.assertEqual(node5_pos1[1], 1)

    def test9(self):
        tree_array = [20, 40, 10, 30, 15, 35, 7, 26, 18, 22, 5]
        tree_array = tree_array + [42, 13, 46, 27, 8, 32, 38, 24, 45]
        tree = BTree(tree_array, paths=5)
        tree.insert(25)

        node0_pos0 = tree.search(25)
        node1_pos0 = tree.search(10)
        node1_pos1 = tree.search(20)
        node2_pos0 = tree.search(30)
        node2_pos1 = tree.search(40)
        node3_pos0 = tree.search(5)
        node3_pos1 = tree.search(7)
        node3_pos2 = tree.search(8)
        node4_pos0 = tree.search(13)
        node4_pos1 = tree.search(15)
        node4_pos2 = tree.search(18)
        node5_pos0 = tree.search(22)
        node5_pos1 = tree.search(24)
        node6_pos0 = tree.search(26)
        node6_pos1 = tree.search(27)
        node7_pos0 = tree.search(32)
        node7_pos1 = tree.search(35)
        node7_pos2 = tree.search(38)
        node8_pos0 = tree.search(42)
        node8_pos1 = tree.search(45)
        node8_pos2 = tree.search(46)

        self.assertEqual(node0_pos0[1], 0)
        self.assertEqual(node1_pos0[1], 0)
        self.assertEqual(node1_pos1[1], 1)
        self.assertEqual(node2_pos0[1], 0)
        self.assertEqual(node2_pos1[1], 1)
        self.assertEqual(node3_pos0[1], 0)
        self.assertEqual(node3_pos1[1], 1)
        self.assertEqual(node3_pos2[1], 2)
        self.assertEqual(node4_pos0[1], 0)
        self.assertEqual(node4_pos1[1], 1)
        self.assertEqual(node4_pos2[1], 2)
        self.assertEqual(node5_pos0[1], 0)
        self.assertEqual(node5_pos1[1], 1)
        self.assertEqual(node6_pos0[1], 0)
        self.assertEqual(node6_pos1[1], 1)
        self.assertEqual(node7_pos0[1], 0)
        self.assertEqual(node7_pos1[1], 1)
        self.assertEqual(node7_pos2[1], 2)
        self.assertEqual(node8_pos0[1], 0)
        self.assertEqual(node8_pos1[1], 1)
        self.assertEqual(node8_pos2[1], 2)


if __name__ == '__main__':
    unittest.main()
