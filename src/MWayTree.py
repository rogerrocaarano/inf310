from src.MWayTreeNode import MWayTreeNode as Node


class NWayTree:
    def __init__(self,
                 tree_array: list = None,
                 m_ways=3
                 ):
        self.__root: Node = None
        self.__m_ways = m_ways
        if tree_array is not None:
            for value in tree_array:
                self.insert(value)

    # Getter methods

    @property
    def root(self):
        return self.__root

    @property
    def m_ways(self):
        return self.__m_ways

    # Setter methods

    @root.setter
    def root(self, node: "Node"):
        self.__root = node
