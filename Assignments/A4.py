"""
-------------------------
# Student Name: Quynh Dao    
# Student ID: 130440130
# Student email: daox0130@mylaurier.ca
#-------------------------
"""

from data import Student
from my_queue import Queue
from copy import deepcopy

def compare_students(student1,student2):
    """
    -------------------------------------------------------
    Description:
        Compare two student objects
        Compare keys, then last name, then first name
        Return 1 if student1 > student2
        Return 2 if student1 < student2
        Return 0 if student1 == student2
        Return -1 if there is an error, which is if either input is not a student object
            In that case also print an error message
    Use: result = compare_students(student1,student2)
    -------------------------------------------------------
    Parameters:
        student1 - a student object (Student)
        student2 - a student object (Student)    
    Returns:
        result - 0/1/2/-1 (int)            
    -------------------------------------------------------
    """
    result = -1
    if isinstance(student1, Student) and isinstance(student2, Student):
        if student1.sid > student2.sid:
            result = 1
        elif student2.sid > student1.sid:
            result = 2
        else:
            if student1.last > student2.last:
                result = 1
            elif student2.last > student1.last:
                result = 2
            else:
                if student1.first > student2.first:
                    result = 1
                elif student2.first > student1.first:
                    result = 2
                else:
                    result = 0
    else:
        print('Error(compare_students): invalid input parameter type')
    return result

def remove_group(queue,num):
    """
    -------------------------------------------------------
    Description:
        Remove num items from a queue, and return it as a list
        if invalid queue or invalid num, print error message and return empty list
    Use: removed_items = remove_group(queue,num)
    -------------------------------------------------------
    Parameters:
        queue - a queue object containing arbitrary items (Queue)
        num - number of items to be removed from queue (int)
    Returns:
        removed_items - list containing copies of removed items (list)           
    -------------------------------------------------------
    """
    i = 0
    removed_items = []
    if isinstance(queue, Queue):
        if isinstance(num, int) and num > 0:
            while i < num:
                if queue.is_empty():
                    break
                else:
                    item = deepcopy(queue.remove())
                    removed_items.append(item)
                    i += 1
        else:
            print('Error(remove_group): invalid value for num')
    else:
        print('Error(remove_group): invalid input parameter type')
    return removed_items

def remove_batch(queue,year):
    """
    -------------------------------------------------------
    Description:
        Remove students enrolled in given year from a given queue
        Function process queue items sequentially:
        if year does not match, item is moved to rear of queue
        students removed are stored in a queue
    Use: batch_queue = remove_batch(queue,year)
    -------------------------------------------------------
    Parameters:
        queue - a queue object containing student objects (Queue)
        year - enrollment year (int)
    Returns:
        batch_queue - a queue containing students of same batch          
    -------------------------------------------------------
    """
    batch_queue = Queue()
    if isinstance(year, int):
        for _ in range(len(queue)):
            student = deepcopy(queue.remove())
            student_key = student.key()
            
            if str(year) in student_key:
                batch_queue.insert(student)
            else:
                queue.insert(student)
    else:
        print('Error(remove_batch): invalid input parameter type')
    return batch_queue

def priority_merge(queue1,queue2):
    """
    -------------------------------------------------------
    Description:
        Merge two queues into one main queue
        The front of the two queues is compared, the larger one is inserted first
        The process repeats until no more objects remain in both queues
        Further details of the merging is provided in the PDF file
    Use: q3 = proirity_merge(q1,q2)
    -------------------------------------------------------
    Parameters:
        queue1 - a queue containing student objects (Queue)
        queue2 - a queue containing student objects (Queue)
    Returns:
        queue3 - a queue containing student objects (Queue)            
    -------------------------------------------------------
    """
    max_size = len(queue1) + len(queue2)
    
    if max_size == 0:
        queue3 = Queue()
    else:
        queue3 = Queue(max_size)
    
    while not (queue1.is_empty() or queue2.is_empty()):
        student1 = queue1.peek()
        student2 = queue2.peek()
        result = compare_students(student1, student2)
        
        if result == 2:
            queue3.insert(queue2.remove())
        elif result == 1:
            queue3.insert(queue1.remove())
        else:
            queue2.remove()
            queue3.insert(queue1.remove())

    if queue1.is_empty():
        for _ in range(len(queue2)):
            queue3.insert(queue2.remove())

    if queue2.is_empty():
        for _ in range(len(queue1)):
            queue3.insert(queue1.remove())
         
    return queue3

def shred_queue(queue,size):
    """
    -------------------------------------------------------
    Description:
        shreds a queue into several equal sized queues of given size.
        Items of the queue is distributed sequentially into the minoir queues.
        If given size is invalid, print error message and return empty list
        At the end of the shredding process the input queue should be restored.  
    Use: queue_list = shred_queue(queue,size)
    -------------------------------------------------------
    Parameters:
        queue - a queue containing arbitrary items (Queue)
        size - size of each mini queue (int)
    Returns:
        queues - a list containing mini queues (list)            
    -------------------------------------------------------
    """
    queues = []
    q = deepcopy(queue)
    
    if isinstance(size, int) and size > 0 and size < len(q)+1:
        i = 0
        if len(queue) % size == 0:
            num_queues = len(queue) // size
        else:
            num_queues = len(queue) // size + 1
        
        while i < num_queues:
            new_queue = Queue(size)
            
            for _ in range(size):
                if q.is_empty():
                    break
                else:
                    new_queue.insert(q.remove())

            queues.append(new_queue)
            i += 1
    else:
        print("Error(shred_queue): invalid shred size")
    
    return queues
        