from mountain import Mountain
from mountain_organiser import MountainOrganiser
from double_key_table import DoubleKeyTable

class MountainManager:

    def __init__(self) -> None:
        self.AllMountain = DoubleKeyTable(None, None)

    def add_mountain(self, mountain: Mountain) -> None:
        """
        Add mountain into the Hash Table according to the difficulty level

        Argument :
            mountain- a Mountain class that store the content of a mountain

        Complexity :
            Best case - O(1)
            Worst case - O(1)
        """
        key = (str(mountain.difficulty_level), mountain.name)
        self.AllMountain.__setitem__(key, mountain)

    def remove_mountain(self, mountain: Mountain) -> None:
        """
        Remove mountain in the Hash Table

        Argument :
            mountain- a Mountain class that store the content of a mountain

        Complexity :
            Best case - O(1)
            Worst case - O(1)
        """
        key = (str(mountain.difficulty_level), mountain.name)
        self.AllMountain.__delitem__(key)

    def edit_mountain(self, old: Mountain, new: Mountain) -> None:
        """
        Edit mountain in the Hash Table

        Argument :
            old - Mountain to be replaced
            new - Mountain to be added

        Complexity :
            Best case - O(1)
            Worst case - O(1)
        """
        old_key = (str(old.difficulty_level), old.name)
        new_key = (str(new.difficulty_level), new.name)
        self.AllMountain.__delitem__(old_key)
        self.AllMountain.__setitem__(new_key, new)

    def mountains_with_difficulty(self, diff: int) -> list[Mountain]:
        """
        Return a list of all mountains with this difficulty

        Arguments:
            diff - an integer indicates difficulty of the mountain

        Complexity :
            Best case - O(1)
            Worst case - O(n)
        """
        iter_obj = self.AllMountain.iter_values(str(diff))
        mountain_list = []
        for i in iter_obj:
            mountain_list.append(i)

        return mountain_list

    def group_by_difficulty(self) -> list[list[Mountain]]:
        """
        Return a list of lists of all mountains grouped by difficulty

        Complexity :
            Best case - O(1)
            Worst case - O(n^2) where n is the number of elements in keys
        """
        keys = self.AllMountain.keys(None)
        int_keys = []
        sorted_mountain = []
        for key in keys:
            int_keys.append(int(key))
        for _ in range(len(keys)):
            mountain_list = self.mountains_with_difficulty(int_keys.pop(int_keys.index(min(int_keys))))
            sorted_mountain.append(mountain_list)
        return sorted_mountain
