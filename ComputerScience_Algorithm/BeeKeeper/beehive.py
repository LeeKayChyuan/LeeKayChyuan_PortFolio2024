from dataclasses import dataclass
from heap import MaxHeap

@dataclass
class Beehive:
    """
    A beehive has a position in 3d space, and some stats.
    : complexity best: O(1)
    : complexity worst: O(1)
    """

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    # compare the value of emerald worth in 1 harvest
    def __lt__(self, other):
        return (min(self.capacity, self.volume) * self.nutrient_factor) < \
               (min(other.capacity, other.volume) * other.nutrient_factor)

    def __gt__(self, other):
        return (min(self.capacity, self.volume) * self.nutrient_factor) > \
               (min(other.capacity, other.volume) * other.nutrient_factor)

    def __le__(self, other):
        return (min(self.capacity, self.volume) * self.nutrient_factor) <= \
               (min(other.capacity, other.volume) * other.nutrient_factor)

    def __ge__(self, other):
        return (min(self.capacity, self.volume) * self.nutrient_factor) >= \
               (min(other.capacity, other.volume) * other.nutrient_factor)


class BeehiveSelector:
    """
    Store the Beehive and allows modification on the beehive
    """

    def __init__(self, max_beehives: int):
        self.beehive = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        """
        reset the behives
        : complexity best: O(1) when len(hive_list) = 1
        : complexity worst: O(n)
        n = len(hive_list)
        """
        self.beehive = MaxHeap(len(hive_list))
        for i in range(len(hive_list)):
            self.beehive.add(hive_list[i])
    
    def add_beehive(self, hive: Beehive):
        """
        add the hive into the beehive
        : complexity: O(log(N))
        """
        if hive.volume > 0:
            self.beehive.add(hive)
    
    def harvest_best_beehive(self) -> float:
        """
        harvest the best hive from the beehive
        : complexity: O(log(N))
        : return: number of emeralds in float
        """
        max_beehive = self.beehive.get_max()
        emeralds = min(max_beehive.capacity, max_beehive.volume) * max_beehive.nutrient_factor
        max_beehive.volume -= max_beehive.capacity
        self.add_beehive(max_beehive)
        return float(emeralds)
