class Vertex(object):
    """
    A vertex (also called a “node”) is a fundamental part of a graph. It can
    have a name, which we will call the “key.”. A vertex may also have
    additional information, which we will call the “payload.”

    For this implementation the payload attributes are:
    - links: A dictionary of connected vertexes.
    - visited: A boolean flag to indicate if the vertex was visited when doing
    a graph search.
    """

    def __init__(self, key):
        """
        Constructor for Vertex.
        :param key: The key for the Vertex.
        """
        self.__key = key
        self.__links = {}
        self.visited = False

    @property
    def key(self):
        """
        Getter for __key.
        :return:
        """
        return self.__key

    @property
    def links(self):
        """
        Getter for __links.
        :return:
        """
        return self.__links

    def __str__(self):
        return '{} links: {}'.format(
            self.__key,
            [x.__key for x in self.__links]
        )

    def __repr__(self):
        return self.__str__()

    def __contains__(self, key):
        return key == self.__key

    def add_link(self, linked_node: "Vertex", weight: float = 0):
        """
        Add a link to another Vertex.
        :param linked_node: The Vertex to link to.
        :param weight: The weight of the link.
        :return:
        """
        assert isinstance(linked_node, Vertex)
        self.__links[linked_node] = weight

    def remove_link(self, linked_node: "Vertex"):
        """
        Remove a link to another Vertex.
        :param linked_node: The Vertex to remove the link to.
        :return:
        """
        assert isinstance(linked_node, Vertex)
        self.__links.pop(linked_node)

    def get_connections(self):
        """
        Get the connected Vertexes.
        :return:
        """
        return self.__links.keys()

    def get_weight(self, neighbor: "Vertex"):
        """
        Get the weight of the link to a connected Vertex.
        :param neighbor:
        :return:
        """
        assert isinstance(neighbor, Vertex)
        return self.__links[neighbor]
