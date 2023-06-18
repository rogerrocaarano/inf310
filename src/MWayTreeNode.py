from src import Exceptions


class MWayTreeNode:
    def __init__(self,
                 values,
                 paths: int = 3,
                 parent: "MWayTreeNode" = None,
                 child_pos: int = -1
                 ):
        """
        Constructor for MWayTreeNode.
        :param values: Values to insert into the node on creation.
        :param paths: Number of paths the node can have.
        :param parent: Parent node.
        :param child_pos: Pointer position on the parent node.
        """
        # Values must be a list, containing values to insert into the node
        # and the length of values list must be less than paths.
        if type(values) is not list:
            values = [values]
        assert len(values) < paths, \
            "Number of values must be less than paths."
        # The data structure will be a list, where the pointers to child nodes
        # will be in the even positions, and the values will be in the odd
        # positions.
        self._data = [None]
        for value in values:
            self._data += [value, None]
        self.__paths = paths
        # If parent parameter is passed, insert the parent into the node.
        if parent is None:
            self.__parent = None
        else:
            parent.insert_child(self, child_pos)

    """
    An m-way tree node is a node that can have up to m children.
    - The node contains values and pointers to child nodes.
    - The values are sorted in ascending order.
    For this implementation, the values will be stored in a list, where the
    pointers to child nodes will be in the even positions, and the values will
    be in the odd positions.        
    """

    @property
    def data(self):
        """
        Getter for data. It includes the pointers to child nodes in the even
        positions, and the values in the odd positions.
        :return: Data array of the parent.
        """
        return self._data

    @property
    def parent(self):
        """
        Getter for parent of the current node.
        :return: Parent of the node.
        """
        return self.__parent

    @property
    def paths(self):
        """
        Getter for number of paths.
        :return: Number of paths.
        """
        return self.__paths

    @property
    def first_pointer(self):
        """
        Getter for first pointer of the node.
        :return: First pointer. None if there isn't a node referenced.
        """
        return self._data[0]

    @property
    def last_pointer(self):
        """
        Getter for last pointer of the node.
        :return: Last pointer. None if there isn't a node referenced.
        """
        return self._data[-1]

    @property
    def min(self):
        """
        Getter for minimum value of the node.
        :return: Minimum value.
        """
        return self._data[1]

    @property
    def max(self):
        """
        Getter for maximum value of the node.
        :return: Maximum value.
        """
        return self._data[len(self._data) - 2]

    @property
    def is_full(self):
        """
        Returns whether the node is full or not.
        :return: True if the node is full, False otherwise.
        """
        return self.__sizeof__() + 1 == self.paths

    def __sizeof__(self):
        """
        Returns the number of values in the node, not counting the pointers.
        :return: Number of values in the node.
        """
        return len(self._data) // 2

    def __repr__(self):
        """
        Returns a string representation of the node.
        :return: MNode[values]
        """
        values: list = []
        for i in range(0, len(self._data) // 2):
            values = values + [self.get_value(i)]
        return f'MNode{values.__str__()}'

    def in_range(self, value):
        """
        Returns whether a value is in the range of the node.
        :param value: Value to check.
        :return: True if the value is in the range, False otherwise.
        """
        return self.min <= value <= self.max

    """
    Since the implementation of the m-way tree is based on a list, the
    positions of the values are important.
    These methods provides a way to convert a value position to a data position
    and getters for the values in the node and the position of a value.
    """

    @staticmethod
    def value_pos_to_data_pos(value_pos):
        """
        Converts a value position to a data position.
        :param value_pos: Value position.
        :return: Data position.
        """
        return value_pos * 2 + 1

    def get_value(self, value_pos):
        """
        Returns the value in value_pos.
        :param value_pos: Position of the value.
        :return: Value in value_pos.
        """
        data_pos = self.value_pos_to_data_pos(value_pos)
        return self._data[data_pos]

    def get_value_pos(self, value):
        """
        Searches for a value in the parent.
        :param value: Value to search for.
        :return: Value position if found, None otherwise.
        """
        for i in range(0, self.__sizeof__()):
            if self.get_value(i) == value:
                return i
        return None

    """
    The following actions should be performed by a node:
    - Insert a value.
    - Delete a value.
    - Search a value.
    - Insert a child node.
    """

    def insert_value(self, value):
        """
        Inserts a value in the node.
        :param value: Value to insert.
        :return:
        """
        # search the value in the node.
        if self.get_value_pos(value) is not None:
            raise Exceptions.NodeValueAlreadyExists
        # search the position to insert the value.
        value_pos = self.get_value_insertion_pos(value)
        if type(value_pos) is MWayTreeNode:
            raise Exceptions.ValueInChildNodeRange(value_pos)
        elif value_pos is None:
            raise Exceptions.InvalidValue
        else:
            self.insert_value_pos(value, value_pos)

    def delete(self, index):
        """
        Removes the value at the index position passed. It removes the value
        in the data structure and the next pointer in the process.
        :param index: Position in the node to remove.
        :return: The pointer deleted with value.
        """
        data_pos = self.value_pos_to_data_pos(index)
        pointer = self.data[data_pos + 1]
        self._data = self.data[0:data_pos] + self.data[data_pos + 2:]
        return pointer

    def search(self, value, pos: int = 0):
        """
        Search a value in the node.
        :param value: Value to search.
        :param pos: Position to start searching.
        :return: The position where the value is, or the next parent to search.
        """
        current_value = self.get_value(pos)
        data_pos = self.value_pos_to_data_pos(pos)
        if current_value == value:
            return pos
        elif pos == 0 and current_value > value:
            return self._data[data_pos - 1]
        elif pos == self.__sizeof__() - 1 and current_value < value:
            return self._data[data_pos + 1]
        elif current_value < value < self.get_value(pos + 1):
            return self._data[data_pos + 1]
        else:
            return self.search(value, pos + 1)

    def insert_child(self, node: "MWayTreeNode", data_pos):
        """
        Inserts a child node into a pointer position.
        :param node: BNode to insert as child.
        :param data_pos: Position to insert the child node into its parent.
        :return:
        """
        self._data[data_pos] = node
        node.__parent = self

    """
    These methods help to insert a value in the node.
    """

    def get_value_insertion_pos(self, value):
        """
        Searches for the position to insert a value, if value is in range of a
        child node, returns the child node.
        :param value: Value to insert.
        :return: A value position for inserting the value on the node, or the
        node than value is in range.
        """
        for pos in range(0, len(self._data), 2):
            child_node: MWayTreeNode = self._data[pos]
            if child_node is not None and child_node.in_range(value):
                return child_node

        if self.min > value:
            return 0
        elif self.max < value:
            return self.__sizeof__()
        for i in range(1, self.__sizeof__()):
            if self.get_value(i) > value:
                return i

    def insert_value_pos(self, value, value_pos):
        """
        Inserts a value in value_pos.
        :param value: Value to insert.
        :param value_pos: Position to insert the value.
        :return:
        """
        # Parameter validation:
        assert not self.is_full
        assert value_pos <= self.__sizeof__()
        # If value_pos is 0, prepend the value.
        if value_pos == 0:
            self.__prepend(value)
        # If data_pos is the size of the parent, append the value.
        elif value_pos == self.__sizeof__():
            self.__append(value)
        # Else, insert the value in the data_pos, and shift all values after
        # data_pos inclusive to the right.
        else:
            # Convert value_pos to data_pos and insert value.
            data_pos = self.value_pos_to_data_pos(value_pos)
            data_pre_pos = self._data[0:data_pos]
            data_insert = [value, None]
            data_post_pos = self._data[data_pos:]
            self._data = data_pre_pos + data_insert + data_post_pos

    def __append(self, value):
        """
        Appends a value to the node.
        :param value: Value to append.
        :return:
        """
        self._data = self._data + [value, None]

    def __prepend(self, value):
        """
        Prepends a value to the node.
        :param value: Value to prepend.
        :return:
        """
        self._data = [None, value] + self._data
