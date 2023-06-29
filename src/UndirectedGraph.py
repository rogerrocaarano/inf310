from src.Graph import *


class UndirectedGraph(Graph):
    """
    An undirected graph is a graph in which edges have no orientation. The edge
    (u, v) is identical to edge (v, u).

    The implementation of this class is identical to Graph, except that
    add_link and remove_link methods are overridden to add/remove the link in
    both directions.
    """

    def __init__(self, vertex=None):
        assert vertex is None or isinstance(vertex, Vertex)
        super().__init__(vertex)

    def add_link(self, from_key, to_key, weight=0):
        super().add_link(from_key, to_key, weight)
        super().add_link(to_key, from_key, weight)

    def remove_link(self, from_key, to_key):
        super().remove_link(from_key, to_key)
        super().remove_link(to_key, from_key)
