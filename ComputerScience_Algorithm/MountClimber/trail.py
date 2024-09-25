from __future__ import annotations
from dataclasses import dataclass

import copy
from mountain import Mountain

from typing import TYPE_CHECKING, Union
from data_structures.linked_stack import LinkedStack

# Avoid circular imports for typing.
if TYPE_CHECKING:
    from personality import WalkerPersonality

@dataclass
class TrailSplit:
    """
    A split in the trail.
       ___path_top____
      /               \
    -<                 >-path_follow-
      \__path_bottom__/
    """

    path_top: Trail
    path_bottom: Trail
    path_follow: Trail

    def remove_branch(self) -> TrailStore:
        """Removes the branch, should just leave the remaining following trail."""
        self = self.path_follow.store
        return self

@dataclass
class TrailSeries:
    """
    A mountain, followed by the rest of the trail

    --mountain--following--

    """

    mountain: Mountain
    following: Trail

    def remove_mountain(self) -> TrailStore:
        """Removes the mountain at the beginning of this series."""
        self = self.following.store
        return self

    def add_mountain_before(self, mountain: Mountain) -> TrailStore:
        """Adds a mountain in series before the current one."""
        self = TrailSeries(mountain, Trail(TrailSeries(self.mountain, self.following)))
        return self

    def add_empty_branch_before(self) -> TrailStore:
        """Adds an empty branch, where the current trailstore is now the following path."""
        self = TrailSplit(Trail(None), Trail(None), Trail(TrailSeries(self.mountain, self.following)))
        return self

    def add_mountain_after(self, mountain: Mountain) -> TrailStore:
        """Adds a mountain after the current mountain, but before the following trail."""
        self = TrailSeries(self.mountain, Trail(TrailSeries(mountain, self.following)))
        return self

    def add_empty_branch_after(self) -> TrailStore:
        """Adds an empty branch after the current mountain, but before the following trail."""
        self = TrailSeries(self.mountain, Trail(TrailSplit(Trail(None), Trail(None), self.following)))
        return self

TrailStore = Union[TrailSplit, TrailSeries, None]

@dataclass
class Trail:
    store: TrailStore = None

    def add_mountain_before(self, mountain: Mountain) -> Trail:
        """Adds a mountain before everything currently in the trail."""
        self = Trail(TrailSeries(mountain, Trail(self.store)))
        return self

    def add_empty_branch_before(self) -> Trail:
        """Adds an empty branch before everything currently in the trail."""
        self = Trail(TrailSplit(Trail(None), Trail(None), Trail(self.store)))
        return self

    def follow_path(self, personality: WalkerPersonality) -> None:
        """
        Follow a path and add mountains according to a personality.

        Arguments :
        personality = personality of users

        Complexity :
        Best case=O(1)
        Worst Case=O(n)
        """
        Trail_Stack = LinkedStack()
        Trail_Stack.push(self)
        while not Trail_Stack.is_empty():
            Current_Trail = Trail_Stack.pop().store
            if isinstance(Current_Trail, TrailSeries):
                personality.add_mountain(Current_Trail.mountain)
                if Current_Trail.following is not Trail(None):
                    Trail_Stack.push(Current_Trail.following)

            elif isinstance(Current_Trail, TrailSplit):
                if Current_Trail.path_follow != Trail(None):
                    Trail_Stack.push(Current_Trail.path_follow)
                if personality.select_branch(Current_Trail.path_top, Current_Trail.path_bottom) is True:
                    Trail_Stack.push(Current_Trail.path_top)
                else:
                    Trail_Stack.push(Current_Trail.path_bottom)

    def collect_all_mountains(self) -> list[Mountain]:
        """Returns a list of all mountains on the trail."""
        if isinstance(self,Trail):
            if isinstance(self.store,TrailSeries):
                return [self.store.mountain] + self.store.following.collect_all_mountains()
            elif isinstance(self.store, TrailSplit):
                return self.store.path_top.collect_all_mountains() + self.store.path_bottom.collect_all_mountains() + self.store.path_follow.collect_all_mountains()
            else:
                return []

    def length_k_paths(self, k) -> list[list[Mountain]]:  # Input to this should not exceed k > 50, at most 5 branches.
        """
        Returns a list of all paths of containing exactly k mountains.
        Paths are represented as lists of mountains.

        Paths are unique if they take a different branch, even if this results in the same set of mountains.
        argument:
            k- an integer that indicates the num of mountain required in a path
        return:
            list[list[Mountain]]- a list to store the path(express as a list of mountain) that contains k mountains
        complexity:
            best case- O(1) when k > 50
            worst case- O(self.length_k_paths_aux) + O(N) where N is the number of elments in mountain_lst_lst
        """
        if k > 50:
            raise KeyError("k should not exceed 50")
        mountain_lst_lst = self.length_k_paths_aux()
        mountain_lst_with_length_k = []
        for mountain_lst in mountain_lst_lst:
            if len(mountain_lst) == k:
                mountain_lst_with_length_k.append(mountain_lst)
        return mountain_lst_with_length_k

    def length_k_paths_aux(self, mount_lst_lst=[]) -> list[list[Mountain]]:
        """
        Return all the paths without considering the length of the path(number of mountains contain)
        argument:
            mount_lst_lst- a list of lists of mountains,default to be empty list []
        return:
            list[list[Mountain]]- a list to store all the path(express as a list of mountain)
        complexity:
            best case- O(1) if self.store == None
            worst case- O(N) where N is the length of the Trail as it can be infinitely long
        """
        if isinstance(self.store, TrailSeries):
            if len(mount_lst_lst) < 1:
                mount_lst_lst.append([self.store.mountain])
            else:
                for mount_lst in mount_lst_lst:
                    mount_lst.append(self.store.mountain)
            mount_lst_lst = self.store.following.length_k_paths_aux(mount_lst_lst)
        elif isinstance(self.store, TrailSplit):
            temp1 = []
            temp2 = []
            temp1 = copy.deepcopy(mount_lst_lst)
            temp2 = copy.deepcopy(mount_lst_lst)
            temp1 = self.store.path_top.length_k_paths_aux(temp1)
            temp2 = self.store.path_bottom.length_k_paths_aux(temp2)
            mount_lst_lst = temp1 + temp2
            mount_lst_lst = self.store.path_follow.length_k_paths_aux(mount_lst_lst)
        else:
            return mount_lst_lst
        return mount_lst_lst