import unittest
from src.Graph import *


class TestGraph(unittest.TestCase):
    def test1(self):
        """
        Test Graph constructor.
        :return:
        """
        graph = Graph()
        self.assertEqual({}, graph.vertexes)

    def test2(self):
        """
        Test Graph constructor and add_vertex method.
        :return:
        """
        graph = Graph()
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
        Test Graph constructor with single vertex as parameter.
        :return:
        """
        vertex_a = Vertex('A')
        graph = Graph(vertex_a)

        self.assertEqual(
            {
                'A': vertex_a
            },
            graph.vertexes
        )

    def test4(self):
        """
        Test get_vertex method.
        :return:
        """
        vertex_a = Vertex('A')
        graph = Graph(vertex_a)
        self.assertEqual(vertex_a, graph.get_vertex('A'))

    def test5(self):
        """
        Test add_link method.
        :return:
        """
        vertex_a = Vertex('A')
        vertex_b = Vertex('B')
        graph = Graph(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_link('A', 'B', 10)
        self.assertEqual({vertex_b: 10}, graph.vertexes['A'].links)

    def test6(self):
        """
        Test Graph constructor with dict as parameter.
        :return:
        """
        dict_graph = {
            'A': {'B': 10, 'C': 20},
            'B': {'C': 30},
            'C': {'A': 40},
            'D': {}
        }
        graph = Graph(dict_graph)
        vertex_a = graph.get_vertex('A')
        vertex_b = graph.get_vertex('B')
        vertex_c = graph.get_vertex('C')
        vertex_d = graph.get_vertex('D')
        self.assertEqual("A links: ['B', 'C']", str(vertex_a))
        self.assertEqual("B links: ['C']", str(vertex_b))
        self.assertEqual("C links: ['A']", str(vertex_c))
        self.assertEqual("D links: []", str(vertex_d))
        self.assertEqual(
            {
                'A': vertex_a,
                'B': vertex_b,
                'C': vertex_c,
                'D': vertex_d
            },
            graph.vertexes
        )

    def test7(self):
        """
        Test remove_vertex method.
        :return:
        """
        dict_graph = {
            'A': {'B': 10, 'C': 20},
            'B': {'C': 30},
            'C': {'A': 40},
            'D': {}
        }
        graph = Graph(dict_graph)
        graph.remove_vertex('A')
        vertex_b = graph.get_vertex('B')
        vertex_c = graph.get_vertex('C')
        vertex_d = graph.get_vertex('D')
        self.assertEqual("B links: ['C']", str(vertex_b))
        self.assertEqual("C links: []", str(vertex_c))
        self.assertEqual("D links: []", str(vertex_d))
        self.assertEqual(
            {
                'B': vertex_b,
                'C': vertex_c,
                'D': vertex_d
            },
            graph.vertexes
        )


if __name__ == '__main__':
    unittest.main()
