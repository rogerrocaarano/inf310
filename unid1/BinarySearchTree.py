"""
Title: Binary Search Tree
Author: Róger Roca Arano
Date: 2022-05-29
"""
from TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self, tree_array: "list" = None):
        self.__root: TreeNode = None
        # self.__deep: int = 0
        if tree_array is not None:
            for i in tree_array:
                self.insert(i)

    def __str__(self, traversal_type: str = "inorder"):
        tree_list = list()
        if traversal_type == "inorder":
            self.__in_order(self.__root, tree_list)
        elif traversal_type == "preorder":
            self.__pre_order(self.__root, tree_list)
        elif traversal_type == "postorder":
            self.__post_order(self.__root, tree_list)
        else:
            return "Invalid traversal type."

        output = tree_list.__str__()
        output = output + f"\nTree deep: {self.deep}"
        return output

    # Getter methods
    @property
    def root(self):
        return self.__root

    @property
    def deep(self):
        left_deep = self.get_left_deep(self.root)
        right_deep = self.get_right_deep(self.root)
        return left_deep if left_deep > right_deep else right_deep

    # Setter methods

    # ----------------------------------------------------------------------- #
    # Utility methods
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

    # ----------------------------------------------------------------------- #
    # Searching

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

    # ----------------------------------------------------------------------- #
    # Insertion

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

    # ----------------------------------------------------------------------- #
    # Deletion

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

    # ----------------------------------------------------------------------- #
    # Traversal
    # A BST can be traversed through three basic algorithms: inorder, preorder,
    # and postorder tree walks.
    def __in_order(self, node: "TreeNode", tree: "list"):
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

    def __pre_order(self, node: "TreeNode", tree: "list"):
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

    def __post_order(self, node: "TreeNode", tree: "list"):
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
    # Balance
    # A BST is balanced if the height of the left and right subtrees of every
    # node differ by at most 1.

    def get_left_deep(self, root: "TreeNode"):
        """
        Private method for getting the deep of the left subtree.
        :param root: Starting node for the search.
        :return: Deep of the left subtree.
        """
        if root.left is None:
            return 0
        return self.get_left_deep(root.left) + 1

    def get_right_deep(self, root: "TreeNode"):
        """
        Private method for getting the deep of the right subtree.
        :param root: Starting node for the search.
        :return: Deep of the right subtree.
        """
        if root.right is None:
            return 0
        return self.get_right_deep(root.right) + 1

    def is_balanced(self, root: "TreeNode"):
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

    def __rotate_clockwise(self):
        """
        Private method for rotating the tree clockwise.
        """
        if self.root.left is None:
            return

        # Get the new values for root and right nodes
        new_root = self.root.left
        new_right = self.root
        # Set the parents of the new nodes
        new_root.parent = None
        new_right.parent = new_root
        # Set right nodes of new root and right
        if new_root.right is not None:
            new_right.left = new_root.right
        new_root.right = new_right
        # Set the new root
        self.__root = new_root

    def __rotate_counterclockwise(self):
        """
        Private method for rotating the tree counterclockwise.
        """
        if self.root.right is None:
            return

        # Get the new values for root and left nodes
        new_root = self.root.right
        new_left = self.root
        # Set the parents of the new nodes
        new_root.parent = None
        new_left.parent = new_root
        # Set left nodes of new root and left
        if new_root.left is not None:
            new_left.right = new_root.left
        new_root.left = new_left
        # Set the new root
        self.__root = new_root

    def balance(self):
        if self.is_balanced(self.__root):
            return
        while not self.is_balanced(self.__root):
            if (
                    self.get_left_deep(self.__root) >
                    self.get_right_deep(self.__root)
            ):
                self.__rotate_clockwise()
            else:
                self.__rotate_counterclockwise()
