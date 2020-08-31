"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""
from copy import deepcopy


class Node:
    """
    ----------------------------------------------
    Implementation of a Doubly Linked List node
    ----------------------------------------------
    """

    def __init__(self, previous_node, next_node, item):
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
            next_node: reference to next node
            previous_node: reference to previous ndoe
        Returns:
            An object of type Node 
        -------------------------------------------------------
        """ 
        self._data = deepcopy(item)
        self._next_node = next_node
        self._previous_node = previous_node
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


class Doubly_Linked_List:
    """
    ----------------------------------------------
    Doubly Linked List Implementation
    Ordered Indexed Unsorted
    ----------------------------------------------
    """

    def __init__(self):
        """
        -------------------------------------------------------
        Description:
            Creates an empty doubly linked list
            front and rear set to None and count to 0
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
        self._rear = None
        self._count = 0
        return
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns a string representation of linked list
            format: [item1, item2, item3, ...]
            Used for testing
        Assert: none
        Use: str(list1) or print(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string representation of doubly linked list (str)
        -------------------------------------------------------
        """
        if self._front is None:
            return '[]'
        output = '['
        current = self._front
        while current is not None:
            output += str(current._data) + ','
            current = current._next_node
        output = output[:-1] + ']'
        return output

    """
    ---------------------------------------------
        These functions are given and could be used in your solution
    ---------------------------------------------
    """

    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            Check if doubly linked list is empty
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
            Returns number of items in a doubly linked list
            same as number of nodes
        Assert: none
        Use: length = len(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            length: number of items in the doubly linked list       
        -------------------------------------------------------
        """
        return self._count
    
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of first item in doubly linked list.
            If list is empty, prints error message and returns None
        Assert: none
        Use: item = list1.peek()
        -------------------------------------------------------
        Parameters:
            No parametrs
        Returns:
            item: copy of first tiem in linked list (?)
        -------------------------------------------------------
        """
        if self._front is None:
            print('Error(Doubly_Linked_List.peek): Cannot peek at an empty list')
            return None
        return deepcopy(self._front._data)
    
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
    
    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Description:
            Private helper method to search for first occurrence
                of the key in the doubly linked list.
            returns key index if found, -1 otherwise
        Assert: none
        Use: c, i = self._linear_search(item)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            c: pointer to the node containing the key (Node) 
            i: index of the node containing key (int)
        -------------------------------------------------------
        """
        current = self._front
        index = 0
 
        while current is not None and current._data != key:
            current = current._next_node
            index += 1
 
        if current is None:
            index = -1
 
        return current, index
        
    """---------------------------------------------
                        Task 1
    ---------------------------------------------"""

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Description:
            Adds given item to the tail of the doubly linked list
        Assert: none
        Use: dlist.insert_rear(item)
        -------------------------------------------------------
        Parameters:
            item: an arbitrary item to add to linked list (?)
        Returns:
            No returns        
        -------------------------------------------------------
        """
        new_node = Node(None, None, value)
        if self._front is None:
            self._front = new_node
            self._rear = new_node
            self._rear._next_node = None
            self._front._previous_node = None
        else:
            self._rear._next_node = new_node
            new_node._previous_node = self._rear
            self._rear = new_node
            self._rear._next_node = None
        self._count += 1
        return
    
    """---------------------------------------------
                        Task 2
    ---------------------------------------------"""

    def insert_front(self, item):
        """
        -------------------------------------------------------
        Description:
            Adds given item to the head of the doubly linked list
        Assert: none
        Use: dlist.insert_front(item)
        -------------------------------------------------------
        Parameters:
            item: an arbitrary item to add to linked list (?)
        Returns:
            No returns        
        -------------------------------------------------------
        """
        new_node = Node(None, None, item)
        new_node._next_node = self._front
        if self._front is None:
            self._front = new_node
            self._rear = new_node
            self._rear._next_node = None
            self._front._previous_node = None
        else:
            self._front._previous_node = new_node
            new_node._next_node = self._front
            new_node._previous_node = None
            self._front = new_node
        self._count += 1
        return
    
    """---------------------------------------------
                      Task 3
    ---------------------------------------------"""

    def insert(self, i, item):
        """
        -------------------------------------------------------
        Description:
            inserts a copy of given item into the doubly linked list at index i
            works for positive and negative values of i
            if i is outside the range of indices --> append
        Assert: i is an integer
        Use: list1.insert(i,item)
        -------------------------------------------------------
        Parameters:
            i - position of the given item to be inserted at (int)
            item - an item to be added (?)
        Returns:
            No returns     
        -------------------------------------------------------
        """
        new_node = Node(None, None, item)
        current_node = self._front
        if i < 0:
            if i * (-1) > self._count:
                i = self._count
            i = self._count + i
            
        if i == 0:
            if self._front is None:
                self._front = new_node
                self._rear = new_node
                self._rear._next_node = None
                self._front._previous_node = None
            else:
                self._front._previous_node = new_node
                new_node._next_node = self._front
                new_node._previous_node = None
                self._front = new_node
        else:
            location = 0
            current_node = self._front
            previous_node = self._front
            
            while location < i and current_node is not None:
                previous_node = current_node
                current_node = current_node._next_node
                location += 1
                
            if i == location:
                new_node._next_node = current_node
                new_node._previous_node = previous_node
                previous_node._next_node = new_node
                
            if current_node is None:
                self._rear._next_node = new_node
                new_node._previous_node = self._rear
                self._rear = new_node
                self._rear._next_node = None
                
        self._count += 1
        return
    
    """---------------------------------------------
                      Task 4
    ---------------------------------------------"""    

    def extend(self, list2):
        """
        -------------------------------------------------------
        Description:
            Adds all items from list2 to tail of current list
            list2 becomes empty
        Assert: list2 is of type Doubly_Linked_List and is not self
        Use: list1.extend(list2)
        -------------------------------------------------------
        Parameters:
            list2: a doubly linked list (Doubly_Linked_List)
        Returns:
            No returns        
        -------------------------------------------------------
        """
        if self._front is None or list2._front is None:
            return 
        current_node = self._front
        while current_node._next_node is not None:
            current_node = current_node._next_node
            
        current_node._next_node = list2._front
        list2._front = None
        return
    
    """---------------------------------------------
                      Task 5
    ---------------------------------------------"""

    def remove_rear(self):
        """
        -------------------------------------------------------
        Description:
            removes and returns copy of last item in the doubly linked list
            if empty list, prints an error message and returns None
        Assert: none
        Use: item = dlist.remove_rear()
        -------------------------------------------------------
        Parameters:
            No input parameters
        Returns:
            item: copy of last item in the doubly linked list
        -------------------------------------------------------
        """
        item = None
        if self.is_empty():
            print('Error(Doubly_Linked_List.remove_rear): list is empty')
        else:
            if self._front != self._rear:
                item = deepcopy(self._rear)
                self._rear = self._rear._previous_node
                self._rear._next_node = None
            else:
                self._front = self._rear = None
            self._count -= 1
        return item

    """---------------------------------------------
                      Task 6
    ---------------------------------------------"""            

    def remove_front(self):
        """
        -------------------------------------------------------
        Description:
            removes and returns copy of first item in the doubly linked list
            if empty list, prints an error message and returns None
        Assert: none
        Use: item = dlist.remove_rear()
        -------------------------------------------------------
        Parameters:
            No input parameters
        Returns:
            item: copy of last item in the doubly linked list
        -------------------------------------------------------
        """
        item = None
        if self.is_empty():
            print('Error(Doubly_Linked_List.remove_front): list is empty')
        else:
            if self._front != self._rear:
                item = deepcopy(self._front)
                self._front = self._front._next_node
                self._front._previous_node = None
            else:
                self._front = self._rear = None
            self._count -= 1
        return item

    """---------------------------------------------
                      Task 7
    ---------------------------------------------"""

    def remove(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds, removes, and returns the value in doubly linked list that matches key.
            if key not found returns None
            If list is empty, prints an error message and returns None
        Assert: none
        Use: item = dlist1.remove(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            item: the full item matching key (?)
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(Doubly_Linked_List.remove): Cannot remove from an empty list')
            return None
        _ , indx = self._linear_search(key)
        current_node = self._front
        location = 0
        while location < indx:
            current_node = current_node._next_node
            location += 1
        if current_node._next_node is None and current_node._previous_node is None:
            self._front = self._rear = None
        elif current_node._next_node is None:
            self._rear = self._rear._previous_node
            self._rear._next_node = None
        elif current_node._previous_node is None:
            self._front = current_node._next_node
            self._front._previous_node = None
        else:
            current_node._previous_node._next_node = current_node._next_node
            current_node._next_node._previous_node = current_node._previous_node
            
        self._count -= 1
        item = current_node._data
        return item
    
    """---------------------------------------------
                        Task 8
    ---------------------------------------------"""

    def reverse(self):
        """
        -------------------------------------------------------
        Description:
           Reverse the order of items in a doubly linked list
        Assert: no asserts
        Use: dlist.reverse()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        current_node = self._front
        while current_node is not None:
            temp = current_node._next_node
            current_node._next_node = current_node._previous_node
            current_node._previous_node = temp
            current_node = current_node._previous_node
        temp = self._front
        self._front = self._rear
        self._rear = temp
        return    
    
    """---------------------------------------------
                        Task 9
    ---------------------------------------------"""

    def swap(self, i, j):
        """
        -------------------------------------------------------
        Description:
            swap items at index i with item at index j
            If either i,j is an invalid index, print error message and do nothing
            if i and j are equal do nothing
            if empty list print error message and return
        Assert: i and j are integers
        Use: list1.swap(i,j)
        -------------------------------------------------------
        Parameters:
            i: index of first swapping item (int)
            j: index of second swapping item (int)
        Returns:
            no returns        
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(Doubly_Linked_List.swap): empty doubly linked list')
        elif i == j:
            return
        elif self._is_valid_index(i) == False or self._is_valid_index(j) == False:
            print('Error(Doubly_Linked_List.swap): invalid i or j')
        elif self._is_valid_index(i) == False or self._is_valid_index(j) == False:
            print("index not valid")
        else:
            if i < 0 and j < 0:
                i = self._count + i
                j = self._count + j
            temp = None
            curri = self._front
            previ = None
            count = 0
            while (curri != None and count != i):
                previ = curri
                curri = curri._next_node
                count += 1
    
            currj = self._front
            prevj = None
            count = 0
            while (currj != None and count != j):
                prevj = currj
                currj = currj._next_node
                count += 1
            
            if curri == None and currj == None:
                return
                
            if previ != None:
                previ._next_node = currj
            else:
                self._front = currj
                
            if prevj != None:
                prevj._next_node = curri
            else:
                self._front = curri
                
            temp = curri._next_node
            curri._next_node = currj._next_node
            currj._next_node = temp
        return

    """---------------------------------------------
                        Task 10
    ---------------------------------------------"""

    def alt_swap(self):
        """
        -------------------------------------------------------
        Description:
            if list is [n1,n2,n3,n4,n5,n6,...]
            swaps every two pairs, result will be:
            [n2,n1,n4,n3,n6,n5,....]
        Assert: no asserts
        Use: dlist.alt_swap()
        -------------------------------------------------------
        Parameters:
            no parameters
        Returns:
            no returns        
        -------------------------------------------------------
        """
        if self._front is None or self._front._next_node is None:
            return
        temp = self._front
        
        while temp is not None and temp._next_node is not None:
            p = temp._data
            temp._data = temp._next_node._data
            temp._next_node._data = p
            temp = temp._next_node._next_node
