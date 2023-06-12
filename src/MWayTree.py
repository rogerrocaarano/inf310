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
            self.__insert(value, self.root)

    def __insert(self, value, node: "Node"):
        """
        Insert a value into the tree, taking a node as parameter.
        :param value: Value to insert.
        :param node: Node to start searching insertion position.
        :return:
        """
        if node.in_range(value) and not node.is_full:
            try:
                node.insert_value(value)
            except NodeValueAlreadyExists:
                return
            except ValueInChildNodeRange as e:
                self.__insert(value, e.node)
            except InvalidValue:
                self.__insert_between_min_max(value, node)
            else:
                return
        if node.is_full:
            self.__insert_in_full_node(value, node)
        else:
            node.insert_value(value)

    def __insert_in_full_node(self, value, node: Node):
        """
        This method inserts a value in the tree, taking a full node as
        parameter, it creates a new node or pass the next node to try insertion
        to __insert(value, node).
        :param value: Value to insert.
        :param node: Node to start searching insertion position.
        :return:
        """
        if value < node.min:
            if node.first_pointer is None:
                Node(value, self.paths, node, 0)
            else:
                self.__insert(value, node.first_pointer)
        elif value > node.max:
            if node.last_pointer is None:
                pos = Node.value_pos_to_data_pos(
                    node.__sizeof__() - 1) + 1
                Node(value, self.paths, node, pos)
            else:
                self.__insert(value, node.last_pointer)
        else:
            self.__insert_between_min_max(value, node)

    def __insert_between_min_max(self, value, node: Node):
        """
        This method inserts a value in the tree, in between the min and max
        values of a node.
        :param value: Value to insert.
        :param node: Node to start searching insertion position.
        :return:
        """
        for i in range(0, node.__sizeof__() - 1):
            if node.get_value(i) < value < node.get_value(i + 1):
                child_pos = Node.value_pos_to_data_pos(i) + 1
                if node.data[child_pos] is None:
                    Node(value, self.paths, node, child_pos)
                else:
                    self.__insert(value, node.data[child_pos])

    def search(self, value, node: Node = None):
        """
        Searches for a value in the tree and return its node and position.
        :param value: Value to search.
        :param node:
        :return: list of [node, pos], if value not found, returns last node
        visited as node and None as pos.
        """
        if node is None:
            node = self.root
        pos = node.search(value)
        if type(pos) is Node:
            return self.search(value, pos)
        else:
            return [node, pos]
