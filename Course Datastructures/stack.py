"""
-------------------------
# Student Name:  Quynh Dao
# Student ID:    130440130
# Student email: daox0130@mylaurier.ca
#-------------------------
"""
from copy import deepcopy


class Stack:
    """
    -------------------------------------------------------
    Implementation of Stack ADT (Array-based Implementation)
    Top of Stack is the last element in the Python list
    -------------------------------------------------------
    """

    def __init__(self):
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
        self.items = []
    
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
        if self.is_empty():
            print("Error(Stack.peek):Invalid peek operation. Stack is empty")
            return None
        else:
            return deepcopy(self.items[-1])
    
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
        self.items.append(item)
    
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
        else:
            return self.items.pop()
    
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
        
        return (self.items == [])
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Stack ADT
            Prints all items in stack
            prints [] if stack is empty
        Use: stack.print()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        -------------------------------------------------------
        """
        if self.is_empty():
            output = '[]'
        else:
            output = ''
            for i in range(len(self.items) - 1, -1, -1):
                output = output + str(self.items[i]) + '\n'
  
        return output                         


def reverse_str(str1):
    """
    -------------------------------------------------------
    Description:
        Reverse a given string using stacks
    Use: rev_str = reverse_str(input_str)
    -------------------------------------------------------
    Parameters:
        str1 - an input string (str)
    Returns:
        str2 - reversed string (str)
    -------------------------------------------------------
    """
    s = Stack()
    
    for char1 in str1:
        s.push(deepcopy(char1))
        
    str2 = ''
    
    while s.is_empty() == False:
        str2 += s.pop()

    return str2


def is_balanced(expression):
    """
    -------------------------------------------------------
    Description:
        Checks if a given expression is balanced
        Uses stacks.
    Use: result = is_balanced(expression)
    -------------------------------------------------------
    Parameters:
        expression - an arbitrary expression (str)
    Returns:
        True/False
    -------------------------------------------------------
    """
    s = Stack()
    
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']
    
    result = False 
    
    for char in expression:
        if char in open_brackets:
            s.push(char)
        elif char in close_brackets and s.is_empty() == False:
            opposite = s.pop()
            index = close_brackets.index(char)
            
            if opposite == open_brackets[index]:
                result = True
            else:
                result *= False
                
    if result == 0:
        result = False
                    
    return result

    
def evaluate_postfix(expression):
    """
    -------------------------------------------------------
    Description:
        Evaluates a postfix expression.
        Uses stacks.
        Expression is formatted such that each term is separated by a space
        Supports seven operators: +,-,*,**,/,// and %
    Use: result = evaluate_postfix(expression)
    -------------------------------------------------------
    Parameters:
        expression - an arbitrary expression (str)
    Returns:
        result - output of expression evaluation (int/float)
    -------------------------------------------------------
    """
    s = Stack()
    
    exp = expression.split(' ')

    for i in exp:
        if i.isdigit():
            s.push(int(i))
        elif i == '+':
            num2 = s.pop()
            num1 = s.pop()
            result = num1 + num2
            s.push(result)
            
        elif i == '-':
            num2 = s.pop()
            num1 = s.pop()
            result = num1 - num2
            s.push(result)
            
        elif i == '*':
            num2 = s.pop()
            num1 = s.pop()
            result = num1 * num2
            s.push(result)
            
        elif i == '**':
            num2 = s.pop()
            num1 = s.pop()
            result = num1 ** num2
            
        elif i == '//':
            num2 = s.pop()
            num1 = s.pop()
            result = num1 // num2
            s.push(result)
            
        elif i == '/':
            num2 = s.pop()
            num1 = s.pop()
            result = num1 / num2
            s.push(result)
            
        elif i == '%':
            num2 = s.pop()
            num1 = s.pop()
            result = num1 % num2
            s.push(result)
    
    result = s.pop()
    
    return result

