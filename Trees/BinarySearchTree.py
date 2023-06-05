from Tree import Tree
from TreeNode import BinaryTreeNode
from Exceptions import *


class BinarySearchTree(Tree):
    def __init__(self, tree_array: list = None):
        super().__init__()
        if tree_array is not None:
            for value in tree_array:
                self.insert(value)

    # ----------------------------------------------------------------------- #
    # Utility methods

    def __str__(self, traversal_type: str = "inorder"):
        """
        Function for getting a string representation of the tree using the
        specified traversal type.
        :param traversal_type: Choose between inorder, preorder or postorder.
        :return: A string representation of the tree.
        """
        tree_list = list()  # List for storing the tree nodes

        # Pass the list to the traversal method to fill it
        if traversal_type == "inorder":
            self.__in_order(self.root, tree_list)
        elif traversal_type == "preorder":
            self.__pre_order(self.root, tree_list)
        elif traversal_type == "postorder":
            self.__post_order(self.root, tree_list)
        else:
            return "Invalid traversal type."

        # Return the list as a string
        output = tree_list.__str__()
        output = output + f"\nTree deep: {self.deep}"
        return output

    @staticmethod
    def __is_leaf(node: "BinaryTreeNode"):
        """
        Private method for checking if a node is a leaf.
        :param node: Node to be checked.
        :return: True if the node is a leaf, False otherwise.
        """
        return node.left is None and node.right is None

    @staticmethod
    def __has_one_child(node: "BinaryTreeNode"):
        """
        Private method for checking if a node has one child.
        :param node: Node to be checked.
        :return: True if the node has one child, False otherwise.
        """
        return node.left is None or node.right is None

    @staticmethod
    def __higher_from_left(root: "BinaryTreeNode"):
        """
        Private method for getting the highest node in the left subtree.
        :param root: Root of the subtree.
        :return: Highest node in the left subtree.
        """
        if root.left is None:
            return root

        higher = root.left
        while higher.right is not None:
            higher = higher.right
        return higher

    @staticmethod
    def __lower_from_right(root: "BinaryTreeNode"):
        """
        Private method for getting the lowest node in the right subtree.
        :param root: Root of the subtree.
        :return: Lowest node in the right subtree.
        """
        if root.right is None:
            return root

        lower = root.right
        while lower.left is not None:
            lower = lower.left
        return lower

    # ----------------------------------------------------------------------- #
    # Searching

    def search(self, value):
        """
        Public method for searching a node in the tree.
        :param value: Value to be searched.
        :return: True if the value is found, False otherwise.
        """
        return self.__search(self.root, value) is not None

    def __search(self, root: "BinaryTreeNode", value):
        """
        Private method for searching a node in the tree.
        :param root: Starting node for the search.
        :param value: Value to be searched.
        :return: Node with the data searched or None if not found.
        """
        # Case 1: Empty tree
        if root.data is None:
            return None
        # Case 2: Value found
        if root.data == value:
            return root
        # Case 3: recursive search
        if value < root.data:
            return self.__search(root.left, value)
        else:
            return self.__search(root.right, value)

    # ----------------------------------------------------------------------- #
    # Insertion

    def insert(self, value):
        """
        Public method for inserting a node in the tree.
        :param value: Value to be inserted.
        """
        node = BinaryTreeNode(value)
        # Case 1: Empty tree
        if self.root is None:
            self.root = node
        # Case 2: Non-empty tree
        else:
            self.__insert(self.root, node)

    def __insert(self, root: "BinaryTreeNode", node: "BinaryTreeNode"):
        """
        Private method for inserting a node in the tree.
        :param root: Starting node for the insertion.
        :param node: Node to be inserted.
        """
        # Case 1: data already in the tree
        if root == node:
            return
        # Case 2: recursive insertion
        try:
            root.add_child(node)

        except LeftNodeAlreadySet:
            self.__insert(root.left, node)
        except RightNodeAlreadySet:
            self.__insert(root.right, node)

    def delete(self, value):
        node = self.__search(self.root, value)
        # Case 1: Value not found
        if node is None:
            return
        # Case 2: Node is a leaf
        if len(node.children) == 0:
            self.__delete_leaf_node(node)
        elif len(node.children) == 1:
            self.__delete_one_child_node(node)
        # Case 4: Node has two children
        else:
            pass

    def __delete_leaf_node(self, node: "BinaryTreeNode"):
        """
        Private method for deleting a leaf node.
        :param node: Node to be deleted.
        """
        # Case 1: Node is the root
        if node is self.root:
            self.root = None

        if node.parent.left is node:
            node.parent.left = None
        else:
            node.parent.right = None

    def __delete_one_child_node(self, node: "BinaryTreeNode"):
        """
        Private method for deleting a node with one child.
        :param node: Node to be deleted.
        """
        # Case 1: Node is the root
        if self.root is node:
            if node.left is None:
                self.root = node.right
            else:
                self.root = node.left
        # Case 2: Node is not the root
        if node.left is None:
            child = node.right
        else:
            child = node.left
        child.parent = node.parent

    # ----------------------------------------------------------------------- #
    # Traversal
    # A BST can be traversed through three basic algorithms: inorder, preorder,
    # and postorder tree walks.
    def __in_order(self, node: "BinaryTreeNode", tree: "list"):
        """
        Nodes from the left subtree get visited first, followed by the root
        node and right subtree.
        :param node:
        :param tree:
        :return:
        """
        if node is not None:
            self.__in_order(node.left, tree)
            tree.append(node.data)
            self.__in_order(node.right, tree)

    def __pre_order(self, node: "BinaryTreeNode", tree: "list"):
        """
        The root node gets visited first, followed by left and right subtrees.
        :param node:
        :param tree:
        :return:
        """
        if node is not None:
            tree.append(node.data)
            self.__pre_order(node.left, tree)
            self.__pre_order(node.right, tree)

    def __post_order(self, node: "BinaryTreeNode", tree: "list"):
        """
        Nodes from the left subtree get visited first, followed by the right
        subtree, and finally the root.
        :param node:
        :param tree:
        :return:
        """
        if node is not None:
            self.__post_order(node.left, tree)
            self.__post_order(node.right, tree)
            tree.append(node.data)
