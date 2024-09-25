from typing import TypeVar, Generic
from ctypes import py_object

# Question 1
def fuse(fitmons):
    """
    Fuse the fitmons to its cutest form.

    :param fitmons: The fitmons to fuse, a list of tuples that representing the fitmons (affinity left, cuteness, affinity right).
    :return: The cutest fitmon ever.
    :Time complexity: O(n^3) where n is the number of fitmons.
    :Time complexity analysis: This function uses a nested loop to iterate all possible combination of fitmons, resulting in cubic time complexity.
    :Space complexity: O(n^2) where n is the number of fitmons (2d array).
    :Space complexity analysis: The function use a 2D array to store the combinations, resulting in s square complexity.
    """
    num_fitmon = len(fitmons)
    combinations = [[0] * num_fitmon for _ in range(num_fitmon)]  # 2D array to store the combination

    for length in range(num_fitmon):
        for i in range(num_fitmon - length):
            j = i + length
            # assign the most original fitmons to the 2D array
            if i == j:
                combinations[i][j] = fitmons[i]
            for k in range(i, j):
                fitmon_left = combinations[i][k]
                fitmon_right = combinations[k + 1][j]
                cuteness_score = int(fitmon_left[1] * fitmon_left[2] + fitmon_right[1] * fitmon_right[0])
                # fuse the fitmon
                fitmon_v = [fitmon_left[0], cuteness_score, fitmon_right[2]]
                # assign and compare the fused fitmon on its cuteness
                if combinations[i][j] == 0 or combinations[i][j][1] < fitmon_v[1]:
                    combinations[i][j] = fitmon_v
    return combinations[0][num_fitmon - 1][1]


# Question 2
class TreeMap:
    def __init__(self, roads, solulus):
        """
        Instantiate
        :param roads: The road available, a list of tuples representing the roads(start, end, time)
        :param solulus: The solulus available, a list of tuples representing the solulus(start, time, end)
        :Time complecity: O(n+m) n is the number of roads and m is the number of solulus
        :Time complexity analysis: To generate the tree structures, the initialization step involves iterating over the lists of roads and solulus.
        :Space complexity: O(n) where n is the len(roads)
        :Space complexity analysis: a list is created with the length of the road to store the Trees in the map
        """
        self.roads = roads
        self.solulus = []
        self.trees = [None] * (len(roads) - 1)
        # Get all the trees from roads
        for u in self.roads:
            # create a road
            road = Road(u)
            if self.trees[road.start.id] is None:
                self.trees[road.start.id] = road.start
            self.trees[road.start.id].roads.append(road)
            if self.trees[road.end.id] is None:
                self.trees[road.end.id] = road.end
        # Get all trees from solulu
        for solulu in solulus:
            soluluRoad = Road((solulu[0], solulu[2], solulu[1]))
            if self.trees[soluluRoad.start.id] is None:
                self.trees[soluluRoad.start.id] = soluluRoad.start
            if self.trees[soluluRoad.end.id] is None:
                self.trees[soluluRoad.end.id] = soluluRoad.end
            self.solulus.append(soluluRoad)

    def escape(self, start, exits):
        """
        Modified dijkstra to find all the shortest available path from start to exit that went through solulu
        :param start: The starting Tree id
        :param exits: A list of exits Tree ids
        :return: The shortest path and Time taken
        :Time Complexity:  O((n + m) log n) n is the number of trees and m is the number of roads
        :Time Complexity Analysis: It takes O(n) time to initialise the algorithm and set up initial conditions for the
        priority queue and the trees, where n is the number of trees. The main task of the algorithm is to visit every
        tree and, in the event that a shorter path is discovered, update the shortest path to its neighbours. The overall
        time complexity of this method is O(n + m), where n is the number of trees and m is the number of roads. This process
        is repeated for each tree and each road. Nevertheless, because the method makes use of a priority queue (executed as a min-heap),
        the log n factor for each heap operation results in an O((n + m) log n) time complexity.

        :Space Complexity: O(n) where n is the number of trees
        :Space Complexity analysis: Based on the trees' current shortest paths, the method manages them using a priority
        queue (executed as a min-heap). The priority queue's space complexity is O(n), where n is the number of trees.
        """
        startTree = self.trees[start]
        exitsTrees = exits
        startTree.time = 0
        discovered = MinHeap(len(self.roads))
        discovered.add(startTree)

        # Search for all available shortest road
        while len(discovered) > 0:
            u = discovered.get_min()
            u.visited = True
            for road in u.roads:
                v = road.end
                if v.discovered == False:
                    v.discovered = True
                    v.time = u.time + road.time
                    v.previous = u
                    discovered.add(v)
                elif v.visited == False:
                    if v.time > u.time + road.time:
                        v.time = u.time + road.time
                        v.previous = u
                        discovered.add(v)

        # add solulu into the road
        for solulu in self.solulus:
            v = self.trees[solulu.end.id]
            u = self.trees[solulu.start.id]
            v.discovered = True
            v.time = u.time + solulu.time
            v.isDestroyed = True
            if v != u:
                v.previous = u

        # Get the road that reach the destination with passing through atleast 1 solulu
        for exitsTree in exitsTrees:
            for u in self.trees:
                if u is None:
                    continue
                if u.id == exitsTree:
                    if u.isDestroyed:
                        discovered.add(u)

        # back tracking the path
        minPath = discovered.get_min()
        path = [minPath.id]
        while minPath.previous.id != startTree.id:
            path.append(minPath.previous.id)
            minPath = minPath.previous
        path.append(minPath.previous.id)
        return print(minPath.time, path)


