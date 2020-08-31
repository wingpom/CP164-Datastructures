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

    def append(self, value):
        """
        -------------------------------------------------------
        Description:
            Adds given item to the tail of the linked list
        Assert: none
        Use: my_list.append(item)
        -------------------------------------------------------
        Parameters:
            item: an arbitrary item to add to linked list (?)
        Returns:
            No returns        
        -------------------------------------------------------
        """
        previous = None
        current = self._front

        # Find the last node in the list
        while current is not None:
            previous = current
            current = current._next_node

        # Case 1:linked list is empty
        #    insert into the front of the list
        if previous is None:
            new_node = Node(deepcopy(value), self._front)
            self._front = new_node
        # Case 2: linked list has multiple items
        else:
            new_node = Node(deepcopy(value), current)
            previous._next_node = new_node
        self._count += 1
        return
    
    def reverse(self):
        """
        -------------------------------------------------------
        Description:
           reverses the order of items in linked list
        Assert: no asserts
        Use: list1.reverse()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        new_front = None

        while self._front is not None:
            temp = self._front._next_node
            self._front._next_node = new_front
            new_front = self._front
            self._front = temp

        self._front = new_front
        return
    
    """---------------------- Task 1 ----------------------"""

    def pop(self, i):
        """
        -------------------------------------------------------
        Description:
            Finds, removes and return copy of linked list item at
            position i
            if invalid index or empty list, print error message and
                return None
        Assert: i is an integer
        Use: item = list1.pop(i)
        -------------------------------------------------------
        Parameters:
            i - index of the element to pop (int)
        Returns:
            item: copy of item at position i (?)        
        -------------------------------------------------------
        """
        if not self._is_valid_index(i):
            print('Error(linked_List.pop): invalid i')
            return None
        
        elif i < 0:
            i = self._count + i
            
        indx = 0  # where I am now
        previous_node = None
        current_node = self._front

        while current_node is not None and indx < i:
            previous_node = current_node
            current_node = current_node._next_node
            indx += 1
        
        if previous_node == None:
            self._front = current_node._next_node
        else:
            previous_node._next_node = current_node._next_node
        
        self._count -= 1
        
        return deepcopy(current_node._data)
            
    """---------------------- Task 2 ----------------------"""

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
        if self._front is None:
            print('Error(Linked_List.swap): empty linked list')
            return
        
        elif i == 0 and j == 0:
            return
            
        elif i == j and not(self._is_valid_index(i) and self._is_valid_index(j)):
            print('Error(Linked_List.swap): invalid i or j')
            return
        
        else:
            if i < 0:
                i = self._count + i
            
            if j < 0:
                j = self._count + j
            
            if i > j:
                t = j
                j = i
                i = t
                
            location1 = 0
            previous_node_1 = None
            current_node_1 = self._front
            
            while current_node_1 is not None and location1 < i:
                previous_node_1 = current_node_1
                current_node_1 = current_node_1._next_node
                location1 += 1
                
            location2 = 0
            previous_node_2 = None
            current_node_2 = self._front
            
            while current_node_2 is not None and location2 < j:
                previous_node_2 = current_node_2
                current_node_2 = current_node_2._next_node
                location2 += 1
                
            if current_node_1 != None and current_node_2 != None:  
                if previous_node_1 == None:
                    temp1 = self._front
                    self._front = previous_node_2._next_node
                else:
                    temp1 = previous_node_1._next_node
                    previous_node_1._next_node = previous_node_2._next_node
                
                if previous_node_2 == None:
                    temp2 = self._front
                    self._front = temp1
                else:
                    temp2 = previous_node_2._next_node
                    previous_node_2._next_node = temp1
                
                temp = temp1._next_node
                temp1._next_node = temp2._next_node
                temp2._next_node = temp
            
            else:
                print('Error(Linked_List.swap): invalid i or j')
            
        return
    
    """---------------------- Task 3 ----------------------"""

    def split(self):
        """
        -------------------------------------------------------
        Description:
            Splits list into two parts. 
            listA contains the first half, listB the second half.
            current list becomes empty
        Assert: i and j are integers
        Use: list1.swap(i,j)
        -------------------------------------------------------
        Parameters:
            No input parameters
        Returns:
            listA - a new List with >= 50% of the original List (Linked_List)
            listB - a new List with <= 50% of the original List (Linked_List)
        -------------------------------------------------------
        """
        n = self._count
        listA = Linked_List()
        listB = Linked_List()
        
        if self._front == None:
            return listA, listB
        
        if self._count % 2 == 0:
            half = self._count // 2
        else:
            half = self._count // 2 + 1
            
        location = 0

        while location < half:
                data = self.pop(0)
                listA.append(data)
                location += 1
                
        while location < n:
                data = self.pop(0)
                listB.append(data)
                location += 1
                
        return listA, listB

    """---------------------- Task 4 ----------------------"""

    def union(self, list2):
        """
        -------------------------------------------------------
        Description:
            Creates a new linked list that contains all elements that
            appear in either current linked list and given linked list 
            or appear in both linked lists
            items from current list are added before items from list2
            Current and input linked lists are not changed
        Assert: list2 is of type Linked_List
        Use: list3 = list1.union(list2)
        -------------------------------------------------------
        Parameters:
            list2: an arbitrary linked list (Linked_List)
        Returns:
            list3: a linked list containing result of union (Linked_List)
        -------------------------------------------------------
        """
        list3 = Linked_List()
        if self._front is None and list2._front is None:
            return list3

        current_node = self._front
        list2_node = list2._front
        
        while current_node is not None:
            temp = current_node
            while temp._next_node is not None:
                if temp._next_node._data == current_node._data:
                    temp._next_node = temp._next_node._next_node
                else:
                    temp = temp._next_node
            list3.append(current_node._data)
            current_node = current_node._next_node
        
        while list2_node is not None:
            temp = list3._front
            while temp._next_node is not None:
                if temp._next_node._data == list2_node._data:
                    temp._next_node = temp._next_node._next_node
                else:
                    temp = temp._next_node
            list3.append(list2_node._data)
            list2_node = list2_node._next_node
        
        return list3

    """---------------------- Task 5 ----------------------"""

    def combine(self, list2):
        """
        -------------------------------------------------------
        Description:
            Creates a new linked list that contains all elements that
            contain all items from current list and given list
            duplicates allowed
            Current items are added before list2 items
            Current and list2 become empty
        Assert: list2 is of type Linked_List
        Use: list3 = list1.cobmine(list2)
        -------------------------------------------------------
        Parameters:
            list2: an arbitrary linked list (Linked_List)
        Returns:
            list3: a linked list containing result of combine (Linked_List)
        -------------------------------------------------------
        """
        list3 = Linked_List()
        if self._front == None and list2._front == None:
            return list3
        elif self._front == None:
            list3._front = list2._front
            list3._count = list2._count
        elif list2._front == None:
            list3._front = self._front
            list3._count = self._count
        else:
            
            list3._front = self._front
            list2_node = list2._front
            while list2_node is not None:
                list3.append(list2_node._data)
                list2_node = list2_node._next_node
                list3._count += 1
                
        self._front = None
        self._count = 0
        
        list2._front = None
        list2._count = 0
        
        return list3  

    """---------------- Task 6 -------------------------"""

    def intersection(self, list2):
        """
        -------------------------------------------------------
        Description:
            Creates a new linked list that contains only elements that
            appear in both lists, no duplicates
            Current items are added before list2 items
            Current list1 and list2 are not changed
        Assert: list2 is of type Linked_List
        Use: list3 = list1.intersection(list2)
        -------------------------------------------------------
        Parameters:
            list2: an arbitrary linked list (Linked_List)
        Returns:
            list3: a linked list containing result of intersection (Linked_List)
        -------------------------------------------------------
        """
        list3 = Linked_List()
        
        if self._front is None or list2._front is None:
            return list3
     
        current_node = self._front
        list2_node = list2._front
        
        while current_node is not None:
            list2_node = list2._front
            while list2_node is not None:
                if current_node._data == list2_node._data:
                    list3.append(current_node._data)
                    break
                list2_node = list2_node._next_node
            current_node = current_node._next_node
        
        temp = list3._front
        
        while temp is not None:
            runner = temp
            while runner._next_node is not None:
                if runner._next_node._data == temp._data:
                    runner._next_node = runner._next_node._next_node
                    list3._count -= 1
                else:
                    runner = runner._next_node
            temp = temp._next_node
        return list3
