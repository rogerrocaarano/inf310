"""
Title: Tree Node Class for binary Search Tree
Author: Róger Roca Arano
Date: 2022-05-29
"""


class BinaryTreeNode:
    def __init__(self, value):
        self.__data = value
        self.__left: BinaryTreeNode = None
        self.__right: BinaryTreeNode = None
        self.__parent: BinaryTreeNode = None

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
    def left(self, node: "BinaryTreeNode"):
        self.__left = node

    @right.setter
    def right(self, node: "BinaryTreeNode"):
        self.__right = node

    @parent.setter
    def parent(self, node: "BinaryTreeNode"):
        self.__parent = node
