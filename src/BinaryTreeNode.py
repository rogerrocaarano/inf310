class BinaryTreeNode:
    def __init__(self,
                 data,
                 parent: "BinaryTreeNode" = None):
        """
        Constructor for the BinaryTreeNode class.
        :param data: data to be stored in the node.
        :param parent: parent node.
        """
        self.__data = data
        self.__left: "BinaryTreeNode" = None
        self.__right: "BinaryTreeNode" = None
        self.__parent = parent
        self.__children = 0

    # ----------------------------------------------------------------------- #
    # Getter methods

    @property
    def data(self):
        return self.__data

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def parent(self):
        return self.__parent

    @property
    def children(self):
        return self.__children

    # ----------------------------------------------------------------------- #
    # Setter methods
    @left.setter
    def left(self, node: "BinaryTreeNode"):
        # If the value passed is None, reduce children by 1.
        if node is None:
            self.__left = None
            self.__children -= 1
            return
        # Otherwise, check node value:
        assert self > node, "Left node must be less than its parent."
        # In case left node has no value set yet:
        if self.__left is None:
            self.__left = node
            # node.parent = self
        else:
            self.__left.make_orphan()
            self.__left = node
        node.parent = self

    @right.setter
    def right(self, node: "BinaryTreeNode"):
        # If the value passed is None, reduce children by 1.
        if node is None:
            self.__right = None
            self.__children -= 1
            return
        # Otherwise, check node value:
        assert self < node, "Right node must be greater than its parent."
        # In case right node has no value set yet:
        if self.__right is None:
            self.__right = node
            # node.parent = self
        else:
            self.__right.make_orphan()
            self.__right = node
        node.parent = self

    @parent.setter
    def parent(self, node: "BinaryTreeNode"):
        assert node.children < 2, \
            "Number of children must be less than max_children"
        # If node is already a child of the parent, do nothing
        if node.parent is self:
            return
        # If node is already a child of another node, make it orphan
        if self.parent is not None:
            self.make_orphan()
        # Add node as a child of the parent
        self.__parent = node
        node.__children += 1

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

    def make_orphan(self):
        """
        Method for making the node an orphan.
        """
        if self.parent.__left is self:
            self.parent.__left = None
        else:
            self.parent.__right = None
        self.parent.__children -= 1
        self.__parent = None

    def __str__(self):
        return f'- Data: {self.data} ' \
               f'- Parent: {self.parent.__repr__()} ' \
               f'- Left: {self.left.__repr__()} ' \
               f'- Right: {self.right.__repr__()}'
