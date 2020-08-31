"""
-------------------------
# Student Name: Quynh Dao
# Student ID: 130440130 
# Student email: daox0130@mylaurier.ca
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

    
class Queue:
    """
    -------------------------------------------------------
    Implementation of Queue ADT (Linked List Implementation)
    -------------------------------------------------------
    """
    DEFAULT_SIZE = 10
    
    def __init__(self, size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Description:
            Initializes a Queue Object
            Queue size is set to given value
        Asserts: size is a positive integer
        Use: queue = Queue()
        -------------------------------------------------------
        Parameters:
            size: maximum number of items in 
        Returns:
            A Queue object (Queue)            
        -------------------------------------------------------
        """
        assert isinstance(size, int) and size >= 0, "invalid size"
        self._size = size
        self._front = None
        self._count = 0
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is empty
        Use: result = queue.is_empty()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is empty, False otherwise
        -------------------------------------------------------
        """
        return self._front is None
    
    def is_full(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is full
        Use: result = queue.is_full()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            True if queue is full, False otherwise
        -------------------------------------------------------
        """
        if self._count == self._size:
            return True
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Override built-in len() method
            Returns number of items currently in queue
        Use: num = len(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            num: number of items in queue (int)
        -------------------------------------------------------
        """
        num = 0
        if self._front is None:
            return num
        
        current_node = self._front
        while current_node is not None:
            current_node = current_node._next_node
            num += 1
        return num
    
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of first item in the queue without removing it
            if queue is empty prints error msg and returns None
        Use: item = queue.peek()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            copy of first item in queue (?)            
        -------------------------------------------------------
        """
        if self._front is None:
            print('Error(Queue.peek): Invalid peek operation. Queue is empty')
            return None
        return deepcopy(self._front)
    
    def insert(self, item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the rear of the queue
        Use: queue.insert(item)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the queue (?)
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

        if self._size == self._count:
            print('Error(Queue.insert): Invalid insert operation. Queue is full')
        else:
            # Case 1:linked list is empty
            # insert into the front of the list
            if previous is None:
                new_node = Node(deepcopy(item), self._front)
                self._front = new_node
            # Case 2: linked list has multiple items
            else:
                new_node = Node(deepcopy(item), current)
                previous._next_node = new_node
            self._count += 1
    
    def remove(self):
        """
        -------------------------------------------------------
        Description:
            Removes the first item of in the queue,
            copy of the removed item is returend
            if queue is empty prints error msg and returns None
        Use: item = queue.remove()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - An item from top of stack (?)            
        -------------------------------------------------------
        """
        if self._front is None:
            print('Error(Queue.remove): Invalid remove operation. Queue is empty')
            return None
        current_node = self._front
        item = current_node._data
        # Move front to the next node
        self._front = self._front._next_node
        current_node = None
        return item

    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Queue ADT
            Prints all items in Queue
            (First Second ... Last)
            prints () if queue is empty
        Use: str(queue) 
             print(queue)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        if self._front is None:
            return '()'
        output = '('
        
        current_node = self._front
        
        while current_node is not None:
            output += str(current_node._data) + ' '
            current_node = current_node._next_node
        return output[:-1] + ')'
    
    def remove_last(self):
        """
        -------------------------------------------------------
        Description:
            This is not part of Queue ADT. Introduced for practice
            Removes last item in queue and returns a copy
            If queue is empty prints an error message
        Use: item = q.remove_last()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            item: copy of data stored in the last node
        -------------------------------------------------------
        """
        previous_node = None
        current_node = self._front
            
        if self._front is None:
            print('Error(Queue.remove_last): Queue is empty')
            return None
        
        if self._front._next_node is None:
            item = current_node._data
            self._front = None
            return item

        while current_node._next_node is not None:
            previous_node = current_node
            current_node = current_node._next_node
        previous_node._next_node = None
        item = current_node._data
        
        return item
