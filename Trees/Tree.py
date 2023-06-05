from Trees.TreeNode import TreeNode


class Tree:
    def __init__(self):
        self.__root = None
        self.__deep = 0

    @property
    def root(self):
        return self.__root

    @property
    def deep(self):
        return self.__deep

    @root.setter
    def root(self, node: "TreeNode"):
        self.__root = node
