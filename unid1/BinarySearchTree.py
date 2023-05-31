"""
Title: Binary Search Tree
Author: Róger Roca Arano
Date: 2022-05-29
github: https://github.com/rogerrocaarano/inf310
"""
from BinaryTreeNode import BinaryTreeNode


class BinarySearchTree:
    def __init__(self, tree_array: "list" = None):
        self.__root: BinaryTreeNode = None
        if tree_array is not None:
            for i in tree_array:
                self.insert(i)

    # Getter methods
    @property
    def root(self):
        return self.__root

    @property
    def deep(self):
        left_deep = self.get_left_deep(self.root)
        right_deep = self.get_right_deep(self.root)
        return max(left_deep, right_deep)

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
            self.__in_order(self.__root, tree_list)
        elif traversal_type == "preorder":
            self.__pre_order(self.__root, tree_list)
        elif traversal_type == "postorder":
            self.__post_order(self.__root, tree_list)
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
        :return: Node with the value searched or None if not found.
        """
        return self.__search(self.__root, value)

    def __search(self, root: "BinaryTreeNode", value):
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

    # ----------------------------------------------------------------------- #
    # Insertion

    def insert(self, value):
        """
        Public method for inserting a node in the tree.
        :param value: Value to be inserted.
        """
        node = BinaryTreeNode(value)
        # Case 1: Empty tree
        if self.__root is None:
            self.__root = node
        # Case 2: Non-empty tree
        else:
            self.__insert(self.__root, node)

    def __insert(self, root: "BinaryTreeNode", node: "BinaryTreeNode"):
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
        # node.deep = node.parent.deep + 1
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
        # self.deep = node.deep
        self.__insert(root, node)

    # ----------------------------------------------------------------------- #
    # Deletion

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

    @staticmethod
    def __delete_leaf(node: "BinaryTreeNode"):
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
    def __delete_single_child_node(node: "BinaryTreeNode"):
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

    # ----------------------------------------------------------------------- #
    # Balance
    # A BST is balanced if the height of the left and right subtrees of every
    # node differ by at most 1.

    def balance(self):
        """
        Public method for balancing the tree.
        """
        if self.is_balanced(self.__root):
            return
        while not self.is_balanced(self.__root):
            if (
                    self.get_left_deep(self.__root) >
                    self.get_right_deep(self.__root)
            ):
                self.__rotate("clockwise")
            else:
                self.__rotate("counterclockwise")

    def get_left_deep(self, root: "BinaryTreeNode"):
        """
        Private method for getting the deep of the left subtree.
        :param root: Starting node for the search.
        :return: Deep of the left subtree.
        """
        if root.left is None:
            return 0
        return self.get_left_deep(root.left) + 1

    def get_right_deep(self, root: "BinaryTreeNode"):
        """
        Private method for getting the deep of the right subtree.
        :param root: Starting node for the search.
        :return: Deep of the right subtree.
        """
        if root.right is None:
            return 0
        return self.get_right_deep(root.right) + 1

    def is_balanced(self, root: "BinaryTreeNode"):
        """
        Private method for checking if a BST is balanced.
        :param root: Starting node for the search.
        :return: True if the BST is balanced, False otherwise.
        """
        if root is None:
            return True
        left_deep = self.get_left_deep(root)
        right_deep = self.get_right_deep(root)
        if abs(left_deep - right_deep) <= 1:
            return True
        return False

    def __rotate(self, direction):
        """
        Private method for rotating the tree in the specified direction.
        :param direction: Direction of the rotation.
        """
        if direction == 'clockwise' and self.root.left is not None:
            new_root = self.root.left
            self.root.left = new_root.right
            if new_root.right is not None:
                new_root.right.parent = self.root
            new_root.parent = None
            new_root.right = self.root
            self.root.parent = new_root
            self.__root = new_root

        elif direction == 'counterclockwise' and self.root.right is not None:
            new_root = self.root.right
            self.root.right = new_root.left
            if new_root.left is not None:
                new_root.left.parent = self.root
            new_root.parent = None
            new_root.left = self.root
            self.root.parent = new_root
            self.__root = new_root
