from Trees.BinaryTreeNode import *
from Trees.Exceptions import *


class BinarySearchTree:
    def __init__(self, tree_array: list = None):
        self.__root = None
        self.__deep = 0
        if tree_array is not None:
            for value in tree_array:
                self.insert(value)

    # ----------------------------------------------------------------------- #
    # Getters and setters

    @property
    def root(self):
        return self.__root

    @property
    def deep(self):
        return self.__deep

    @root.setter
    def root(self, node: "BinaryTreeNode"):
        self.__root = node

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
            self.in_order(self.root, tree_list)
        elif traversal_type == "preorder":
            self.pre_order(self.root, tree_list)
        elif traversal_type == "postorder":
            self.post_order(self.root, tree_list)
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
    def higher_from_left(root: "BinaryTreeNode"):
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
    def lower_from_right(root: "BinaryTreeNode"):
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

    def __promote_higher_left(self, node):
        """
        Private method for promoting the highest node in the left subtree.
        :param node: Node to be promoted.
        """
        # Get needed nodes
        higher = self.higher_from_left(node)
        left = node.left
        right = node.right

        # Case node is the root
        if node is self.root:
            self.root = higher

        # Detach nodes
        higher.make_orphan()
        left.make_orphan()
        right.make_orphan()
        del node

        higher.right = right
        higher.left = left

    def __promote_lower_right(self, node):
        lower = self.lower_from_right(node)

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
        if node < root:
            if root.left is None:
                root.left = node
            else:
                self.__insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                self.__insert(root.right, node)

    # ----------------------------------------------------------------------- #
    # Delete
    def delete(self, value, promote: str = "higher-left"):
        """
        Public method for deleting a node from the tree.
        :param value: Value to be deleted.
        :param promote: Method for promoting a node when deleting a node with
        two children. Choose between "higher-left" or "lower-right", default
        is "higher-left".
        """
        node = self.__search(self.root, value)
        # Case 1: Value not found
        if node is None:
            return
        # Case 2: Node is a leaf
        if node.children == 0:
            self.__delete_leaf_node(node)
        elif node.children == 1:
            self.__delete_one_child_node(node)
        # Case 4: Node has two children
        else:
            if promote == "higher-left":
                self.__promote_higher_left(node)
            elif promote == "lower-right":
                self.__promote_lower_right(node)
            else:
                raise InvalidPromotionMethod

    def __delete_leaf_node(self, node: "BinaryTreeNode"):
        """
        Private method for deleting a leaf node.
        :param node: Node to be deleted.
        """
        # Case 1: Node is the root
        if node is self.root:
            self.root = None
            del node
            return
        # Case 2: Node is not the root
        parent = node.parent
        if parent.left is node:
            parent.left = None
        else:
            parent.right = None
        del node

    def __delete_one_child_node(self, node: "BinaryTreeNode"):
        """
        Private method for deleting a node with one child.
        :param node: Node to be deleted.
        """
        # Case 1: Node is the root
        if self.root is node:
            # Switch the root
            if node.left is None:
                self.root = node.right
            else:
                self.root = node.left
            self.root.make_orphan()
            del node
            return
        # Case 2: Node is not the root
        if node.left is None:
            child = node.right
        else:
            child = node.left

        # Detach Nodes:
        parent = node.parent
        node.make_orphan()
        child.make_orphan()
        del node

        # Attach child to its new parent
        if parent > child:
            parent.left = child
        else:
            parent.right = child

    # ----------------------------------------------------------------------- #
    # Traversal
    # A BST can be traversed through three basic algorithms: inorder, preorder,
    # and postorder tree walks.
    def in_order(self, node: "BinaryTreeNode", tree: "list"):
        """
        Nodes from the left subtree get visited first, followed by the root
        node and right subtree.
        :param node:
        :param tree:
        :return:
        """
        if node is not None:
            self.in_order(node.left, tree)
            tree.append(node.data)
            self.in_order(node.right, tree)

    def pre_order(self, node: "BinaryTreeNode", tree: "list"):
        """
        The root node gets visited first, followed by left and right subtrees.
        :param node:
        :param tree:
        :return:
        """
        if node is not None:
            tree.append(node.data)
            self.pre_order(node.left, tree)
            self.pre_order(node.right, tree)

    def post_order(self, node: "BinaryTreeNode", tree: "list"):
        """
        Nodes from the left subtree get visited first, followed by the right
        subtree, and finally the root.
        :param node:
        :param tree:
        :return:
        """
        if node is not None:
            self.post_order(node.left, tree)
            self.post_order(node.right, tree)
            tree.append(node.data)

    # ----------------------------------------------------------------------- #
    # Balance
    # A BST is balanced if the height of the left and right subtrees of every
    # node differ by at most 1.
    #
    # Traverse given BST in inorder and store result in an array. Note that
    # this array would be sorted as inorder.
    # Build a balanced BST from the above created sorted array using a
    # recursive approach. This step also takes O(n) time as we traverse every
    # element exactly once and processing an element takes O(1) time.

    def balance(self):
        """
        Public method for balancing the tree.
        :return:
        """
        # Get the balanced tree
        balanced_tree = self.get_balanced_tree()
        # Delete the current tree
        self.root = None
        # Insert the balanced tree
        for node in balanced_tree:
            self.insert(node)

    def get_balanced_tree(self):
        """
        Public method for getting a balanced tree.
        :return:
        """
        # Get the inorder tree
        inorder_tree = []
        self.in_order(self.root, inorder_tree)
        # Get the balanced tree
        balanced_tree = []
        BinarySearchTree.__get_balanced_tree(inorder_tree, balanced_tree)
        # Return the balanced tree
        return balanced_tree

    @staticmethod
    def __get_balanced_tree(inorder_tree: list[BinaryTreeNode],
                            balanced_tree: list[BinaryTreeNode]):
        # Base case:
        if len(inorder_tree) < 3:
            inorder_tree.reverse()
            balanced_tree.extend(inorder_tree)
            return balanced_tree
        # Recursive case:
        root_pos = len(inorder_tree) // 2
        balanced_tree.append(inorder_tree[root_pos])
        left_tree = inorder_tree[:root_pos]
        right_tree = inorder_tree[root_pos + 1:]
        BinarySearchTree.__get_balanced_tree(left_tree, balanced_tree)
        BinarySearchTree.__get_balanced_tree(right_tree, balanced_tree)
