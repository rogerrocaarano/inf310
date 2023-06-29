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

    def test4(self):
        """
        Test Dijkstra's algorithm with an UndirectedGraph.
        :return:
        """
        graph = UndirectedGraph()
        graph.add_link(0, 1, 2)
        graph.add_link(0, 2, 6)
        graph.add_link(1, 3, 5)
        graph.add_link(2, 3, 8)
        graph.add_link(3, 5, 15)
        graph.add_link(3, 4, 10)
        graph.add_link(4, 5, 6)
        graph.add_link(5, 6, 6)
        graph.add_link(4, 6, 2)

        vertex_0 = graph.get_vertex(0)
        vertex_1 = graph.get_vertex(1)
        vertex_2 = graph.get_vertex(2)
        vertex_3 = graph.get_vertex(3)
        vertex_4 = graph.get_vertex(4)
        vertex_5 = graph.get_vertex(5)
        vertex_6 = graph.get_vertex(6)

        dijkstra_result = graph.dijkstra(vertex_0)
        dijkstra_expected = {
            vertex_0: [None, 0],
            vertex_1: [vertex_0, 2],
            vertex_2: [vertex_0, 6],
            vertex_3: [vertex_1, 7],
            vertex_4: [vertex_3, 17],
            vertex_5: [vertex_3, 22],
            vertex_6: [vertex_4, 19]
        }
        self.assertEqual(dijkstra_expected, dijkstra_result)

    def test5(self):
        """
        Test lower_path method.
        :return:
        """
        graph = UndirectedGraph()
        graph.add_link(0, 1, 2)
        graph.add_link(0, 2, 6)
        graph.add_link(1, 3, 5)
        graph.add_link(2, 3, 8)
        graph.add_link(3, 5, 15)
        graph.add_link(3, 4, 10)
        graph.add_link(4, 5, 6)
        graph.add_link(5, 6, 6)
        graph.add_link(4, 6, 2)

        vertex_0 = graph.get_vertex(0)
        vertex_1 = graph.get_vertex(1)
        vertex_2 = graph.get_vertex(2)
        vertex_3 = graph.get_vertex(3)
        vertex_4 = graph.get_vertex(4)
        vertex_5 = graph.get_vertex(5)
        vertex_6 = graph.get_vertex(6)

        path_result = graph.lower_cost_path(vertex_0, vertex_6)
        path_expected = {
            "path": [vertex_0, vertex_1, vertex_3, vertex_4, vertex_6],
            "cost": 19
        }

        self.assertEqual(path_expected, path_result)


if __name__ == '__main__':
    unittest.main()
