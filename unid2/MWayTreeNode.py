class MWayTreeNode:

    def __init__(self, m: int = 3, parent: "MWayTreeNode" = None):
        self.__m = m
        self.__keys: list = []
        self.__children = [None] * m
        self.__parent = parent

    @property
    def m(self):
        return self.__m

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, value):
        if len(self.keys) == self.m - 1:
            raise Exception("Node is full")
        self.__keys.append(value)
        self.__keys.sort()

    def in_node_range(self, value):
        if self.keys[0] <= value <= self.keys[len(self.keys) - 1]:
            return True
