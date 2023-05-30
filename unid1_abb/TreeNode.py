"""
Title: Tree Node Class for binary Search Tree
Author: Róger Roca Arano
Date: 2022-05-29
"""


class TreeNode:
    def __init__(self, value, deep: int = 0):
        self.__data = value
        self.__left: TreeNode = None
        self.__right: TreeNode = None
        self.__parent: TreeNode = None
        # self.__deep = deep

    def __str__(self):
        return f'- Data: {self.__data} ' \
               f'- Left: {self.__left} ' \
               f'- Right: {self.__right} ' \
               f'- Parent: {self.__parent}'

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

    # @property
    # def deep(self):
    #     return self.__deep

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

    # @deep.setter
    # def deep(self, value: int):
    #     self.__deep = value
