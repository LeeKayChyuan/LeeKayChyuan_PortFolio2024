# Assignment 2 task 1
# Referenced from week 10 tutor video, chat gpt
class Node:
    def __init__(self):
        """
        Initialize the attributes of a Node with 5 possible links (A-D)
        
        :Time Complexity: O(1)
        :Space Complexity: O(1)
        """
        
        self.links = [None] * 4     # a list of 4 possible child nodes
        self.indexes = []   # a list of starting indexes passing through this node.

    def insert(self, text, start_index, current_index):
        """
        Insert a suffix into the trie recursively

        :param text: A string.
        :param start_index: The starting index of the suffix.
        :param current_index: The current index.
        :Time Complexity: O(N) where N is the length of the text.
        :Time Complexity Analysis: It recursive on each character of text
        :Space Complexity: O(N) where N is the length of the text.
        :Space Complexity: Each character's node created.
        """
        if len(text) > current_index :  # Base case
            chr_index = ord(text[current_index]) - ord('A')
            if not self.links[chr_index]:
                self.links[chr_index] = Node()
            self.links[chr_index].insert(text, start_index, current_index + 1)
        self.indexes.append(start_index)

    def search(self, key, key_index):
        """
        Search for a key in the trie using recursive.

        :param key_index: The current index of the key.
        :return: A list of indexes if the key is found, None if not found.
        :Time Complexity: O(N) where N is the length of the key.
        :Time Complexity Analysis: Check on each character of the key recursively.
        :Space Complexity: O(1).
        :Space Complexity: No addition space needed.
        """
        if key_index == len(key):
            return self.indexes
        chr_index = ord(key[key_index]) - ord('A')
        if self.links[chr_index]:
            return self.links[chr_index].search(key, key_index + 1)
        return None


class Trie:
    def __init__(self, text):
        """
        Initialize a Trie and insert all suffixes of the given text.

        :param text: The text to create the trie.
        :Time Complexity: O(N^2), N is the length of the text.
        :Time Complexity Analysis: Inserts each of the N suffixes by looping.
        :Space Complexity: O(N^2), as each suffix creates a new path in the trie.
        :Space Complexity Analysis: Each node represents a character in the suffix.
        """
        self.root = Node()
        for i in range(len(text)):
            self.root.insert(text, i, i)

    def search(self, value):
        """
        Search for a value in the trie.

        :param value: The value to search for.
        :return: A list of starting positions where the value is found, or an empty list if not found.
        :Time Complexity: O(N) where N is the length of the value.
        :Time Complexity Analysis: Recurses on each character of the value.
        :Space Complexity: O(1) as no additional space is required beyond the result list.
        """
        result = self.root.search(value, 0)
        if result:
            val_len = len(value)
            positions = []
            for i in result:
                positions.append(i)
            return positions
        else:
            return []


class OrfFinder:
    def __init__(self, genome):
        """
        Initialize an OrfFinder.

        :param genome: The genome that have characters in between [A-D].
        :Time Complexity: O(N^2) where N is the length of the genome.
        :Time Complexity Analysis: Creates two suffix tries, each take O(N^2) time.
        :Space Complexity: O(N^2) where N is the length of the genome.
        :Space Complexity Analysis: Node is created for each character in the genome.
        """
        self.genome = genome
        self.suffix_trie = Trie(genome)
        self.reversed_suffix_trie = Trie(genome[::-1])

    def find(self, start, end):
        """
        Find all substrings in the genome that start and end with provided sequence.

        :param start: The starting of the sequence.
        :param end: The ending of the sequence.
        :return: A list of substrings that start and end with the provided sequence.
        :Time Complexity: O(N + M + V) where N is the length of the starting sequence,
                          M is the length of the ending sequence, and V is the number of characters
                          in the output list.
        :Time Complexity Analysis: Searches for start and end sequences and constructs the result list.
        :Space Complexity: O(N) where N is the total length of the substrings found.
        :Space Complexity Analysis: Stores substrings found in the genome.
        """
        starting_index = self.suffix_trie.search(start)
        ending_index = self.reversed_suffix_trie.search(end[::-1])
        result_genome = []
        for starting in starting_index:
            for ending in ending_index:
                end_index = len(self.genome) - ending - 1
                if starting + len(start) + len(end) <= end_index + 1:
                    # Manually construct the substring
                    orf = []
                    for i in range(starting, end_index + 1):
                        orf.append(self.genome[i])
                    result_genome.append(''.join(orf))
        return result_genome