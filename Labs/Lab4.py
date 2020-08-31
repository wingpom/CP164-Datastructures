"""
-------------------------
# Student Name: Quynh Dao
# Student ID: 130440130
# Student email: daox0130@mylaurier.ca
#-------------------------
"""
from copy import deepcopy
from my_queue import Queue
MAX_SIZE = 100


def reverse_stack(stack):
    """
    -------------------------------------------------------
    Description:
        Reverse a stack using a queue
    Use: reverse_stack(stack)
    -------------------------------------------------------
    Parameters:
        stack - a stack of items (Stack)
    Returns:
        No returns
    -------------------------------------------------------
    """
    queue = Queue()
    
    while not stack.is_empty():
        item = deepcopy(stack.pop())
        queue.insert(item)
    
    while not queue.is_empty():
        stack.push(queue.remove())

    return


def queue_to_file(queue, filename):
    """
    -------------------------------------------------------
    Description:
        Writes students stored in a queue into given file.
        Queue becomes empty after writing
        Each student record appears in a separate line in file
        using the following format:
        [sid,first last]
    Use: queue_to_file(queue,filename)
    -------------------------------------------------------
    Parameters:
        queue - A queue containing students objects (Queue)
        filename - name of input file (str)
    Returns:
        No return
    -------------------------------------------------------
    """
    students = []
    f = open(filename, 'w')

    while not queue.is_empty():
        item = queue.remove()
        line = str(item).replace(',', ' ').replace(':', ',')
        students.append('[' + line + ']')
    
    string_of_students = '\n'.join(students)

    f.write(string_of_students)
    f.close()
    
    return


def lshift_queue(queue, shifts):
    """
    -------------------------------------------------------
    Description:
        Shifts the queue to left by putting the front to the rear
        and repeating that as many as #shifts
        prints an error if shifts is negative or if queue is empty
    Use: lshift_queue(queue,shifts)
    -------------------------------------------------------
    Parameters:
        queue - A queue containing arbitrary objects (Queue)
        shifts - number of shifts to make the right(int)
    Returns:
        No returns
    -------------------------------------------------------
    """
    if  shifts < 0:
        print('Error(lshift_queue): Invalid shift value. Should be non negative')
    elif queue.is_empty():
        print('Error(lshift_queue): Queue is empty')
        queue = queue
    else:
        for _ in range(shifts):
            queue.insert(queue.remove())
    return


def rshift_queue(queue, shifts):
    """
    -------------------------------------------------------
    Description:
        Shifts the queue to right by putting the rear to the front
        and repeating that as many as #shifts
        prints an error if shifts is negative or if queue is empty
    Use: rshift_queue(queue,shifts)
    -------------------------------------------------------
    Parameters:
        queue - A queue containing arbitrary objects (Queue)
        shifts - number of shifts to make the right(int)
    Returns:
        No returns
    -------------------------------------------------------
    """
    if shifts < 0:
        print('Error(rshift_queue): Invalid shift value. Should be non negative')
    elif queue.is_empty():
        print('Error(rshift_queue): Queue is empty')
        queue = queue
    else:
        for _ in range(len(queue) - shifts):
            queue.insert(queue.remove())
    return
