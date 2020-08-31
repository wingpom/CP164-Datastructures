"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""
from copy import deepcopy


class List:
    """
    ----------------------------------------------
    Ordered Indexed Unsorted List
    Array Implementation
    ----------------------------------------------
    """

    def __init__(self):
        """
        -------------------------------------------------------
        Description:
            Creates an empty list
        Assert: none
        Use: my_list = List()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An object of type List       
        -------------------------------------------------------
        """
        self._items = []

    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Compute number of items in a list
        Assert: none
        Use: length = len(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            length: number of items in the        
        -------------------------------------------------------
        """
        return len(self._items)  # len is an operator, no dot method used
    
    def append(self, item):
        """
        -------------------------------------------------------
        Description:
            Adds given item to the tail of the list
        Assert: none
        Use: list1.append(item)
        -------------------------------------------------------
        Parameters:
            item: an arbitrary item to add to list
        Returns:
            No returns        
        -------------------------------------------------------
        """
        # self._items.append(item) is an method and violating our rules
        self._items += [deepcopy(item)]
        return
    
    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Description:
            Private helper method to search for first occurrence
                of the key in the list.
            returns key index if found, -1 otherwise
        Assert: none
        Use: indx = self._linear_search(item)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            indx: position of key in the list (int)
        -------------------------------------------------------
        """
        indx = -1
        for i in range(len(self)):
            if self._items[i] == key:
                indx = i
                break
        return indx
    
    def __iter__(self):
        """
        -------------------------------------------------------
        Description:
            Generates a Python iterator.
            Iterates from item at index 0 to end of list
        Assert: none
        Use: for item in list1:
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            item - the next value in the list (?)
        -------------------------------------------------------
        """
        # for item in list1: there is some iterator that iterates through any iterable object
        #     print(items)
        # list1 = List1()
        # for item in list1... overload the iterator
        for item in self._items:
            yield item  # continue where you stop last item after returning the first item through yield
            # return goes from the start and once returned restarts again
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns a string representation of list
            format: [item1, item2, item3, ...]
        Assert: none
        Use: str(list1) or print(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string representation of the list (str)
        -------------------------------------------------------
        """
        if self.is_empty():
            return '[]'
        output = '['
        for item in self: 
            output += str(item) + ','
        return output[:-1] + ']'
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            Compute number of items in a list
        Assert: none
        Use: result = list1.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if list is empty, False otherwise (bool) 
        -------------------------------------------------------
        """
        # already overload the len operator so we can use it
        return len(self) == 0
    
    def __contains__(self, key):
        """
        -------------------------------------------------------
        Description:
            Returns True if list contains an item in the list that
                matches given key, returns False otherwise
        Assert: none
        Use: result = key in list1
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            result: True/False
        -------------------------------------------------------
        """
        return self._linear_search(key) != -1 
 
    def _is_valid_index(self, i):  # helper function
        """
        -------------------------------------------------------
        Description:
            Private helper method to validate an index value
            Valid python list values are -len(list) to len(list)-1
        Assert: i is an integer
        Use: result = self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i: an index value (int)
        Returns:
            result: True if valid index and False otherwise (bool)        
        -------------------------------------------------------
        """
        # a = [1,2,3]
        # what are the valid index, index 0,1,2 and also -1,-2,-3
        # range from negative of the length and positive len(List)-1
        assert isinstance(i, int), 'invalid i'
        return i < len(self) and i >= len(self) * (-1)
    
    def index(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds location of a value by key in list.
            Returns the position of the item that match given key
            Returns -1 if not found
        Assert: No asserts
        Use: i = list1.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - location of key in the list (int)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        return i

    def __getitem__(self, i):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of the ith element of the list
        Assert: i is an integer and is a valid index
        Use: item = list1[i]
        -------------------------------------------------------
        Parameters:
            i: an index value (int)
        Returns:
            result: copy of ith element in list (?)      
        -------------------------------------------------------
        """
        assert isinstance(i, int) and self._is_valid_index(i), 'invalid i'
        return deepcopy(self._items[i])

    def pop(self, i):
        """
        -------------------------------------------------------
        Description:
            removes item at position i and return a copy
            If invalid index, print error message and return None
        Assert: no asserts
        Use: list1.pop(i)
        -------------------------------------------------------
        Parameters:
            i - index of the element to pop (int)
        Returns:
            item: copy of item at position i (?)    
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(List.pop): List is empty')
            return None
        if not self._is_valid_index(i):
            print('Error(List.pop): Invalid value of i')
            return None
        return self.remove(self[i])
    
    def remove(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds, removes, and returns the value in list that matches key.
            if key not found returns None
            If list is empty, prints an error message and returns None
        Assert: none
        Use: item = list1.remove(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            item: the full item matching key (?)
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(List.remove): Cannot remove from an empty list')
            return None
        i = self._linear_search(key)
        if i == -1:
            item = None
        else:
            item = deepcopy(self._items[i])
            self._items = self._items[:i] + self._items[i + 1:]
        return item

    def clear(self):
        """
        -------------------------------------------------------
        Description:
            removes all items in current List
        Assert: no asserts
        Use: list1.clear()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        for item in self:
            self.remove(item)
        return
    
    """---------------------- Task 1 ------------------------"""

    def extend(self, list2):
        """
        -------------------------------------------------------
        Description:
            append list2 to the current list
            if given parameter is not of type List, 
                print error message and return
        Assert: none
        Use: list1.extend(list1)
        -------------------------------------------------------
        Parameters:
            list2: a List object to be appended to current list(List)
        Returns:
            No returns
        -------------------------------------------------------
        """
        assert isinstance(list2, List), 'invalid list'
        for i in range(len(list2)):
            self._items += [deepcopy(list2[i])]
        return
    
    """---------------------- Task 2 ------------------------"""

    def swap(self, i, j):
        """
        -------------------------------------------------------
        Description:
            Swaps item at position i with item at position j
            if invalid i or j print error message
        Assert: assert i and j are integers
        Use: list1.swap(i,j)
        -------------------------------------------------------
        Parameters:
            i: index of first swap item (int)
            j: index of second swap item(int)
        Returns:
            No returns
        -------------------------------------------------------
        """
        if isinstance(j, int) and not self._is_valid_index(j):
            print('Error(List.swap): invalid j')
        elif isinstance(i, int) and not self._is_valid_index(i):
            print('Error(List.swap): invalid i')
        elif self._is_valid_index(j) and self._is_valid_index(i):
            self._items[i], self._items[j] = deepcopy(self._items[j]), deepcopy(self._items[i])
        return
    
    """---------------------- Task 3 ------------------------"""

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Description:
            Removes all items in list which match given key
            if list is empty, print error message and return
            Returns a single copy of removed item
            if item not found prints an error message and return None
        Assert: no asserts
        Use: item = list1.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key: partial data (?)
        Returns:
            item: copy of removed item (?)
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(List.remove_many): list is empty')
            return None
        i = self._linear_search(key)
        if i == -1:
            print('Error(List.remove_many): key not found')
            return None
        else:
            item = deepcopy(self._items[i])
            for item in self:
                if item == key:
                    self.remove(deepcopy(item))
        # self._items = [item for item in self if item != key]
        return item
    
    """---------------------- Task 4 ------------------------"""

    def split(self):
        """
        -------------------------------------------------------
        Description:
            Splits list into two parts. 
            ls contains the first half,
            rs the second half. 
            Current list becomes empty.
            If current list is empty, print error message 
                and return two empty lists
        Use: ls, rs = l.split()
        Assert: no asserts
        Use: ls,rs = list1.split()
        -------------------------------------------------------
        Parameters:
            no parameters
        Returns:
            ls - a new List with >= 50% of the original List (List)
            rs - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        ls = List()
        rs = List()
        
        if len(self) % 2 == 0:
            half = len(self) // 2
        else:
            half = len(self) // 2 + 1
            
        for item in self._items[:half]:
            ls.append(item)
            
        for item in self._items[half:]:
            rs.append(item) 
        
        self.clear()
        
        return ls, rs
    
    """---------------------- Task 5 ------------------------"""

    def reverse(self):
        """
        -------------------------------------------------------
        Description:
            Reverses the order of elements in the list
            if list is empty do nothing
        Use: ls, rs = l.split()
        Assert: no asserts
        Use: list1.reverse()
        -------------------------------------------------------
        Parameters:
            no parameters
        Returns:
            no returns
        -------------------------------------------------------
        """
        ls, rs = self.split()
        
        for i in range(len(rs) - 1, -1, -1):
            self._items += deepcopy([rs[i]])
        
        for i in range(len(ls) - 1, -1, -1):
            self._items += deepcopy([ls[i]])
            
        return
    
    """---------------------- Task 6 ------------------------"""
    
    def __add__(self, list2):
        """
        -------------------------------------------------------
        Description:
            Overloads + operator to allow list1 + list2
            contents of list1 and list2 is not changed
        Assert: list2 is of type list
        Use: list3 = list1 + list2
        -------------------------------------------------------
        Parameters:
            list2: a List object to be added to current list(List)
        Returns:
            list3: result of list1 + list2 (list)
        -------------------------------------------------------
        """
       
        assert isinstance(list2, List), 'invalid list2'
        result = List()
        
        for item in self:
            result.append(item)
            
        for item in list2:
            result.append(item) 
        
        return result
