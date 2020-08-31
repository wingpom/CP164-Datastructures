"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""

"""----------- Task 1 ------------"""
def product1(num,n):
    """
    -------------------------------------------------------
    Description:
        Computes the product of num which is: 
            num*num*... repeated n times
        Uses loops
    Assert: num is an integer or float
            n is a positive integer
    Use: result = product1(num,n)
    -------------------------------------------------------
    Parameters:
        num: A number to compute its product (int/float)
        n: Number of times to multiply num (int)
    Returns:
        result: product of num, n times (int/float)        
    -------------------------------------------------------
    """
    assert isinstance(num, int) or isinstance(num, float), "invalid num"
    assert n >= 0, 'invalid n'
    if n == 0:
        return  num
    result = num
    for _ in range(1,n):
        result *= num
    return result

def product2(num,n):
    """
    -------------------------------------------------------
    Description:
        Computes the product of num which is: 
            num*num*... repeated n times
        Uses Recursion
    Assert: num is an integer or float
            n is a positive integer
    Use: result = product1(num,n)
    -------------------------------------------------------
    Parameters:
        num: A number to compute its product (int/float)
        n: Number of times to multiply num (int)
    Returns:
        result: product of num, n times (int/float)        
    -------------------------------------------------------
    """
    assert isinstance(num, int) or isinstance(num, float), "invalid num"
    assert n >= 0, 'invalid n'
    if n == 0:
        return num
    if n == 1:
        return product2(num, n-1)
    return num * product2(num, n-1)

"""----------- Task 2 ------------"""
def Sn1(i):
    """
    -------------------------------------------------------
    Description:
        Finds the ith number of the sequence Sn
        S(0) = 1
        S(n) = S(n-1)^2 + 1
        i     :    0    1    2    3    4    
        Sn1(i):    1    2    5    26   677
        Uses Loops
    Assert: i is a non-negative integer
    Use: num = Sn1(i)
    -------------------------------------------------------
    Parameters:
        i: a non-negative number (int)
    Returns:
        number: the ith number in the Sn sequence (int)      
    -------------------------------------------------------
    """
    assert i >= 0, "invalid i"
    if i == 0:
        return 1
    n = 1
    sum = 1
    for _ in range(0,i): 
        sum = (n**2) + 1
        n = sum
    return sum

def Sn2(i):
    """
    -------------------------------------------------------
    Description:
        Finds the ith number of the sequence Sn
        S(0) = 1
        S(n) = S(n-1)^2 + 1
        i     :    0    1    2    3    4    
        Sn2(i):    1    2    5    26   677
        Uses Recursion
    Assert: i is a non-negative integer
    Use: num = Sn2(i)
    -------------------------------------------------------
    Parameters:
        i: a non-negative number (int)
    Returns:
        number: the ith number in the Sn sequence (int)      
    -------------------------------------------------------
    """
    if i == 0:
        return 1
    return Sn2(i-1)**2+1
    
"""----------- Task 3 ------------"""
def countp1(list1):
    """
    -------------------------------------------------------
    Description:
        Counts number of positive numbers in a list
        Uses Loops
    Assert: 'list1' is a non-empty list
            No need to check if items are int/float
    Use: result = countp1(list1)
    -------------------------------------------------------
    Parameters:
        list1: list containing arbitrary numbers (list)
    Returns:
        result: number of positive numbers in list1 (int)        
    -------------------------------------------------------
    """
    assert isinstance(list1, list), "invalid list1"
    counter = 0
    for thing in list1:
        if thing > 0:
            counter += 1
    return counter

def countp2(list1):
    """
    -------------------------------------------------------
    Description:
        Counts number of positive numbers in a list
        Uses Recursion
    Assert: 'list1' is of type list
            No need to check if items are int/float
    Use: result = countp2(list1)
    -------------------------------------------------------
    Parameters:
        list1: list containing arbitrary numbers (list)
    Returns:
        result: number of positive numbers in list1 (int)        
    -------------------------------------------------------
    """
    assert isinstance(list1, list), "invalid list1"
    if list1 == []:
        return 0
    if list1[0] > 0:
        return 1 + int(countp2(list1[1:]))
    else:
        return 0 + int(countp2(list1[1:]))

    
"""----------- Task 4 ------------"""
def get_positives1(list1):
    """
    -------------------------------------------------------
    Description:
        Construct a list of positive numbers in list1
        Uses Loops
    Assert: 'list1' is of type list
            you do not need to assert that list1 items are numbers
    Use: pos_list = get_positives1(input_list):
    -------------------------------------------------------
    Parameters:
        list1: list containing numbers (list)
    Returns:
        pos_list: list containing positive numbers from list1 (list)        
    -------------------------------------------------------
    """
    assert isinstance(list1, list), "invalid list1"
    pos_list = []
    for item in list1:
        if item > 0:
            pos_list.append(item)
    return pos_list

def get_positives2(list1):
    """
    -------------------------------------------------------
    Description:
        Construct a list of positive numbers in list1
        Uses Recursion
    Assert: 'list1' is of type list
            you do not need to assert that list1 items are numbers
    Use: pos_list = get_positives2(input_list):
    -------------------------------------------------------
    Parameters:
        list1: list containing numbers (list)
    Returns:
        pos_list: list containing positive numbers from list1 (list)        
    -------------------------------------------------------
    """
    assert isinstance(list1, list), "invalid list1"
    if list1 == []:
        return []
    if list1[-1] < 0: # is 4 in rest of the bag, throw it out
        return get_positives2(list1[:-1])
    else:
        return get_positives2(list1[:-1]) + [list1[0]]

"""----------- Task 5 ------------"""
def find_depth1(list1):
    """
    -------------------------------------------------------
    Description:
        Finds the depth of a list
        Assume all list items are of same depth
        Uses loops
    Use: depth = find_depth1(list1)
    -------------------------------------------------------
    Parameters:
        list1: a list containing arbitrary items of same depth (list)
    Returns:
        depth: an integer reprsenting depth of a list
    -------------------------------------------------------
    """
    depth = 0
    while isinstance(list1,list):
        if list1 == []:
            break
        depth += 1
        list1 = list1[0]
    return depth

def find_depth2(list1):
    """
    -------------------------------------------------------
    Description:
        Finds the depth of a list
        Assume all list items are of same depth
        Uses Recursion
    Use: depth = find_depth2(list1)
    -------------------------------------------------------
    Parameters:
        list1: a list containing arbitrary items of same depth (list)
    Returns:
        depth: an integer reprsenting depth of a list
    -------------------------------------------------------
    """
    if isinstance(list1, list):
        if len(list1) == 0:
            return 0
        else:
            return 1 + max([find_depth2(l) for l in list1])
    else:
        return 0
