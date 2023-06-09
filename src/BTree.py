from src.MWayTree import MWayTree
from src.BTreeNode import BTreeNode
from src.MWayTreeNode import MWayTreeNode
from src.Exceptions import *


class BTree(MWayTree):
    def __init__(self,
                 tree_array: list = None,
                 paths=3
                 ):
        super().__init__(tree_array, paths)

    def _insert(self, value, node: MWayTreeNode):
        if node.is_full:
            node = BTreeNode.cast_as_b_node(node)
            self.__split_insert(node, value)
            node = BTreeNode.cast_as_m_node(node)
        else:
            super()._insert(value, node)

    def __split_insert(self, node: BTreeNode, value):
        parent: MWayTreeNode = node.parent
        new_node: MWayTreeNode
        split_result = node.split_node()
        mid_value = split_result[0]
        new_node = split_result[1]
        if parent is None:
            if mid_value > value:
                parent_value = mid_value
                node_value = value
            else:
                parent_value = value
                node_value = mid_value
            parent = MWayTreeNode(parent_value, self.paths)
            self.root = parent
            parent.insert_child(node, 0)
            parent.insert_child(new_node, 2)
            node.insert_value(node_value)
        elif parent.is_full:
            node.insert_value(mid_value)
            parent_b_first_value_pos = ((parent.__sizeof__() - 1) // 2) + 1
            parent_b_first_value = parent.get_value(parent_b_first_value_pos)
            parent: BTreeNode = BTreeNode.cast_as_b_node(parent)
            self.__split_insert(parent, value)
            parent: MWayTreeNode = BTreeNode.cast_as_m_node(parent)
            pos = self.search(parent_b_first_value)
            pos[0].insert_child(new_node, 0)
            node: MWayTreeNode = BTreeNode.cast_as_m_node(node)
            parent_insert_pos = MWayTreeNode.value_pos_to_data_pos(
                parent_b_first_value_pos) - 1
            parent.insert_child(node, parent_insert_pos)
        else:
            node.insert_value(value)
            parent.insert_value(mid_value)
            pos = parent.search(mid_value)
            pos = MWayTreeNode.value_pos_to_data_pos(pos)
            parent: MWayTreeNode = BTreeNode.cast_as_m_node(parent)
            parent.insert_child(new_node, pos + 1)
            node: MWayTreeNode = BTreeNode.cast_as_m_node(node)
            parent.insert_child(node, pos - 1)
