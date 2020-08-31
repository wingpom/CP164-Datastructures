"""
----------------------------------------
# Student Name:  Quynh Dao
# Student ID:    130440130
# Student email: daox0130@mylaurier.ca
#---------------------------------------
"""
from list import List 


# linear = O(n)
# BST - O(log n)
# ? = O(1)
# Hashing is not relevant to BST or searching, it's own concept
# Hashset is one of the applications for searching (Hashing) of mix types
#                      ------25-----
#                     /             \
#                   13 -             35-
#                 /     \           /   \
#               11      19        33     40 
#              /  \    /   \     /  \   /  \ 
#             9   12  18   20   30  34 38  44 
#                                 \
#                                 32
# Searching a tree: 2 ways
# DFS (recursion or stacks)
# Depth First Search (Go to the bottom then up): There are multiple ways for traverse a tree
# You can use Recursion vs Stacks
# 1. inorder
# 2. preorder
# 3. postorder
# BFS (Queues)
# BFS = Breadth First Search (Goes level by level)
# You can use Queues to solve 
# 1. levelorder
# DFS (inorder): Left, root, Right
# [9, 11, 12, 13, 18 19, 20, 25, 30, 32, 33, 34, 35, 38, 38, 40, 44]
# Visit every node and sorts the tree in ascending order
# DFS (preorder): root, left, right
# [25, 13, 11, 9, 12, 19, 18, 20, 35, 33, 30, 32, 34, 40, 38, 44]
# DFS (post order): left, right, root
# [9, 12, 11, 18, 20, 19, 13, 32, 30, 34, 33, 38, 44, 40, 35, 25]
# BFS (levelorder): going horizontal then left to right
# [25, 13, 35, 11, 19, 33, 40, 9, 12, 18, 20, 30, 34, 38, 44, 32]
# HASHING
# Given some data X, hashing is mash, crush and produces a hash digest
# X --> hash digest
# hash(x) --> hash digest
# Properties:
# - One way
# - hash digest << len(x), this you want the hash value to be much smaller then the original file
# - hash(y) != hash(x)
# i.e. windows_update_123 will publish the hash(windows_update_!23): 256 bits
# if the values match then is the same file uploaded by windows, some sort of verification
# shrink students data, and produce an unique number by hashing the key only
# python has built-in hash function
# HASHSET
# table
# size (number of slots) = 5
# count # count number of items
# load_factor = 3 # if the number of items in the hashset is 3*5 (load_factor * size)
# if count > (load_factor * size) then rehash
# student1 --> hash_value
#    find slot: hash_value % size (Number will be 0 to 5) --> assume 3
#    and so forth for student2, ... 
# For example, given the key look for student in hash table
# Linear search, go and visit every single item
# Binary search go thru very line
# We want a fixed number of steps
# First hash, do modulus size and we know it exists in the slot, then do linear search
# We'd gonna be a cap on how many students can fit a slot
# Slot 0:
# Slot 1: student2, student3
# Slot 2: student4, student5, student6
# Slot 3: student1
# Slot 4: student7
class HashSet:
    _DEFAULT_LOAD_FACTOR = 5

    # size is number of slots
    # load factor will determine when to expand the size
    def __init__(self, size, load_factor=_DEFAULT_LOAD_FACTOR):
        # Imported variables
        self._size = size 
        self._load_factor = load_factor 
        
        # Other variables
        self._table = []  # table is a python list
        self._count = 0  # no items in the list
        
        # Creating hashset (doesn't allow for duplicates)
        for _ in range(self._size):  # initialize to empty slots
            self._table.append(List())  # each slot is a empty list structure so we can add items
        return 
    
    def __len__(self):
        return self._count 
    
    def is_empty(self):
        return self._count == 0 
    
    def _find_slot(self, key):
        slot_num = hash(key) % self._size 
        return self._table[slot_num]
    
    def __contains__(self, key):
        slot = self._find_slot(key)
        return key in slot  # a slot is list and in operation is overloaded in list data structure
    
    def find(self, key):  # linear search, a limit to how much we can search, then there is rehashing to move key 
        slot = self._find_slot(key)
        value = slot.find(key)  # there a find method in list data structure
        return value
    
    def insert(self, item):
        slot = self._find_slot(item)  # find slot to insert at
        if item in slot:  # duplicates not allowed in a hashset
            inserted = False 
        else:
            slot.append(item)  # we use any adding method
            self._count += 1 
            inserted = True
            if self._count > (self._load_factor * self._size): 
                self._rehash() 
        return inserted
    
    def _rehash(self):
        # copy current data to a temporary table 
        temp_table = self._table
        # increase # slots
        self._size = (self._size * 2) + 1  # Uses odd number of slots, so mod isn't 0 such that we have an odd number
        # Create new table and slots 
        self._table = [] 
        for _ in range(self._size): 
            self._table.append(List())
        # copy data from temp_table to new table 
        while len(temp_table) > 0:
            old_slot = temp_table.pop(0)  # get a slot
            while not old_slot.is_empty():  # happening for all items in that slot
                # finding of the mod/new location and adding items to slots
                item = old_slot.pop(0) 
                slot = self._find_slot(item) 
                slot.append(item)
        return

    def _dehash(self):
        # copy current data to a temporary table 
        temp_table = self._table
        if self._size // 2 < self._load_factor and self._load_factor % 2 == 0:
            self._size = self._load_factor + 1
        elif self._size % 2 == 0:
            self._size = self._size // 2 + 1
        else:
            self._size = self._size // 2  

        self._table = [] 
        for _ in range(self._size): 
            self._table.append(List())
        # copy data from temp_table to new table 
        while len(temp_table) > 0:
            old_slot = temp_table.pop(0)  # get a slot
            while not old_slot.is_empty():  # happening for all items in that slot
                # finding of the mod/new location and adding items to slots
                item = old_slot.pop(0) 
                slot = self._find_slot(item) 
                slot.append(item)

    def remove(self, key):
        if self._count == 0:
            print('Error(HashSet.remove): Cannot remove from an empty hash set')
            return None 

        if self._count < (self._size * self._load_factor) / 3:
            self._dehash()
        slot = self._find_slot(key)
        item = slot.remove(key) 
        if item is not None: 
            self._count -= 1 
        return item 
    
    def __iter__(self):
        for slot in self._table:  # goes through every slot
            for item in slot:  # goes through every item in that slot
                yield item 
        return
                
    def __str__(self): 
        output = "Hashset(count) = {}\n".format(str(self._count))
        i = 0 
        for slot in self._table: 
            output += "Slot {}: ".format(str(i))
            if not slot.is_empty():
                for item in slot:
                    output += '{} , '.format(str(item))
                output = "{}\n".format(output[:-3]) 
            else:
                output += '\n' 
            i += 1  
        return output
    
