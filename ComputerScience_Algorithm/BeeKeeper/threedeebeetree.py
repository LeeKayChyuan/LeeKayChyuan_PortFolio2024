from __future__ import annotations
from typing import Generic, TypeVar, Tuple, List
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    subtree_size: int = 1

    children: List[BeeNode | None] = field(default_factory=lambda: [None] * 8)

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        """
        The Big(O) time complexity is O(1) because get_index is also O(1)
        returns child
        """
        return self.children[self.get_index(point)]
    def get_index(self, point):
        """
        The Big(O) time complexity is also O(1)
        checks which of the 8 possible outcomes for the point relative to the current key
        and returns the index the child should be at
        """
        x,y,z = point
        x1,y1,z1 = self.key

        if self.key == point:
            return self
        elif (x1 <= x, y1 <= y, z1 <= z) == (True, True, True):
            return 0
        elif (x1 <= x, y1 <= y, z1 <= z) == (True, True, False):
            return 1
        elif (x1 <= x, y1 <= y, z1 <= z) == (True, False, True):
            return 2
        elif (x1 <= x, y1 <= y, z1 <= z) == (True, False, False):
            return 3
        elif (x1 <= x, y1 <= y, z1 <= z) == (False, True, True):
            return 4
        elif (x1 <= x, y1 <= y, z1 <= z) == (False, True, False):
            return 5
        elif (x1 <= x, y1 <= y, z1 <= z) == (False, False, True):
            return 6
        elif (x1 <= x, y1 <= y, z1 <= z) == (False, False, False):
            return 7

class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        """
        Best case O(1)
        worst case O(n) where n is number of nodes in the tree
        returns BeeNode corresponding to key
        """
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: BeeNode, key: Point) -> BeeNode:
        """
        recursively call itself until the current key is the same as the provided key
        """
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:
            return current
        else:
            return self.get_tree_node_by_key_aux(current.get_child_for_key(key), key)

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
            Best case O(1)
            worst case O(n) where n is number of nodes in the tree
        """
        if current is None:  # base case: at the leaf
            self.length += 1
            return BeeNode(key, item=item)
        elif (current.key == key):
            raise ValueError('Duplicate item')
        else:
            current.children[current.get_index(key)] = self.insert_aux(current.get_child_for_key(key), key, item)
            current.subtree_size += 1

        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf.
        Best case O(1)
        worst case O(n)"""
        for i in current.children:
            if i is not None:
                return False
            else:
                return True

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2