'''
Title: Binary Search Tree
Author: Róger Roca Arano
Date: 2022-05-29
Code version: 1.0
'''


# Tree node class definition for binary search tree
class TreeNode:
    def __init__(self, value):
        self.__data = value
        self.__left: TreeNode = None
        self.__right: TreeNode = None
        self.__parent: TreeNode = None

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

    # Setter methods
    @data.setter
    def data(self, value):
        self.__data = value

    @left.setter
    def left(self, node: "TreeNode"):
        self.__left = node

    @right.setter
    def right(self, node: "TreeNode"):
        self.__right = node

    @parent.setter
    def parent(self, node: "TreeNode"):
        self.__parent = node


class BinarySearchTree:
    def __init__(self):
        self.__root: TreeNode = None

    # Getter methods
    @property
    def root(self):
        return self.__root

    def __insert(self, root: "TreeNode", node: "TreeNode"):
        """
        Private method for inserting a node in the tree.
        :param root: Starting node for the insertion.
        :param node: Node to be inserted.
        """
        # Case 1: data already in the tree
        if root.data == node.data:
            return

        # Case 2: recursive insertion
        node.parent = root
        if node.data < root.data:
            if root.left is None:
                root.left = node
            else:
                root = root.left
        else:
            if root.right is None:
                root.right = node
            else:
                root = root.right
        self.__insert(root, node)

    def insert(self, value):
        """
        Public method for inserting a node in the tree.
        :param value: Value to be inserted.
        """
        node = TreeNode(value)
        # Case 1: Empty tree
        if self.__root is None:
            self.__root = node
        # Case 2: Non-empty tree
        else:
            self.__insert(self.__root, node)

    def __search(self, root: "TreeNode", value):
        """
        Private method for searching a node in the tree.
        :param root: Starting node for the search.
        :param value: Value to be searched.
        :return: Node with the value searched or None if not found.
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

    def search(self, value):
        """
        Public method for searching a node in the tree.
        :param value: Value to be searched.
        :return: Node with the value searched or None if not found.
        """
        return self.__search(self.__root, value)

    def in_order(self, node: "TreeNode", tree: "list"):
        """
        Public method for storing the tree in a list.
        :param node:
        :param tree:
        :return:
        """
        if node is not None:
            self.in_order(node.left, tree)
            tree.append(node.data)
            self.in_order(node.right, tree)

    def pre_order(self, node: "TreeNode", tree: "list"):
        if node is not None:
            tree.append(node.data)
            self.pre_order(node.left, tree)
            self.pre_order(node.right, tree)

    def post_order(self, node: "TreeNode", tree: "list"):
        if node is not None:
            self.post_order(node.left, tree)
            self.post_order(node.right, tree)
            tree.append(node.data)

    @staticmethod
    def __is_leaf(node: "TreeNode"):
        """
        Private method for checking if a node is a leaf.
        :param node: Node to be checked.
        :return: True if the node is a leaf, False otherwise.
        """
        return node.left is None and node.right is None

    @staticmethod
    def __has_one_child(node: "TreeNode"):
        """
        Private method for checking if a node has one child.
        :param node: Node to be checked.
        :return: True if the node has one child, False otherwise.
        """
        return node.left is None or node.right is None

    @staticmethod
    def __delete_leaf(node: "TreeNode"):
        """
        Private method for deleting a leaf.
        :param node: Node to be deleted.
        """
        if node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
        del node

    @staticmethod
    def __delete_single_child_node(node: "TreeNode"):
        """
        Private method for deleting a node with one child.
        :param node: Node to be deleted.
        """
        # Get the child node and set its parent to the parent of the node to
        # be deleted
        child_node = node.left if (node.left is not None) else node.right
        child_node.parent = node.parent

        # Set the child node as the child of the parent of the node to be
        # deleted and delete the node
        if node.parent.left == node:
            node.parent.left = child_node
        else:
            node.parent.right = child_node
        del node

    @staticmethod
    def __higher_from_left(root: "TreeNode"):
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
    def __lower_from_right(root: "TreeNode"):
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

    def delete(self, value):
        """
        Public method for deleting a node from the tree.
        :param value: Value to be deleted.
        """
        node = self.search(value)
        # Case 1: Value not found
        if node is None:
            return
        # Case 2: Node is a leaf
        if self.__is_leaf(node):
            self.__delete_leaf(node)
        # Case 3: Node has one child
        elif self.__has_one_child(node):
            self.__delete_single_child_node(node)
        # Case 4: Node has two children
        else:
            # Get the highest node in the left subtree
            higher = self.__higher_from_left(node)
            # Replace the node with the highest node in the left subtree
            node.data = higher.data
            # Delete the highest node in the left subtree
            if self.__is_leaf(higher):
                self.__delete_leaf(higher)
            else:
                self.__delete_single_child_node(higher)
