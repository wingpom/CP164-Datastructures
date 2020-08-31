"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""

from copy import deepcopy


class Node:
    """
    ----------------------------------------------
    Implementation of a Linked List node
    ----------------------------------------------
    """

    def __init__(self, item, next_node):
        """
        -------------------------------------------------------
        Description:
            Creates and initializes an empty linked list node
            data and next set to given values
        Assert: none
        Use: my_node = Node()
        -------------------------------------------------------
        Parameters:
            item: An arbitrary object (?)
            next_node: reference to another node
        Returns:
            An object of type Node 
        -------------------------------------------------------
        """ 
        self._data = deepcopy(item)
        self._next_node = next_node
        return
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns string representation of node
            Used for testing purposes
        Assert: none
        Use: str(my_node) or print(my_node)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string represenation of node 
        -------------------------------------------------------
        """
        return str(self._data)

    
class Linked_List:
    """
    ----------------------------------------------
    Ordered Indexed Unsorted List
    Linked List Implementation
    ----------------------------------------------
    """

    def __init__(self):
        """
        -------------------------------------------------------
        Description:
            Creates an empty linked list
            head is initialized to None
        Assert: none
        Use: my_list = Linked_list()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An object of type Linked_List       
        -------------------------------------------------------
        """ 
        self._front = None
        self._count = 0
        return
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns a string representation of linked list
            format: [item1, item2, item3, ...]
        Assert: none
        Use: str(list1) or print(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string representation of linked list (str)
        -------------------------------------------------------
        """
        if self._front is None:
            return '[]'
        output = '['
        current_node = self._front
        while current_node is not None:
            output += str(current_node._data) + ','
            current_node = current_node._next_node
        return output[:-1] + ']'

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Description:
            Private helper method to search for first occurrence
                of the key in the linked list.
            returns key index if found, -1 otherwise
        Assert: none
        Use: p, c, i = self._linear_search(item)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            p: pointer to the node previous to the one containing key (Node)
            c: pointer to the node containing the key (Node) 
            i: index of the node containing key (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0

        while current is not None and current._data != key:
            previous = current
            current = current._next_node
            index += 1

        if current is None:
            index = -1
            previous = None

        return previous, current, index
        
    def _is_valid_index(self, i):
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
        assert isinstance(i, int), 'invalid i'
        return i < self._count and i >= self._count * -1

    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            Check if linked list is empty
        Assert: none
        Use: result = list1.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if list is empty, False otherwise (bool) 
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Returns number of items in a list
            same as number of nodes
        Assert: none
        Use: length = len(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            length: number of items in the linked list       
        -------------------------------------------------------
        """
        return self._count

    """---------------- Task 1 -------------------------"""

    def insert_front(self, item):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the list.
        Use: l.insert_front(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element. (?)
        Postconditions:
            value is added to the front of the list.
        -------------------------------------------------------
        """
        new_node = Node(item, self._front)
        self._front = new_node
        self._count += 1
        return
    
    """---------------- Task 2 -------------------------"""

    def remove_front(self):
        """
        -------------------------------------------------------
        Description:
            Removes and returns the first value in linked list that matches key.
            if list is empty, print an error messange and return None      
        Assert: none
        Use: item = list1.remove_front()
        -------------------------------------------------------
        Parameters:
            No input parameters
        Returns:
            item: copy of first item in linked list (?)
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(Linked_List.remove_front): Cannot remove from an empty linked list')
            return None
        self._front = self._front._next_node
        self._count -= 1
        if self._front is None:
            return None
        else:
            item = self._front._data
        return item
    
    """---------------- Task 3 -------------------------"""

    def __setitem__(self, i, item):
        """
        -------------------------------------------------------
        Description:
            Places a copy of given item into the linked list at position i
        Assert: i is an integer and is a valid index
        Use: list1[i] = item
        -------------------------------------------------------
        Parameters:
            i - index of the element to modify (int)
            item - an item which value will be assigned to the ith element in list (?)
        Returns:
            No returns     
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'invalid i'
        if i < 0:
            i = self._count + i
        
        curr = self._front
        location = 0
        
        while curr is not None and location < i:
            curr = curr._next_node
            location += 1
        curr._data = item
        return
        
    """---------------- Task 4 -------------------------"""

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds and removes all items in linked list that match given key
        Assert: no asserts
        Use: list1.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - partial data to search for (?)
        Returns:
            No returns     
        -------------------------------------------------------
        """
        previous_node = None
        current_node = self._front
        
        while current_node is not None:
            if current_node._data == key:
                if  previous_node == None:
                    current_node = current_node._next_node
                else:
                    previous_node._next_node = current_node._next_node
                self._count -= 1
            previous_node = current_node
            current_node = current_node._next_node
        return
    
    """---------------- Task 5 -------------------------"""

    def max(self):
        """
        -------------------------------------------------------
        Description:
            Finds the item with the maximum value in the linked list
        Assert: linked list is not empty
        Use: max_data = list1.max()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            max_data: copy of the item with the maximum value    
        -------------------------------------------------------
        """
        assert not self.is_empty(), 'invalid linked list'
        max_data = self._front._data
        current_node = self._front
        while current_node is not None:
            if max_data < current_node._data:
                max_data = current_node._data
            current_node = current_node._next_node
        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Description:
            Finds the item with the minimum value in the linked list
        Assert: linked list is not empty
        Use: min_data = list1.min()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            min_data: copy of the item with the minimum value    
        -------------------------------------------------------
        """
        assert not self.is_empty(), 'invalid linked list'
        min_data = self._front._data
        current_node = self._front
        while current_node is not None:
            if min_data > current_node._data:
                min_data = current_node._data
            current_node = current_node._next_node
        return min_data
    
    """---------------- Task 6 -------------------------"""

    def copy(self):
        """
        -------------------------------------------------------
        Description:
            Duplicates the current linked list to a new linked list
                with same order and content
        Assert: no asserts
        Use: list2 = list1.copy()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            list2: a copy of current linked list (Linked_List)    
        -------------------------------------------------------
        """
        list2 = Linked_List()
        
        if self._front is not None:
            new_node = Node(self._front._data, None)
            list2._front = new_node
            current_node = self._front._next_node
            list2_node = list2._front
            list2._count += 1
            
            while current_node is not None:
                new_node = Node(current_node._data, None)
                list2_node._next_node = new_node
                current_node = current_node._next_node
                list2_node = new_node
                list2._count += 1
                
        return list2
    
