from MWayTreeNode import MWayTreeNode


class MWaySearchTree:
    def __init__(self, max_children: int = 3):
        self.__root: MWayTreeNode = None
        self.__max_children = max_children

    @property
    def root(self):
        return self.__root

    @property
    def max_children(self):
        return self.__max_children

    def __search(self,
                 value,
                 search_node: MWayTreeNode = None,
                 pos: int = 0
                 ):
        """
        Search for a data in the tree.
        :param search_node: Node to start the search.
        :param value: Value to search for.
        :return: The node where data is found and its position in the node.
        """
        # If the tree is empty, return None
        if self.root is None:
            return None
        # If no node is passed, start from the root
        if search_node is None:
            search_node = self.root
        # If data is in the node, return the node and the position
        if value is search_node.data[pos]:
            return [search_node, pos]
        # Case 1: If data is less than the first data in the node and first
        # child is not None, search in the left child
        if value < search_node.data[pos] \
                and search_node.child[pos] is not None:
            return self.__search(value, search_node.child[pos])
        # Case 2: If data is greater than the last data in the node and last
        # child is not None, search in the right child
        if search_node.data[pos] < value < search_node.data[pos + 1] \
                and search_node.child[pos + 1] is not None:
            return self.__search(value, search_node.child[pos + 1])
        # Case 3: If data is greater than the last data in the node and last
        # child is not None, search in the right child
        if value > search_node.data[pos]:
            if search_node.data[pos + 1] is not None:
                return self.__search(value, search_node, pos + 1)
            elif search_node.child[pos + 1] is not None:
                return self.__search(value, search_node.child[pos + 1])
        # Case 4: If the values is not found, return the last node visited and
        # None as position.
        return [search_node, None]

    def insert(self, value):
        """
        Insert a data in the tree.
        :param value: Value to insert.
        :return: None
        """
        # If the tree is empty, create a root node
        if self.root is None:
            self.__root = MWayTreeNode(self.max_children)
            self.root.data = value
        else:
            # Search for the node where the data should be inserted
            node, pos = self.__search(value)
            # If the node is full, insert the data on its right child
            if node.full_node():
                new_node = MWayTreeNode(self.max_children, node.parent)
                new_node.data = value
                node.child[self.max_children] = new_node
            else:
                node.data = value

    def __insert_position(self, node: MWayTreeNode, value):
        if node.value_before_node_range(value):
            return 0
        if node.value_after_node_range(value):
            return node.count
