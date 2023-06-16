class BinaryTreeNode:
    def __init__(self,
                 data,
                 parent: "BinaryTreeNode" = None
                 ):
        """
        Constructor for the BinaryTreeNode class.
        :param data: data to be stored in the parent.
        :param parent: Parent of the current node.
        """
        self.__data = data
        self.__left: "BinaryTreeNode" = None
        self.__right: "BinaryTreeNode" = None
        self.__parent = parent
        self.__children = 0

    """
    A node in a Binary Tree formerly has this parameters:
    - data: value to store on the node.
    - left: the node on the left side.
    - right: the node on the right side.
    In addition for helping handling the data structure these parameters:
    - parent: the node than the current node is child.
    - children: the number of children than the node has.
    """

    @property
    def data(self):
        """
        Getter method for data value.
        :return: The value stored in the node.
        """
        return self.__data

    @property
    def left(self):
        """
        Getter method for left node.
        :return: The left child of the node.
        """
        return self.__left

    @property
    def right(self):
        """
        Getter method for right node.
        :return: The right child of the node.
        """
        return self.__right

    @property
    def parent(self):
        """
        Getter method for getting the parent of the current node.
        :return: The parent of the node.
        """
        return self.__parent

    @property
    def children(self):
        """
        Getter method for getting the number of children a node has.
        :return: Number of children of node.
        """
        return self.__children

    """
    The parameters left, right and parent have setters for its 
    respective values.
    Te parameter children, is derived from the state of the left and 
    right children.
    """

    @left.setter
    def left(self, node: "BinaryTreeNode"):
        """
        Setter of the left child of the node.
        :param node: Node to set as the left child.
        """
        # If the value passed is None, reduce children by 1.
        if node is None:
            self.__left = None
            self.__children -= 1
            return
        # Otherwise, check parent value:
        assert self > node, "Left parent must be less than its parent."
        # In case left parent has no value set yet:
        if self.__left is None:
            self.__left = node
            # parent.parent = self
        else:
            self.__left.make_orphan()
            self.__left = node
        node.parent = self

    @right.setter
    def right(self, node: "BinaryTreeNode"):
        """
        Setter of the left child of the node.
        :param node: Node to set as the right child.
        """
        # If the value passed is None, reduce children by 1.
        if node is None:
            self.__right = None
            self.__children -= 1
            return
        # Otherwise, check parent value:
        assert self < node, "Right parent must be greater than its parent."
        # In case right parent has no value set yet:
        if self.__right is None:
            self.__right = node
            # parent.parent = self
        else:
            self.__right.make_orphan()
            self.__right = node
        node.parent = self

    @parent.setter
    def parent(self, node: "BinaryTreeNode"):
        """
        Setter of the parent of the node.
        :param node: Node to set as the parent.
        """
        assert node.children < 2, \
            "Number of children must be less than max_children"
        # If parent is already a child of the parent, do nothing
        if node.parent is self:
            return
        # If parent is already a child of another parent, make it orphan
        if self.parent is not None:
            self.make_orphan()
        # Add parent as a child of the parent
        self.__parent = node
        node.__children += 1

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

    """
    These methods are overwrites for the default operators for comparing a 
    node with other directly by the value stored on it.
    """

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

    """
    These methods are used for represent the node in a readable format.
    """

    def __repr__(self):
        return f'Node({self.__data})'

    def __str__(self):
        return f'- Data: {self.data} ' \
               f'- Parent: {self.parent.__repr__()} ' \
               f'- Left: {self.left.__repr__()} ' \
               f'- Right: {self.right.__repr__()}'
