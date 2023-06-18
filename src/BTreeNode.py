from src.MWayTreeNode import MWayTreeNode


class BTreeNode(MWayTreeNode):
    def __init__(self,
                 values,
                 paths: int = 3,
                 parent: "MWayTreeNode" = None,
                 child_pos: int = -1
                 ):
        """
        Constructor for a BTreeNode.
        :param values:
        :param paths:
        :param parent:
        :param child_pos:
        """
        super().__init__(values, paths, parent, child_pos)

    @classmethod
    def cast(cls, node):
        """
        Casts a MWayTreeNode to a BTreeNode.
        :param node: An MWayTreeNode to cast.
        :return: A BTreeNode.
        """
        if type(node) is BTreeNode:
            node.__class__ = MWayTreeNode
        elif type(node) is MWayTreeNode:
            node.__class__ = BTreeNode
        return node

    def split_node(self):
        """
        Splits a node into two nodes, mutating the current node.
        :return: A list containing the mid-value and the new node.
        """
        split_pos = (self.__sizeof__() - 1) // 2
        mid_value = self.get_value(split_pos)
        values: list = []
        for i in range(split_pos + 1, self.__sizeof__()):
            values = values + [self.get_value(i)]
        new_node = MWayTreeNode(values, self.paths)
        data_pos = self.value_pos_to_data_pos(split_pos)
        new_data = self._data[0:data_pos]
        self._data = new_data
        return [mid_value, new_node]

    def __repr__(self):
        """
        Returns a string representation of the node.
        :return: MNode[values]
        """
        values: list = []
        for i in range(0, len(self._data) // 2):
            values = values + [self.get_value(i)]
        return f'BNode{values.__str__()}'
