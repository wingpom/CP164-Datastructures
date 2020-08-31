"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""
from copy import deepcopy

from data import Student


class cQueue:
    """
    -------------------------------------------------------
    Implementation of Circular Queue ADT (Array-based Implementation)
    -------------------------------------------------------
    """
    DEFAULT_SIZE = 10
    
    def __init__(self, size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Description:
            Initializes a Queue Object
            Initializes items to an empty list
            Queue size is set by given value
        Use: cq = cQueue()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            A Queue object (Queue)            
        -------------------------------------------------------
        """
        assert isinstance(size, int), "size should be an integer"
        assert size > 0, "Queue Size > 0"
        self._max_size = size
        self._current_size = 0
        self._items = [None] * size
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
            self._front = 0
            self._rear = 0
        else:
            self._rear = (self._rear + 1) % self._max_size
        
        self._items[self._rear] = deepcopy(item)
        self._current_size += 1
        
        return
    
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
        
        removed_item = deepcopy(self._items[self._front])
        self._items[self._front] = None

        self._current_size -= 1
        
        if self._current_size == 0:
            self._front = -1
            self._rear = -1
        else:
            self._front = (self._front + 1) % self._max_size

        return removed_item
    
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
        if self.is_empty():
            return '()'
        output = '('
        i = self._front
        output = output + str(self._items[i]) + ''
        while i != self._rear:
            output += ' '
            i = (i + 1) % self._max_size
            output = output + str(self._items[i]) + ''
        output += ')'
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
            None
        -------------------------------------------------------
        """
        print('front = {}, rear = {}, current_size = {} , contents = \n('.format
              (self._front, self._rear, self._current_size), end='')
        for i in range(self._max_size):
            if i != self._max_size - 1:
                print(self._items[i], end=' ')
            else:
                print(self._items[i], end='')
        print(')')
        return

    
class pQueue:
    """
    -------------------------------------------------------
    Implementation of Prioirity Queue ADT (Array-based Implementation)
    Sorted insertion approach
    Highest priority is determined to be greatest item
    If multiple highest items, pick any item
    -------------------------------------------------------
    """
    DEFAULT_SIZE = 10
    
    def __init__(self, size=DEFAULT_SIZE, mode='H'):
        """
        -------------------------------------------------------
        Description:
            Initializes a Priority Queue Object
            Initializes items to an empty list
            Queue size is set by given value
        Use: queue = Queue()
        -------------------------------------------------------
        Parameters:
            size: maximum size of queue (default = 10)
            mode: H = Highest First and L = Lowest First
        Returns:
            A pQueue object (pQueue)            
        -------------------------------------------------------
        """
        assert isinstance(size, int), "size should be an integer"
        assert size > 0, "Queue Size > 0"
        assert mode == 'H' or mode == 'L', "Unsupported priority"
        self._items = []
        self._size = size
        self._mode = mode
    
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of highest priority item in the queue without removing it
            if queue is empty prints error msg and returns None
        Use: item = queue.peek()
        Analysis: O(1)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            copy of first item in queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(pQueue.peek): Invalid peek operation. Queue is empty')
            return None
        highest = 0  # sorting index of highest priority
        
        if self._mode == 'H':
            for i in range(1, len(self.items)):
                if self._items[i] > self._items[highest]:  # >= picks the last one, two items of the same priority preference for the one arriving earliest
                    highest = i
                    
        elif self._mode == 'L':
            for i in range(1, len(self.items)):
                if self._items[i] < self._items[highest]:  # >= picks the last one, two items of the same priority preference for the one arriving earliest
                    highest = i
        return deepcopy(self._items[highest])
    
    def insert(self, item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the priority queue
        Use: queue.insert(item)
        Analysis: O(nlogn) - Python uses Timsort which is:
                 O(nlogn) worst and average, O(n) best case
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the queue (?)
        Returns:
            No returns           
        -------------------------------------------------------
        """
        if self.is_full():
            print('Error(pQueue.insert): Invalid insert operation. Queue is full')
        else:
            self._items.append(deepcopy(item))
            if self._mode == 'H':
                self._items = sorted(self._items)
            elif self._mode == 'L':
                self._items = sorted(self._items, reverse=True) 
        return
    
    def remove(self):
        """
        -------------------------------------------------------
        Description:
            Removes the item with the highest priority from the queue
            copy of the removed item is returend
            if queue is empty prints error msg and returns None
        Use: item = queue.remove()
        Analysis: O(1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - highest priority item in the queue (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(pQueue.remove): Invalid remove operation. Queue is empty')
            return None
        highest = 0  # sorting index of highest priority
        
        if self._mode == 'H':
            for i in range(1, len(self._items)):
                if self._items[i] > self._items[highest]:  # >= picks the last one, two items of the same priority preference for the one arriving earliest
                    highest = i
                    
        elif self._mode == 'L':
            for i in range(1, len(self._items)):
                if self._items[i] < self._items[highest]:  # >= picks the last one, two items of the same priority preference for the one arriving earliest
                    highest = i
        return deepcopy(self._items.pop(highest))
    
        if self.is_empty():
            print('Error(pQueue.remove):Invalid remove operation. Queue is empty')
            return None
    
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
        return len(self._items)
    
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
        if self.is_empty():
            output = '()'
        else:
            output = '('
            for i in range(len(self._items) - 1, -1, -1):
                output = output + str(self._items[i]) + ' '
        output = output[:-1] + ')'
        return output


def students_to_queue(filename, q_type):
    """
    -------------------------------------------------------
    Description:
        Converts students stored in a file in a queue
        if q_type is cQueue --> use cQueue
        if q_type is pQueue --> use pQueue('H')
        otherwise, print error and return None
    Use: q = students_to_queue(filename,'cQueue')
         q = students_to_queue(filename, 'pQueue')
    -------------------------------------------------------
    Parameters:
        filename: name of file containing students (str)
        q_type: cQueue or pQueue (str)
    Returns:
        q: a Queue containing students objects (cQueue or pQueue)
    -------------------------------------------------------
    """
    fv = open(filename, 'r')
    lines = fv.readlines()
    size = len(lines)
    
    if q_type == 'cQueue':
        q = cQueue(size)
        for line in lines:
            int1 = line.find(',')
            sid = line[0:7]
            last = line[8:int1]
            first = line[int1 + 1:].strip('\n')
            
            student = Student(sid, last, first)
            q.insert(student)
            
    elif q_type == 'pQueue':
        q = pQueue(size, mode='H')
        
        for line in lines:
            line.strip('\n')
            int1 = line.find(',')
            sid = line[0:7]
            last = line[8:int1]
            first = line[int1 + 1:].strip('\n')
            
            student = Student(sid, last, first)
            q.insert(student)
    else:
        print('Error(file_to_queue): unsupported q_type')
        q = None
    fv.close()
    
    return q


def schedule(filename, schedule_type):
    """
    -------------------------------------------------------
    Description:
        Schedule students stored in a file using given scheduler
        Supports FIFO and Priority schedulers, 
            otherwise print error msg and return None
        Prints output similar to samples in Lab5_output.txt
    Use: schedule(filename,'FIFO')
         schedule(filename,'Priority')
    -------------------------------------------------------
    Parameters:
        filename: name of file containing students (str)
        scheduler_type: FIFO or Priority (str)
    Returns:
        No Returns
    -------------------------------------------------------
    """
    if schedule_type == 'Priority':
        q_type = 'pQueue'
        q = students_to_queue(filename, q_type)
        
        print('{} {}{}'.format('Starting Priority Scheduler on', filename, ':'))
        
        while not q.is_empty():
            print('\t', q.remove())
        print('Closing Priority Scheduler')
        
    elif schedule_type == 'FIFO':
        q_type = 'cQueue'
        q = students_to_queue(filename, q_type)
        print('{} {}{}'.format('Starting FIFO Scheduler on', filename, ':'))
        
        while not q.is_empty():
            print('\t', q.remove())
        print('Closing FIFO Scheduler')
    
    else:
        print('Error(schedule): unsupported scheduler')
        
    return
