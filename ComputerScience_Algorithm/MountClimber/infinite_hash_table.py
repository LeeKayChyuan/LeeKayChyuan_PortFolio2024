from __future__ import annotations
from typing import Generic, TypeVar

from data_structures.referential_array import ArrayR

K = TypeVar("K")
V = TypeVar("V")

class InfiniteHashTable(Generic[K, V]):
    """
    Infinite Hash Table.

    Type Arguments:
        - K:    Key Type. In most cases should be string.
                Otherwise `hash` should be overwritten.
        - V:    Value Type.

    Unless stated otherwise, all methods have O(1) complexity.
    """

    TABLE_SIZE = 27

    def __init__(self) -> None:
        self.count = 0
        self.level = 0
        self.table = ArrayR(InfiniteHashTable.TABLE_SIZE)

    def hash(self, key: K) -> int:
        if self.level < len(key):
            return ord(key[self.level]) % (self.TABLE_SIZE-1)
        return self.TABLE_SIZE-1

    def __getitem__(self, key: K) -> V:
        """
        Get the value at a certain key

        :raises KeyError: when the key doesn't exist.
        argument:
            key- a key type to determine the position of the data
        return:
            v- A value type where its position is with respect to the key
        complexity:
            best case- O(1) when self.table[position] is None
            worst case- O(internal table.__getitem__) as it can be infinitely long until it meets a tuple or NoneType
        """
        position = self.hash(key)
        if self.table[position] is None:
            raise KeyError("Key doesn't exist.")
        if isinstance(self.table[position],tuple):
            if self.table[position][0] != key:
                raise  KeyError("Key doesn't exist.")
            else:
                return self.table[position][1]
        else:
            self.table[position].__getitem__(key)


    def __setitem__(self, key: K, value: V) -> None:
        """
        Set an (key, value) pair in our hash table.
        argument:
            key- a key type which determines the position in the hash table
            value- a value type which should be stored with the key
        complexity:
            best case- O(1) when self.table[position] is None
            worst case- O(internal table.__setitem__) as it can be infinitely long until it meets a NoneType or a tuple

        """
        position = self.hash(key)
        self.count += 1
        if self.table[position] is None:
            self.table[position] = (key,value)
            return
        if isinstance(self.table[position],tuple):
            duplicate_pair = self.table[position]
            self.table[position] = InfiniteHashTable()
            self.table[position].level = self.level + 1
            self.table[position].__setitem__(duplicate_pair[0],duplicate_pair[1])
            self.table[position].__setitem__(key,value)
        elif isinstance(self.table[position],InfiniteHashTable):
            self.table[position].__setitem__(key,value)

    def __delitem__(self, key: K) -> None:
        """
        Deletes a (key, value) pair in our hash table.

        :raises KeyError: when the key doesn't exist.
        argument:
            key- a key type which determines the position in the hash table
        complexity:
            best case- O(self.__contain__) when it return False
            worst case- O(self.__contain__) + O(internal table.__delitem__) as it can be infinitely long until
                        it meets a tuple which is the (key, value) pair
        """
        if not self.__contains__(key):
           raise KeyError("Key doesn't exist.")
        position = self.hash(key)
        if self.count != 2:
            if isinstance(self.table[position],tuple):
                self.table[position] = None
                self.count -= 1
            elif isinstance(self.table[position],InfiniteHashTable):
                    if self.table[position].count != 2:
                        self.count -= 1
                        self.table[position].__delitem__(key)
                    else:
                        self.table[position] = self.table[position].__delitem__(key)
                        self.count -= 1
        else:
            if self.level != 0 :
                if isinstance(self.table[position],tuple):
                    self.table[position] = None
                    self.count -= 1
                    for item in self.table:
                        if isinstance(item,tuple):
                            return item
                elif isinstance(self.table[position],InfiniteHashTable):
                    self.table = self.table[position].table
                    self.level += 1
                    return self.__delitem__(key)
            else:
                if isinstance(self.table[position],tuple):
                    self.table[position] = None
                    self.count -= 1
                elif isinstance(self.table[position],InfiniteHashTable):
                    self.table[position] = self.table[position].__delitem__(key)
                    self.count -= 1

    def __len__(self):
        return self.count

    def __str__(self) -> str:
        """
        String representation.

        Not required but may be a good testing tool.
        """
        raise NotImplementedError()

    def get_location(self, key) -> list[int]:
        """
        Get the sequence of positions required to access this key.

        :raises KeyError: when the key doesn't exist.
        argument:
            key- a key type which determines the position in the hash table
        return:
            a list of integers which indicates the position of the key in the table
        complexity:
            best case- O(self.__contain__) when it return False
            worst case- O(internal table.get_location) as it can be infinitely long until it meets a tuple which is the
                        (key,value) pair
        """
        if not self.__contains__(key):
            raise KeyError("Key doesn't exist.")
        position = self.hash(key)
        if isinstance(self.table[position],tuple):
            return [position]
        if isinstance(self.table[position],InfiniteHashTable):
            return [position] + self.table[position].get_location(key)



    def __contains__(self, key: K) -> bool:
        """
        Checks to see if the given key is in the Hash Table

        :complexity: See linear probe.
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

