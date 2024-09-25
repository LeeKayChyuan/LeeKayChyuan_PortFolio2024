from __future__ import annotations

from typing import Generic, TypeVar, Iterator
from data_structures.hash_table import LinearProbeTable, FullError
from data_structures.referential_array import ArrayR

K1 = TypeVar('K1')
K2 = TypeVar('K2')
V = TypeVar('V')

class DoubleKeyTable(Generic[K1, K2, V]):
    """
    Double Hash Table.

    Type Arguments:
        - K1:   1st Key Type. In most cases should be string.
                Otherwise `hash1` should be overwritten.
        - K2:   2nd Key Type. In most cases should be string.
                Otherwise `hash2` should be overwritten.
        - V:    Value Type.

    Unless stated otherwise, all methods have O(1) complexity.
    """

    # No test case should exceed 1 million entries.
    TABLE_SIZES = [5, 13, 29, 53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241, 786433, 1572869]

    HASH_BASE = 31

    def __init__(self, sizes:list|None=None, internal_sizes:list|None=None) -> None:

        if sizes is not None:
            self.TABLE_SIZES = sizes
        if internal_sizes is not None:
            self.internal_TABLE_SIZES = internal_sizes
        else:
            self.internal_TABLE_SIZES = self.TABLE_SIZES
        self.size_index = 0
        self.TLtable = ArrayR(self.TABLE_SIZES[self.size_index])
        self.count = 0


    def hash1(self, key: K1) -> int:
        """
        Hash the 1st key for insert/retrieve/update into the hashtable.

        :complexity: O(len(key))
        """

        value = 0
        a = 31415
        for char in key:
            value = (ord(char) + a * value) % self.table_size
            a = a * self.HASH_BASE % (self.table_size - 1)
        return value

    def hash2(self, key: K2, sub_table: LinearProbeTable[K2, V]) -> int:
        """
        Hash the 2nd key for insert/retrieve/update into the hashtable.

        :complexity: O(len(key))
        """

        value = 0
        a = 31415
        for char in key:
            value = (ord(char) + a * value) % sub_table.table_size
            a = a * self.HASH_BASE % (sub_table.table_size - 1)
        return value

    def _linear_probe(self, key1: K1, key2: K2, is_insert: bool) -> tuple[int, int]:
        """
        Find the correct position for this key in the hash table using linear probing.

        :raises KeyError: When the key pair is not in the table, but is_insert is False.
        :raises FullError: When a table is full and cannot be inserted.
        argument:
            key1 - the first key of the key pair to determine the hash of the top-level table
            key2 - the second key of the key pair to determine the hash of the internal table
            is_insert - boolean that indicates whether the key pair will be inserted into the table or not
        return:
            a tuple of integers which indicates the position of the key pair
        complexity:
            best case- O(hash1) + O(1)*O(LP) where hash1 is the complexity of hash1 function
                       and LP is the complexity of linear probe function of internal LPtable
            worst case- O(hash1) + O(N)*O(LP) where N is the table size of the top level table
        """
        position1 = self.hash1(key1)
        for _ in range(self.table_size):
            if self.TLtable[position1] is None:
                if is_insert:
                    self.TLtable[position1] = LinearProbeTable(self.internal_TABLE_SIZES)
                    self.count += 1
                    self.TLtable[position1].hash = lambda k: self.hash2(k[1], self.TLtable[position1])
                    position2 = self.TLtable[position1]._linear_probe((key1, key2), is_insert)
                    return (position1, position2)
                else:
                    raise KeyError("Key pair is not in table,but is_insert is False.")
            #line 89-98 will be used to pass the test case in line 30 & 31 of test_double_hash,as a LinearProbeTable is created
            #in line 30 without inserting any (key,value) in it, occupying a space of TLtable and line 31 will return FullError
            #if without this implementation
            elif self.TLtable[position1].count == 0:
                if is_insert:
                    self.TLtable[position1] = LinearProbeTable(self.internal_TABLE_SIZES)
                    self.count += 1
                    self.TLtable[position1].hash = lambda k: self.hash2(k[1], self.TLtable[position1])
                    position2 = self.TLtable[position1]._linear_probe((key1, key2), is_insert)
                    return (position1, position2)
                else:
                    raise KeyError("Key pair is not in table,but is_insert is False.")
            else:
                for i in range(self.TLtable[position1].table_size):
                    if self.TLtable[position1].array[i] is not None:
                        if self.TLtable[position1].array[i][0][0] != key1:
                            position1 = (position1 + 1) % self.table_size
                            break
                        else:
                            position2 = self.TLtable[position1]._linear_probe((key1,key2),is_insert)
                            return (position1,position2)
        if is_insert:
            raise FullError("Table is full.")
        else:
            raise KeyError("Key pair is not in table but is_insert is False.")

    def iter_keys(self, key:K1|None=None) -> Iterator[K1|K2]:
        """
        key = None:
            Returns an iterator of all top-level keys in hash table
        key = k:
            Returns an iterator of all keys in the bottom-hash-table for k.
        complexity:
            best case- O(N) where N is the table size of the top-level table
                        when key is None and only 1 internal table found in the top-level table,and the key is in the
                        0 postion of the internal table
            worst case- O(N*n) where n is the table size of the internal table
        """
        for table in self.TLtable:
            if isinstance(table,LinearProbeTable):
                for item in table.array:
                    if item is not None:
                        if key is None:
                            yield item[0][0]
                            break
                        elif item[0][0] == key:
                            yield item[0][1]
    def keys(self, key:K1|None=None) -> list[K1]:
        """
        key = None: returns all top-level keys in the table.
        key = x: returns all bottom-level keys for top-level key x.
        complexity:
            best case: O(N) where N is the length of the top-level table
            worst case: O(N*n) where n is the length of the table.array
        """
        key_lst = []
        for table in self.TLtable:
            if isinstance(table,LinearProbeTable):
                for item in table.array:
                    if item is not None:
                        if key is None:
                            key_lst.append(item[0][0])
                            break
                        elif item[0][0] == key:
                            key_lst.append(item[0][1])
        return key_lst
    def iter_values(self, key:K1|None=None) -> Iterator[V]:
        """
        key = None:
            Returns an iterator of all values in hash table
        key = k:
            Returns an iterator of all values in the bottom-hash-table for k.
        complexity:
            best case- O(hash1) + O(n) where n is the length of the internal array
            worst case- O(N*n) where N is the length of the top-level table
        """
        for table in self.TLtable:
            if isinstance(table, LinearProbeTable):
                for item in table.array:
                    if item is not None:
                        if key is None:
                            yield item[1]
                        elif item[0][0] == key:
                            yield item[1]

    def values(self, key:K1|None=None) -> list[V]:
        """
        key = None: returns all values in the table.
        key = x: returns all values for top-level key x.
        complexity:
            best = worst = O(N*n) where N,n are the length of the top-level table and internal array respectively.
        """
        value_lst = []
        for table in self.TLtable:
            if isinstance(table, LinearProbeTable):
                for item in table.array:
                    if item is not None:
                        if key is None:
                            value_lst.append(item[1])
                        elif item[0][0] == key:
                            value_lst.append(item[1])
        return value_lst

    def __contains__(self, key: tuple[K1, K2]) -> bool:
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

    def __getitem__(self, key: tuple[K1, K2]) -> V:
        """
        Get the value at a certain key
        :raises KeyError: when the key doesn't exist.
        argument:
            key - a tuple of keys which also represents a key pair
        return:
            V- the value with respect to the key
        complexity:
             O(linear_probe)+O(internal array.__getitem__)
        """
        position = self._linear_probe(key[0],key[1],False)
        return self.TLtable[position[0]].__getitem__(key)

    def __setitem__(self, key: tuple[K1, K2], data: V) -> None:
        """
        Set an (key, value) pair in our hash table.
        argument:
            key- a tuple of keys which also represents a key pair
            data- a value which should be stored with the key as a pair
        complexity:
            best = O(linear_probe) + O(internal_array.__setitem__)
            worst = O(linear_probe) + O(internal_array.__setitem__) + O(rehash)
        """
        position = self._linear_probe(key[0], key[1], True)
        self.TLtable[position[0]].__setitem__(key,data)

        if len(self) > self.table_size / 2:
            self._rehash()

    def __delitem__(self, key: tuple[K1, K2]) -> None:
        """
        Deletes a (key, value) pair in our hash table.

        :raises KeyError: when the key doesn't exist.
        argument:
            key- a tuple of keys which also represent a key pair
        complexity:
            O(linear_probe) + O(internal__delitem__)
        """
        position = self._linear_probe(key[0],key[1],False)
        self.TLtable[position[0]].__delitem__(key)
        if self.TLtable[position[0]].count == 0:
            self.TLtable[position[0]] = None

    def _rehash(self) -> None:
        """
        Need to resize table and reinsert all values

        :complexity best: O(N*hash(K)) No probing.
        :complexity worst: O(N*hash(K) + N^2*comp(K)) Lots of probing.
        Where N is len(self)
        """
        old_TLtable = self.TLtable
        self.size_index += 1
        if self.size_index == len(self.TABLE_SIZES):
            # Cannot be resized further.
            return
        self.TLtable = ArrayR(self.TABLE_SIZES[self.size_index])
        self.count = 0
        table_lst = []
        for table in old_TLtable:
            if isinstance(table,LinearProbeTable):
                table_lst.append(table)
        for table_ in table_lst:
            for item in table_.array:
                if item is not None:
                    key,data = item
                    self[key] = data

    @property
    def table_size(self) -> int:
        """
        Return the current size of the table (different from the length)
        """
        return len(self.TLtable)
    def __len__(self) -> int:
        """
        Returns number of elements in the hash table
        """
        return self.count

    def __str__(self) -> str:
        """
        String representation.

        Not required but may be a good testing tool.
        """
        raise NotImplementedError()
