from src.Vertex import *


class Graph(object):
    """
    A graph data structure consists of a finite (and possibly mutable) set of
    vertices (also called nodes or points), together with a set of unordered
    pairs of these vertices for an undirected graph or a set of ordered pairs
    for a directed graph. These pairs are known as edges (also called links
    or lines), and for a directed graph are also known as edges but also
    sometimes arrows or arcs. The vertices may be part of the graph structure,
    or may be external entities represented by integer indices or references.
    A graph data structure may also associate to each edge some edge value,
    such as a symbolic label or a numeric attribute (cost, capacity, length,
    etc.).
    """

    def __init__(self, vertexes=None):
        """
        Constructor for Graph.
        :param vertexes: A dict of Vertexes, a Vertex or None.
        """
        if vertexes is None:
            self.vertexes = {}
        elif type(vertexes) is Vertex:
            self.vertexes = {vertexes.key: vertexes}
        elif type(vertexes) is dict:
            """
            vertexes is received as a representation of a dict of Vertexes
            in the form of:
            {
                key: { destination_key: weight, destination_key: weight, ... },
                key: { destination_key: weight, destination_key: weight, ... },
                ...
            }
            """
            # Create an empty dict for storing graph data
            self.vertexes = {}
            # Instantiate Vertexes from keys
            for key in vertexes.keys():
                vertex = Vertex(key)
                self.add_vertex(vertex)
            for key, value in vertexes.items():
                if value != {}:
                    for destination, weight in value.items():
                        self.add_link(key, destination, weight)
        else:
            raise TypeError("vertexes must be a dict or Vertex")

    def __str__(self):
        return str(self.vertexes.keys())

    def __repr__(self):
        return self.__str__()

    def __contains__(self, key):
        if self.get_vertex(key) is None:
            return False
        return True

    def __iter__(self):
        return iter(self.vertexes.values())

    def get_vertex(self, key):
        """
        Get a Vertex by key.
        :param key: The key of the Vertex to get.
        :return: The Vertex if found, None otherwise.
        """
        try:
            return self.vertexes[key]
        except KeyError:
            return None

    def add_vertex(self, vertex: Vertex):
        self.vertexes[vertex.key] = vertex

    def remove_vertex(self, key):
        """
        Remove a Vertex from the graph.
        :param key: The key of the Vertex to remove.
        :return:
        """
        # Get the Vertex to remove
        vertex = self.get_vertex(key)
        # Remove all links to the Vertex
        for v in self.vertexes:
            if vertex in self.vertexes[v].links:
                self.vertexes[v].remove_link(vertex)
        # Remove the Vertex from the graph
        self.vertexes.pop(key)
        del vertex

    def add_link(self, from_key, to_key, weight=0):
        """
        Add a link between two Vertexes given their keys as parameters.
        :param from_key: key of the Vertex to link from.
        :param to_key: key of the Vertex to link to.
        :param weight: The weight of the link.
        :return:
        """
        # If from or to keys are not in the graph, add them
        if from_key not in self:
            self.add_vertex(Vertex(from_key))
        if to_key not in self:
            self.add_vertex(Vertex(to_key))
        # get the Vertexes of the from and to keys
        from_vertex = self.get_vertex(from_key)
        to_vertex = self.get_vertex(to_key)
        # add the link
        from_vertex.add_link(to_vertex, weight)

    def remove_link(self, from_key, to_key):
        """
        Remove a link between two Vertexes given their keys as parameters.
        :param from_key: key of the Vertex to link from.
        :param to_key: key of the Vertex to link to.
        :return:
        """
        # get the Vertexes of the from and to keys
        from_vertex: Vertex = self.get_vertex(from_key)
        to_vertex: Vertex = self.get_vertex(to_key)
        # remove the link
        from_vertex.remove_link(to_vertex)

    def get_vertices(self):
        return self.vertexes.keys()
