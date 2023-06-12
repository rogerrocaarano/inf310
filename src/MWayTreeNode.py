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
        :param child_pos: Pointer position in parent node.
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
        self.__data = [None]
        for value in values:
            self.__data += [value, None]
        self.__paths = paths
        # If parent parameter is passed, insert the node into the parent.
        if parent is None:
            self.__parent = None
        else:
            parent.insert_child(self, child_pos)

    # Getter methods

    @property
    def data(self):
        """
        Getter for data. It includes the pointers to child nodes in the even
        positions, and the values in the odd positions.
        :return: Data array of the node.
        """
        return self.__data

    @property
    def parent(self):
        """
        Getter for parent node.
        :return: Parent node.
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
        Getter for first pointer of node.
        :return: First pointer. None if there are no pointers.
        """
        return self.__data[0]

    @property
    def last_pointer(self):
        """
        Getter for last pointer of node.
        :return: Last pointer. None if there are no pointers.
        """
        return self.__data[-1]

    @property
    def min(self):
        """
        Getter for minimum value of node.
        :return: Minimum value.
        """
        return self.__data[1]

    @property
    def max(self):
        """
        Getter for maximum value of node.
        :return: Maximum value.
        """
        return self.__data[len(self.__data) - 2]

    @property
    def is_full(self):
        """
        Returns whether the node is full or not.
        :return: True if the node is full, False otherwise.
        """
        return self.__sizeof__() + 1 == self.paths

    # Methods for representing the node and its size

    def __sizeof__(self):
        """
        Returns the number of values in the node, not counting the pointers.
        :return: Number of values in the node.
        """
        return len(self.__data) // 2

    def __repr__(self):
        """
        Returns a string representation of the node.
        :return: Node[values]
        """
        values: list = []
        for i in range(0, len(self.__data) // 2):
            values = values + [self.get_value(i)]
        return f'Node{values.__str__()}'

    def in_range(self, value):
        """
        Returns whether a value is in the range of the node.
        :param value: Value to check.
        :return: True if the value is in the range, False otherwise.
        """
        return self.min <= value <= self.max

    @staticmethod
    def value_pos_to_data_pos(value_pos):
        """
        Converts a value position to a data position.
        :param value_pos: Value position.
        :return: Data position.
        """
        return value_pos * 2 + 1

    @staticmethod
    def __data_pos_to_value_pos(data_pos):
        return (data_pos - 1) // 2

    @staticmethod
    def __pointer_pos_to_data_pos(pointer_pos):
        return pointer_pos * 2

    def get_value(self, value_pos):
        """
        Returns the value in value_pos.
        :param value_pos: Position of the value.
        :return: Value in value_pos.
        """
        data_pos = self.value_pos_to_data_pos(value_pos)
        return self.__data[data_pos]

    def get_value_pos(self, value):
        """
        Searches for a value in the node.
        :param value: Value to search for.
        :return: Value position if found, None otherwise.
        """
        for i in range(0, self.__sizeof__()):
            if self.get_value(i) == value:
                return i
        return None

    def get_value_insertion_pos(self, value):
        """
        Searches for the position to insert a value, if value is in range of a
        child node, returns the child node.
        :param value: Value to insert.
        :return: A value position for inserting the value on the node, or the
        node than value is in range.
        """
        for pos in range(0, len(self.__data), 2):
            child_node: MWayTreeNode = self.__data[pos]
            if child_node is not None and child_node.in_range(value):
                return child_node

        if self.min > value:
            return 0
        elif self.max < value:
            return self.__sizeof__()
        for i in range(0, self.__sizeof__() - 1):
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
        # If data_pos is the size of the node, append the value.
        elif value_pos == self.__sizeof__():
            self.__append(value)
        # Else, insert the value in the data_pos, and shift all values after
        # data_pos inclusive to the right.
        else:
            # Convert value_pos to data_pos and insert value.
            data_pos = self.value_pos_to_data_pos(value_pos)
            self.__data = \
                self.__data[0:data_pos + 1] \
                + [value, None] \
                + self.__data[data_pos + 1:]

    def __append(self, value):
        """
        Appends a value to the node.
        :param value: Value to append.
        :return:
        """
        self.__data = self.__data + [value, None]

    def __prepend(self, value):
        """
        Prepends a value to the node.
        :param value: Value to prepend.
        :return:
        """
        self.__data = [None, value] + self.__data

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

    def insert_child(self, node: "MWayTreeNode", data_pos):
        """
        Inserts a child node into a pointer position.
        :param node: Node to insert as child.
        :param data_pos: Position to insert the child node into its parent.
        :return:
        """
        self.__data[data_pos] = node
        node.__parent = self

    def search(self, value, pos: int = 0):
        """
        Search a value in the node.
        :param value: Value to search.
        :param pos: Position to start searching.
        :return: The position where the value is, or the next node to search.
        """
        current_value = self.get_value(pos)
        data_pos = self.value_pos_to_data_pos(pos)
        if current_value == value:
            return pos
        elif pos == 0 and current_value > value:
            return self.__data[data_pos - 1]
        elif pos == self.__sizeof__() - 1 and current_value < value:
            return self.__data[data_pos + 1]
        elif current_value < value < self.get_value(pos + 1):
            return self.__data[data_pos + 1]
        else:
            return self.search(value, pos + 1)
