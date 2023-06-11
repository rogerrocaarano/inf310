from src.MWayTreeNode import MWayTreeNode as Node
from src.Exceptions import *


class NWayTree:
    def __init__(self,
                 tree_array: list = None,
                 paths=3
                 ):
        """
        Constructor for NWayTree.
        :param tree_array: (Optional) Array of values to insert into the tree.
        :param paths: Number of paths the tree can have (Default 3).
        """
        # Set the root to None, and the paths to the number of paths.
        self.__root: Node = None
        self.__paths = paths
        # If tree_array parameter is passed, insert the values into the tree.
        if tree_array is not None:
            for value in tree_array:
                self.insert(value)

    # Getter methods

    @property
    def root(self):
        """
        Getter for root node.
        :return: Root node.
        """
        return self.__root

    @property
    def paths(self):
        """
        Getter for number of paths.
        :return: Number of paths.
        """
        return self.__paths

    # Setter methods

    @root.setter
    def root(self, node: "Node"):
        """
        Setter for root node.
        :param node: Node to set as root.
        :return: None.
        """
        self.__root = node

    def insert(self, value):
        """
        Insert a value into the tree.
        :param value: Value to insert.
        :return: None.
        """
        # If the root is None, create a new root.
        if self.root is None:
            self.root = Node(value, self.paths)
        # If the root is not None:
        else:
            self.__insert(value, self.root, None)

    def __insert(self, value, node: "Node"):
        if node.in_range(value):
            try:
                node.insert_value(value)
            except NodeValueAlreadyExists:
                return
            except ValueInChildNodeRange as e:
                self.__insert(value, e.node)
            else:
                return
        else:
            if node.is_full:
                if value < node.min:
                    Node(value, self.paths, node, node.first_pointer)
                elif value > node.max:
                    Node(value, self.paths, node, node.last_pointer)
                else:
                    for i in range(0, node.__sizeof__() - 1):
                        if node.get_value(i) < value < node.get_value(i + 1):
                            child_pos = Node.value_pos_to_data_pos(i) + 1
                            Node(value, self.paths, node, child_pos)
            else:
                node.insert_value(value)
