import unittest
from src.UndirectedGraph import *


class TestUndirectedGraph(unittest.TestCase):
    def test1(self):
        """
        Test UndirectedGraph constructor.
        :return:
        """
        graph = UndirectedGraph()
        self.assertEqual({}, graph.vertexes)

    def test2(self):
        """
        Test UndirectedGraph constructor and add_vertex method.
        :return:
        """
        graph = UndirectedGraph()
        vertex_a = Vertex('A')
        vertex_b = Vertex('B')
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        self.assertEqual(
            {
                'A': vertex_a,
                'B': vertex_b
            },
            graph.vertexes
        )

    def test3(self):
        """
        Test UndirectedGraph with 3 vertexes and links between them.
        :return:
        """
        graph = UndirectedGraph()
        vertex_a = Vertex('A')
        vertex_b = Vertex('B')
        vertex_c = Vertex('C')
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_vertex(vertex_c)
        graph.add_link('A', 'B')
        graph.add_link('B', 'C')
        graph.add_link('C', 'A')
        self.assertEqual(
            {
                'A': vertex_a,
                'B': vertex_b,
                'C': vertex_c
            },
            graph.vertexes
        )
        # Check A vertex links
        self.assertEqual(
            {
                vertex_b: 0,
                vertex_c: 0
            },
            graph.vertexes['A'].links
        )
        # Check B vertex links
        self.assertEqual(
            {
                vertex_a: 0,
                vertex_c: 0
            },
            graph.vertexes['B'].links
        )
        # Check C vertex links
        self.assertEqual(
            {
                vertex_a: 0,
                vertex_b: 0
            },
            graph.vertexes['C'].links
        )


if __name__ == '__main__':
    unittest.main()
