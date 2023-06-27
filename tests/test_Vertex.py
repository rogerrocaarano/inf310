import unittest
from src.Vertex import *


class TestVertex(unittest.TestCase):
    def test1(self):
        """
        Test Vertex constructor.
        :return:
        """
        vertex = Vertex('A')
        self.assertEqual('A', vertex.key)
        self.assertEqual({}, vertex.links)
        self.assertEqual(False, vertex.visited)

    def test2(self):
        """
        Test add_link method.
        :return:
        """
        vertex_a = Vertex('A')
        vertex_b = Vertex('B')
        vertex_a.add_link(vertex_b, 10)
        connections = vertex_a.get_connections()
        self.assertEqual({vertex_b: 10}, vertex_a.links)
        self.assertEqual([vertex_b], list(connections))

    def test3(self):
        """
        Test __contains__ method.
        :return:
        """
        vertex_a = Vertex('A')
        self.assertTrue('A' in vertex_a)
        self.assertFalse('B' in vertex_a)

    def test4(self):
        """
        Test get_weight method.
        :return:
        """
        vertex_a = Vertex('A')
        vertex_b = Vertex('B')
        vertex_a.add_link(vertex_b, 10)
        self.assertEqual(10, vertex_a.get_weight(vertex_b))


if __name__ == '__main__':
    unittest.main()
