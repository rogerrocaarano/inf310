from Trees.Exceptions import *


class TreeNode:
    def __init__(self,
                 data,
                 parent: "TreeNode" = None,
                 max_children: int = 2,
                 children: list["TreeNode"] = None
                 ):
        """
        Constructor for the TreeNode class.
        :param data: data to be stored in the node.
        :param parent: parent node.
        :param max_children: maximum number of children.
        :param children: list of children nodes.
        """
        self.__data = data
        self.__parent = parent
        if children is not None:
            assert len(children) <= max_children, \
                "Number of children must be less or equal than max_children"
            self.__children = children
        else:
            self.__children = []
        self.__max_children = max_children

    # ----------------------------------------------------------------------- #
    # Getter methods
    @property
    def data(self):
        return self.__data

    @property
    def parent(self):
        return self.__parent

    @property
    def children(self):
        return self.__children

    @property
    def max_children(self):
        return self.__max_children

    # ----------------------------------------------------------------------- #
    # Setter methods
    @parent.setter
    def parent(self, node: "TreeNode"):
        assert len(self.children) < self.__max_children, \
            "Number of children must be less than max_children"
        # If node is already a child of the parent, do nothing
        if node.parent is self:
            return
        # If node is already a child of another node, make it orphan
        if node.parent is not None:
            node.make_orphan()
        # Add node as a child of the parent
        self.__children.append(node)
        self.__children.sort()
        self.__parent = node

    @children.setter
    def children(self, node: "TreeNode"):
        self.__children.append(node)
        self.__children.sort()
        node.__parent = self

    # ----------------------------------------------------------------------- #
    # Overloaded operators methods for comparing nodes
    def __repr__(self):
        return f'Node({self.__data})'

    def __eq__(self, other):
        return self.__data == other.data

    def __lt__(self, other):
        return self.__data < other.data

    def __gt__(self, other):
        return self.__data > other.data

    def __le__(self, other):
        return self.__data <= other.data

    def __ge__(self, other):
        return self.__data >= other.data

    def __ne__(self, other):
        return self.__data != other.data

    # ----------------------------------------------------------------------- #
    # Other methods

    # def add_child(self, node: "TreeNode"):
    #     """
    #     Method for adding a child to the node.
    #     :param node: node to be added as a child.
    #     """
    #     assert len(self.children) < self.__max_children, \
    #         "Number of children must be less than max_children"
    #     self.__children.append(node)
    #     self.__children.sort()

    def __str__(self):
        return f'- Data: {self.__data} ' \
               f'- Parent: {self.parent.__repr__()} ' \
               f'- Children: {self.__children}'

    def make_orphan(self):
        """
        Private method for making the node an orphan.
        """
        parent = self.__parent
        parent.__children.remove(self)
        self.__parent = None


class BinaryTreeNode(TreeNode):
    def __init__(self,
                 data,
                 parent: "BinaryTreeNode" = None):
        """
        Constructor for the BinaryTreeNode class.
        :param data: data to be stored in the node.
        :param parent: parent node.
        """
        super().__init__(data, parent, 2)
        self.__left: "BinaryTreeNode" = None
        self.__right: "BinaryTreeNode" = None

    # ----------------------------------------------------------------------- #
    # Getter methods
    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    # ----------------------------------------------------------------------- #
    # Setter methods
    @left.setter
    def left(self, node: "BinaryTreeNode"):
        if node is None:
            self.left.make_orphan()
            self.__left = None
            return
        assert self > node, \
            "Left node must be less than its parent."
        if self.left is not None:
            self.left.make_orphan()
        self.children = node
        self.__left = node

    @right.setter
    def right(self, node: "BinaryTreeNode"):
        if node is None:
            self.right.make_orphan()
            self.__right = None
            return
        assert self < node, \
            "Right node must be greater than its parent."
        if self.right is not None:
            self.right.make_orphan()
        self.children = node
        self.__right = node

    # ----------------------------------------------------------------------- #
    # Other methods
    # def add_child(self, node: "BinaryTreeNode"):
    #     if node == self:
    #         return
    #     try:
    #         if node < self:
    #             if self.left is not None:
    #                 raise LeftNodeAlreadySet
    #             else:
    #                 self.left = node
    #         else:
    #             if self.right is not None:
    #                 raise RightNodeAlreadySet
    #             else:
    #                 self.right = node
    #     except (LeftNodeAlreadySet, RightNodeAlreadySet) as e:
    #         raise e
    #     else:
    #         super().add_child(node)

    def __str__(self):
        return f'- Data: {self.data} ' \
               f'- Parent: {self.parent.__repr__()} ' \
               f'- Left: {self.left.__repr__()} ' \
               f'- Right: {self.right.__repr__()}'
