"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""
from stack import Stack
from data import Student
from copy import deepcopy

def count_stack(stack):
    """
    -------------------------------------------------------
    Description:
        Counts the items stored in the stack
        Should not access the items directly, need to use push/pop
        if input is not a stack, the function prints an error message
    Use: num_items = count_stack(stack)
    -------------------------------------------------------
    Parameters:
        stack - a stack object (Stack)
    Returns:
        num_items - number of items in stack (int)
    -------------------------------------------------------
    """
    num_items = 0
    new_stack = deepcopy(stack)

    if isinstance(new_stack, Stack):
        if new_stack.is_empty():
            num_items = 0
        else:
            while not new_stack.is_empty():
                new_stack.pop()
                num_items += 1
                
        return num_items
    else:
        print("Error(count_stack): input is not a stack")
        return -1
 
def reverse_stack(stack):
    """
    -------------------------------------------------------
    Description:
        Reverses the order of items within a stack
        Should not access the items directly, need to use push/pop
        if input is not a stack, the function prints an error message
    Use: reverse_stack(stack)
    -------------------------------------------------------
    Parameters:
        stack - a stack object (Stack)
    Returns:
        No returns
    -------------------------------------------------------
    """
    items = []
    if isinstance(stack, Stack):
        if stack.is_empty():
            return []
        else:
            while not stack.is_empty():
                items.append(stack.pop())
            
        for item in items:
            stack.push(item)     
    else:
        print("Error(reverse_stack): input is not a stack")

    return

def swap_stacks(stack1,stack2):
    """
    -------------------------------------------------------
    Description:
        swaps the contents of two stacks
        Should not access the items directly, need to use push/pop
        if either input is not a stack, the function prints an error message
    Use: reverse_stack(stack)
    -------------------------------------------------------
    Parameters:
        stack1 - first stack (Stack)
        stack2 - second stack
    Returns:
        No returns
    -------------------------------------------------------
    """
    stack = Stack()
    i = 0
    j = 0
    
    if isinstance(stack1, Stack) and isinstance(stack2, Stack):
        size1 = count_stack(stack1)
        size2 = count_stack(stack2)
        
        while not stack1.is_empty():
            stack.push(stack1.pop())
        
        while not stack2.is_empty():
            stack.push(stack2.pop())

        while i < size2:
            stack1.push(stack.pop())
            i += 1
            
        while j < size1:
            stack2.push(stack.pop())
            j += 1
            
    else:
        print('Error(swap_stacks): invalid input')
    return

def stack_to_students(stack):
    """
    -------------------------------------------------------
    Description:
        Copy students stored in a stack into a list of students
        Should not access the items directly, need to use push/pop
        After copy operation, both stack and list should have
            a distinct copy of students
        The top of the stack will be the last item in the list
        if input is not a stack, the function prints an error message
    Use: students = stack_to_students(stack)
    -------------------------------------------------------
    Parameters:
        stack - a stack containing student objects (Stack)
    Returns:
        students - a list of students (list)
    -------------------------------------------------------
    """
    students = []
    s = deepcopy(stack)
    
    if count_stack(s) % 3 == 0 and isinstance(s, Stack):
        while not s.is_empty():
            sid = str(s.pop())
            last = str(s.pop())
            first = str(s.pop())
            student = Student(sid,last,first)
            students.append(student)
    else:
        print('Error(stack_to_students): Invalid stack')
        
    return students

def del_batch(stack,year):
    """
    -------------------------------------------------------
    Description:
        deletes from a stack all students with an enrolment year equal
            to given year
        The order of the stack should be preserve after deleting the students
        Should not access the items directly, need to use push/pop
        if first input is not a stack, or second input is not an integer
            the function prints an error message
    Use: del_batch(stack,year)
    -------------------------------------------------------
    Parameters:
        stack - a stack of students (Stack)
        year - an enrolment year (int)
    Returns:
        No returns
    -------------------------------------------------------
    """
    count = 0
    new_stack = Stack()
    
    if isinstance(stack, Stack):
        size_stack = count_stack(stack)
        
        while not stack.is_empty() and count < size_stack:
            student = stack.pop()
            enrol_year = student.get_year()
            if year != enrol_year:
                new_stack.push(student)
            count += 1

        while not new_stack.is_empty():
            stack.push(new_stack.pop())

    else:
        print('Error(del_batch): One of the inputs is invalid')
            
    return
