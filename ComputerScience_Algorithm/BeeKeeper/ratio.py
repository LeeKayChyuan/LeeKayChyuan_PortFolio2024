from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil, floor
from bst import BinarySearchTree
from node import TreeNode

T = TypeVar("T")
I = TypeVar("I")


class Percentiles(Generic[T]):

    def __init__(self) -> None:
        """
        initialize a bst
        O(1)
        """
        self.list = BinarySearchTree()

    def add_point(self, item: T):
        """
        add item to bst
        O(log n)
        """
        self.list[item] = item

    def remove_point(self, item: T):
        """
        remove item from bst
        O(log n)
        """
        del (self.list[item])

    def ratio(self, x, y):
        """
        Worst case of O(N) where n is number of nodes
        use inorder to recursive call and add the values
        returns a list that contains all elements that are within percentages
        """
        ans = []
        lb_add_one = ceil(self.list.length * (x / 100)) + 1
        item = self.list.kth_smallest(lb_add_one, self.list.root).item
        ans.append(item)
        self.inorder(self.list.root, ans, x, y, 0)
        return ans

    def inorder(self, current: TreeNode, ans: list, x, y, j: int):
        """
        lb and ub are the upper and lower bound index given percentage x and y
        traverses our binary tree in order while adding values that are within lb and ub
        """
        lb = ceil(self.list.length * (x / 100))
        ub = floor(self.list.length * (100 - y) / 100)

        if current is not None:  # if not a base case
            if current.left is None:
                location = j
            else:
                location = current.left.subtree_size + j

            if (location > lb) and (location < ub):
                ans.append(current.item)

            if current.item is not ans[0]:
                self.inorder(current.left, ans, x, y, j)

            if location <= ub:
                self.inorder(current.right, ans, x, y, location + 1)


if __name__ == "__main__":
    points = list(range(50))
    import random

    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))