from __future__ import annotations
from mountain import Mountain
class MountainOrganiser:

    def __init__(self) -> None:
        self.sorted_mountain = []
        self.length = 0

    def cur_position(self, mountain: Mountain) -> int:
        """
        Find the position of the mountain in the sorted mountains

        arguments:
            Mountain object that were insert to find the position
        return:
            i - an integer indicates the position of the mountain input
        error:
            Raise KeyError when mountain insert is not in the list
        Complexity :
            Best case - O(1) Where there is only 1 mountain in the list
            Worst case - O(n) where n is the length of sorted_mountain
        """
        for i in range(len(self.sorted_mountain)):
            if self.sorted_mountain[i][1] == mountain.name:
                return i
        raise KeyError("Mountain is not added")

    def add_mountains(self, mountains: list[Mountain]):
        """
        Add a list of mountain and sort it according to the length of the mountain

        arguments:
            mountains - A list of Mountains
        Complexity :
            Best case - O(1) Where the len(self.sorted_mountain) == 0
            Worst case - O(n) where n is the length of mountain list
        """
        for i in range(len(mountains)):
            mountain_list = [None] * (len(self.sorted_mountain) + 1)
            if (i == 0) & (len(self.sorted_mountain) == 0):
                self.sorted_mountain.append([mountains[i].length, mountains[i].name])
            else:
                index = self.search_index(self.sorted_mountain, [mountains[i].length, mountains[i].name], len(self.sorted_mountain))
                for j in range(len(self.sorted_mountain)+1):
                    if j < index:
                        mountain_list[j] = (self.sorted_mountain[j])
                    elif j == index:
                        mountain_list[j] = [mountains[i].length, mountains[i].name]
                    elif j > index:
                        mountain_list[j] = self.sorted_mountain[j-1]
                self.sorted_mountain = mountain_list

    def search_index(self, l: list, item: list, hi, lo=0) -> int:
        """
        return the position of mountain should be added in the list according to the length
        modified binary search

        arguments:
            l - list of sorted mountain
            item - a list that contain length and name of mountain to find the index
            hi - an integer indicates the highest index
            lo - an integer indicates the lowest index
        return:
            an integer indicates the position of the current item in the l: list
        complexity :
            Best case - O(1)
            Worst case - O(log n) where n is the length of sorted mountain list
        """
        if lo == hi:
            return lo
        mid = (hi + lo) // 2
        if l[mid] > item:
            if mid == 0:
                return mid
            if l[mid-1] < item:
                return mid
            else:
                # Item would be before mid
                return self.search_index(l, item, mid, lo)
        elif l[mid] < item:
            if (mid+1) == len(l):
                return mid+1
            else:
                if l[mid+1] > item:
                    return mid+1
                else:
                    # Item would be after mid
                    return self.search_index(l, item, hi, mid+1)
        elif l[mid] == item:
            return mid


