"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""
from copy import deepcopy

from data import Student


class Stack:
    """
    -------------------------------------------------------
    Implementation of Stack ADT (Array-based Implementation)
    Top of Stack is the last element in the Python list
    -------------------------------------------------------
    """

    def __init__(self, size):
        """
        -------------------------------------------------------
        Description:
            Initializes a Stack Object
            Initializes items to an empty list
        Use: stack = Stack()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            A Stack object (Stack)            
        -------------------------------------------------------
        """
        self.items = [] * size
        self.capacity = size    
    
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of top of stack
            if Stack is empty prints error msg and returns None
        Use: item = stack.peek()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An item from top of stack (?)            
        -------------------------------------------------------
        """
        result = None
        if self.is_empty():
            print('Error(Stack.peek):Invalid peek operation. Stack is empty')
        else:
            result = deepcopy(self.items[0])
        return result
    
    def push(self, item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the stack
        Use: stack.push(item)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the stack (?)
        Returns:
            None           
        -------------------------------------------------------
        """
        if len(self.items) != self.capacity:
            self.items.insert(0, deepcopy(item))
        else: 
            print('Error(Stack.push):Invalid push operation. Stack is full')
        return 
    
    def pop(self):
        """
        -------------------------------------------------------
        Description:
            Removes the top item of the stack
            if Stack is empty prints error msg and returns None
        Use: item = stack.pop()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - An item from top of stack (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(Stack.pop):Invalid pop operation. Stack is empty')
            return None
        return self.items.pop(0)
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if stack is empty
        Use: result = stack.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        return len(self.items) == 0
    
    def is_full(self):
        return len(self.items) == self.capacity
    

def print_stack(stack):
    """
    -------------------------------------------------------
    Description:
        Utility function for testing purposes only
        Prints contents of stack
        First line is: size = stack_size
        Next lines contain stack items, each in separate line
        Top of stack is printed first
    Use: print_stack(stack)
    -------------------------------------------------------
    Parameters:
        stack - a stack object to be printed (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    items = []
    print('size = {}'.format(stack.capacity))
    
    if stack.is_empty():
        print(items)
    else:
        while not stack.is_empty():
            print(stack.peek())
            item = stack.pop()
            items.append(item)
    
        for item in items:
            stack.push(item)
    return None

            
def list_to_stack(list1):
    """
    -------------------------------------------------------
    Description:
        Convert a list to a stack
        First item in list will be the bottom of stack
        Last item in list will be the top of the stack
    Use: stack = list_to_stack(list1)
    -------------------------------------------------------
    Parameters:
        list1 - a list to be copied into a new stack (list)
    Returns:
        stack - a newly created stack objects with items from list (Stack)
    -------------------------------------------------------
    """
    stack = Stack(len(list1))
    for i in range(len(list1)):
        stack.push(list1[i])
    return stack


def students_to_stack(filename, size):
    """
    -------------------------------------------------------
    Description:
        Reads the contents of a file into a stack
        The file stores student information, each in separate line
            sid:last,first
        The stack is initialized with the given size
        The function does not perform file reading if stack is full 
    Use: stack = students_to_stack(filename,size)
    -------------------------------------------------------
    Parameters:
        filename - name of input file (str)
        size - Maximum stack size (int)
    Returns:
        stack - a stack containing student objects (Stack)
    -------------------------------------------------------
    """
    i = 0
    stack = Stack(size)
    file = open(filename, 'r')
    
    for line in file:
        int1 = line.find(',')
        
        sid = line[:7]
        last = line[8:int1]
        first = line[int1 + 1:].strip('\n')
        student = Student(sid, last, first)
        
        if i != size:
            stack.push(student)
            i += 1
    return stack
