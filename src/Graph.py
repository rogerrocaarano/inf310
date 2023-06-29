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

    def lower_cost_path(self, from_key: Vertex, to_key: Vertex):
        """
        Get the lower cost path between two Vertexes.
        :param from_key: Starting Vertex or key of the Vertex to start from.
        :param to_key: Ending Vertex or key of the Vertex to end to.
        :return: A dict with the path and the cost.
        """
        if type(from_key) is not Vertex:
            from_key = self.get_vertex(from_key)
        if type(to_key) is not Vertex:
            to_key = self.get_vertex(to_key)

        assert from_key is not None, \
            "from_key is not in the graph"
        assert to_key is not None, \
            "to_key is not in the graph"
        assert from_key is not to_key, \
            "from_key and to_key are the same"
        assert from_key.key in self.vertexes.keys(), \
            "from_key is not in the graph"
        assert to_key.key in self.vertexes.keys(), \
            "to_key is not in the graph"

        distance = self.dijkstra(from_key)
        path: list = [to_key]
        vertex = distance[to_key][0]
        while vertex is not None:
            path.insert(0, vertex)
            vertex = distance[vertex][0]
        return {"path": path, "cost": distance[to_key][1]}

    def dijkstra(self, vertex: Vertex, distance: dict = None):
        """
        Dijkstra algorithm implementation.
        :param vertex: Source Vertex.
        :param distance: **Don't use this parameter, it's used for recursion.**
        :return: distance, a dict of Vertexes as keys and a list of
        [previous_vertex, distance] as values , where previous_vertex is None
        and distance is 0 for the head of the path.
        """
        if vertex is None:
            # When the recursion is over, reset the visited status of all the
            # Vertexes and return the distance dictionary.
            self.__reset_visited_status()
            return distance

        if distance is None:
            # Construct the distance dictionary with all the vertexes of the
            # Graph, and set the distance to inf.
            distance = {}
            for key in self.vertexes.keys():
                v = self.get_vertex(key)
                distance[v] = [None, float("inf")]
            # Set the distance to the starting vertex to 0.
            distance[vertex] = [None, 0]
        # Update the distances of the adjacent vertexes, and get the next
        # vertex to visit.
        self.__update_distances_adjacent_vertex(vertex, distance)
        next_vertex = self.__get_lower_cost_visitable_vertex(distance)
        return self.dijkstra(next_vertex, distance)

    @staticmethod
    def __update_distances_adjacent_vertex(current_vertex: Vertex,
                                           distance: dict
                                           ):
        """
        Update the distances of the adjacent vertexes of the current vertex for
        the Dijkstra algorithm.
        :param current_vertex: The current visited vertex.
        :param distance: The distance dictionary.
        :return:
        """
        for adjacent_vertex, weight in current_vertex.links.items():
            if not adjacent_vertex.visited:
                distance_current_vertex = distance[current_vertex][1]
                new_distance = distance_current_vertex + weight
                v = distance[adjacent_vertex][0]
                d = distance[adjacent_vertex][1]
                if v is None or d > new_distance:
                    distance[adjacent_vertex] = [current_vertex, new_distance]
        current_vertex.visited = True

    def __get_lower_cost_visitable_vertex(self, distance_dict: dict):
        """
        Get the lower cost vertex to visit.
        :param distance_dict: The distance dictionary.
        :return: The lower cost vertex to visit, or None if there are no more
        vertexes to visit.
        """
        lower_cost = [None, float("inf")]
        visitable_nodes = self.get_visitable_nodes()
        if len(visitable_nodes) != 0:
            for vertex in visitable_nodes:
                distance = distance_dict[vertex][1]
                if distance < lower_cost[1]:
                    lower_cost = [vertex, distance]
        return lower_cost[0]

    def get_visitable_nodes(self):
        """
        Get the list of vertexes that are not visited.
        :return: A list of vertexes that are not visited.
        """
        visitable_nodes = []
        for vertex in self.vertexes.values():
            if not vertex.visited:
                visitable_nodes.append(vertex)
        return visitable_nodes

    def __reset_visited_status(self):
        """
        Reset the visited status of all the Vertexes of the Graph.
        :return:
        """
        for vertex in self.vertexes.values():
            vertex.visited = False
