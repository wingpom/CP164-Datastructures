"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""
from copy import deepcopy


class Queue:
    """
    -------------------------------------------------------
    Implementation of Queue ADT (Array-based Implementation)
    start of Queue is the last element in the Python list
    -------------------------------------------------------
    """
    
    def __init__(self, size=10):
        """
        -------------------------------------------------------
        Description:
            Initializes a Queue Object
            Initializes items to an empty list
            Queue size is set by given value
        Use: queue = Queue()
        -------------------------------------------------------
        Parameters:
            size - max # of values that can be stored in queue, 
            default value is 10 (int)
        Returns:
            A Queue object (Queue)            
        -------------------------------------------------------
        """
        assert isinstance(size, int), 'size should be an integer'
        assert size > 0, 'Queue Size > 0'
        
        self._items = []
        self._size = size
    
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of first item in the queue without removing it
            if queue is empty prints error msg and returns None
        Use: item = queue.peek()
        Analysis: 
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            copy of first item in queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(Queue.peek): Invalid peek operation. Queue is empty')
            return None
        else:
            return deepcopy(self._items[-1])
    
    def insert(self, item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the rear of the queue
        Use: queue.insert(item)
        Analysis: O(n)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the queue (?)
        Returns:
            No returns           
        -------------------------------------------------------
        """
        if self.is_full():
            print('Error(Queue.insert): Invalid insert operation. Queue is full')
            
        else:
            self._items.insert(0, deepcopy(item))
            
        return
    
    def remove(self):
        """
        -------------------------------------------------------
        Description:
            Removes the first item of in the queue,
            copy of the removed item is returend
            if queue is empty prints error msg and returns None
        Use: item = queue.remove()
        Analysis: O(1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - An item from top of stack (?)            
        -------------------------------------------------------
        """
        item = None
        
        if self.is_empty():
            print('Error(Queue.remove):Invalid remove operation. Queue is empty')
            
        else:
            item = deepcopy(self._items.pop(-1))
        
        return item
    
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
        
        return len(self._items) == 0
    
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
        return len(self._items) == self._size
    
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
        num = len(self._items)
        
        return num
    
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
        print_queue = "("
        
        if self.is_empty():
            print_queue += ')'
        
        else:
            for i in range(len(self._items) - 1, -1, -1):
                if i != 0:
                    print_queue += '{} '.format(self._items[i])
                else:
                    print_queue += '{})'.format(self._items[i])
            
        return print_queue

    
class cQueue:
    """
    -------------------------------------------------------
    Implementation of Circular Queue ADT (Array-based Implementation)
    -------------------------------------------------------
    """
    
    def __init__(self, size=10):
        """
        -------------------------------------------------------
        Description:
            Initializes a Queue Object
            Initializes items to an empty list
            Queue size is set by given value, or default of 10
        Use: cq = cQueue()
        -------------------------------------------------------
        Parameters:
            size - max # of values that can be stored in circular 
            queue, default value is 10 (int)
        Returns:
            A Queue object (Queue)            
        -------------------------------------------------------
        """
        assert isinstance(size, int), "size should be an integer"
        assert size > 0, "Queue Size > 0"
        
        self._items = [None] * size
        self._max_size = size
        self._current_size = 0
        self._front = -1
        self._rear = -1

    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of first item in the queue without removing it
            if queue is empty prints error msg and returns None
        Use: item = cq.peek()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            copy of first item in queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(cQueue.peek):Invalid peek operation. Queue is empty')
            return None 
        
        else:
            return deepcopy(self._items[self._front])
    
    def insert(self, item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the queue
        Use: cq.insert(item)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the queue (?)
        Returns:
            No returns           
        -------------------------------------------------------
        """
        if self.is_full():
            print('Error(cQueue.insert): Invalid insert operation. Queue is full')
            return 
        
        if self.is_empty():
            # Front and rear become last index value of list (positive)
            self._front = self._max_size - 1
            self._rear = self._max_size - 1
            
        else:
            self._rear = (self._rear - 1) % self._max_size
            
        self._items[self._rear] = deepcopy(item)
        self._current_size += 1 
    
    def remove(self):
        """
        -------------------------------------------------------
        Description:
            Removes the first item of in the queue,
            copy of the removed item is returend
            if queue is empty prints error msg and returns None
        Use: item = cq.remove()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - An item from top of stack (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(cQueue.remove):Invalid remove operation. Queue is empty')
            return None 
        
        item = deepcopy(self._items[self._front])
        self._items[self._front] = None 
        
        self._current_size -= 1
        
        if self._current_size == 0:
            self._front = -1
            self._rear = -1
            
        else:
            self._front = (self._front - 1) % self._max_size   
            
        return item
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is empty
        Use: result = cq.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if queue is empty, False otherwise
        -------------------------------------------------------
        """
        return self._current_size == 0
        
    def is_full(self):
        """
        -------------------------------------------------------
        Description:
            checks if queue is full
        Use: result = cq.is_full()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if queue is full, False otherwise
        -------------------------------------------------------
        """
        return self._current_size == self._max_size
            
    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Returns number of items currently in queue
        Use: num = len(cq)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            num: number of items in queue (int)
        -------------------------------------------------------
        """
        return self._current_size
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Queue ADT
            Prints items in queue in proper order
            prints () if queue is empty
        Use: print(queue) or str(queue)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        -------------------------------------------------------
        """
        output = ''
        
        if self.is_empty():
            output = '()' 
        
        else:
            i = self._front
            output += '{} '.format(str(self._items[i]))
            
            while i != self._rear:
                i = (i - 1) % self._max_size 
                output += '{} '.format(str(self._items[i]))
        
        return output

    def print(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Queue ADT
            Prints actual contents of cqueue list
            also prints front and rear pointers
        Use: queue.print()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            cQ_print - prints information and contents of queue
        -------------------------------------------------------
        """
        contents = ""
            
        for i in range(self._max_size):
            if i != self._max_size - 1:
                contents += '{} '.format(self._items[i])

            else:
                contents += '{}'.format(self._items[i])
        
        print('front = {}, back = {}, current_size = {} , contents = \n({})'.
            format(self._front, self._rear, self._current_size, contents))
            
        return
        
        