class Road:
    """
    A Road object indicates the road from 1 tree to another
    """
    def __init__(self, road):
        """
        Instantiate
        :param road: a tuple with (start, end, time)
        """
        self.start = Tree(road[0])
        self.end = Tree(road[1])
        self.time = road[2]

class Tree:
    """
    A Tree object as the tree in the forest
    """
    def __init__(self, id):
        """
        Instantiate
        :param id: The id that represent the tree
        """
        self.id = id
        # list of road
        self.roads = []
        self.solulus = []
        # for traversal
        self.discovered = False
        self.visited = False
        # travel time
        self.time = 0
        # backtracking/ from where
        self.previous = None
        self.isDestroyed = False

    def __gt__(self, other):
        """
        Return a boolean after comparing this greater than other
        :param other: another Tree object to compare
        :return: Boolean
        """
        return self.time > other.time

    def __ge__(self, other):
        """
        Return a boolean after comparing this greater than or equal to other
        :param other: another Tree object to compare
        :return: Boolean
        """
        return self.time >= other.time

    def __lt__(self, other):
        """
        Return a boolean after comparing this lesser than other
        :param other: another Tree object to compare
        :return: Boolean
        """
        return self.time < other.time

    def __le__(self, other):
        """
        Return a boolean after comparing this lesser than or equal to other
        :param other: another Tree object to compare
        :return: Boolean
        """
        return self.time <= other.time

T = TypeVar('T')
# Reference from FIT1008 Assignment 3 2023 S1
class MinHeap(Generic[T]):
    """
    A Minimum Heap
    """
    MIN_CAPACITY = 1
    def __init__(self, max_size: int) -> None:
        """
        Instantiate
        :param max_size: maximum size of the heap
        """
        self.length = 0
        self.the_array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)

    def __len__(self) -> int:
        return self.length

    def is_full(self) -> bool:
        return self.length + 1 == len(self.the_array)

    def rise(self, k: int) -> None:
        """
        Rise element at index k to its correct position
        :pre: 1 <= k <= self.length
        :Time complexity: O(log n) n is number of element in heap
        :Space complexity: O(1)
        """
        item = self.the_array[k]
        while k > 1 and item < self.the_array[k // 2]:
            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        self.the_array[k] = item

    def add(self, element: T) -> bool:
        """
        Swaps elements while rising
        :Time complexity: O(log n) n is number of element in heap
        :Space complexity: O(1)
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = element
        self.rise(self.length)

    def smallest_child(self, k: int) -> int:
        """
        Returns the index of k's child with smallest value.
        :pre: 1 <= k <= self.length // 2
        :Time complexity: O(1)
        :Space complexity: O(1)
        """

        if 2 * k == self.length or \
                self.the_array[2 * k] < self.the_array[2 * k + 1]:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:
        """
        Make the element at index k sink to the correct position.
        :pre: 1 <= k <= self.length
        :Time complexity: O(log n) n is number of element in heap
        :Space complexity: O(1)
        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            min_child = self.smallest_child(k)
            if self.the_array[min_child] >= item:
                break
            self.the_array[k] = self.the_array[min_child]
            k = min_child

        self.the_array[k] = item

    def get_min(self) -> T:
        """
        Remove (and return) the minimum element from the heap.
        :Time complexity: O(log n) n is number of element in heap
        :Space complexity: O(1)
        """
        if self.length == 0:
            raise IndexError

        min_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length + 1]
            self.sink(1)
        return min_elt

# Reference from FIT1008 Assignment 3 2023 S1
class ArrayR(Generic[T]):
    def __init__(self, length: int) -> None:
        """
        Creates an array of references to objects of the given length
        :complexity: O(length) for best/worst case to initialise to None
        :pre: length > 0
        Time complexity: O(n) n is the length of the array.
        Space complexity: O(n) n is the length of the array.
        """
        if length <= 0:
            raise ValueError("Array length should be larger than 0.")
        self.array = (length * py_object)()  # initialises the space
        self.array[:] = [None for _ in range(length)]

    def __len__(self) -> int:
        """
        Returns the length of the array
        :complexity: O(1)
        """
        return len(self.array)

    def __getitem__(self, index: int) -> T:
        """
        Returns the object in position index.
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """
        Sets the object in position index with the value
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.array[index] = value