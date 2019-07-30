"""
Python implementation of a hash table.
"""


class HashTable:
    def __init__(self):
        self.data = {}

    def hash(self, val):
        """
        Calculates the val key in the hash table.

        Returns int index.
        """
        split_val = list(val)
        ascii_tot = 0
        data_length = len(self.data.items)
        
        for c in split_val:
            ascii_tot += ord(c)

        # Modulo / Remainder if there is data else just place it in arbitary first
        return ascii_tot - (ascii_tot // data_length) * data_length if data_length else 1

    def store(self, value):
        hash_index = self.hash(value)
        
        try:
            current = self.data[hash_index]
            current.append(value)
        except KeyError:
            current = [value]
            self.data[hash_index] = current
        
        return current

    def find(self, value):
        hash_index = self.hash(value)
        
        try:
            result = self.data[hash_index]
        except KeyError:
            print("Value doesn't exist!")
            return None
        finally:
            for i in result:
                if i == value:
                    return i

    def __repr__(self):
        return str(self.data)
