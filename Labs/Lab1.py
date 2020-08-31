def flip_list_dict(collection):
    """
    -------------------------------------------------------
    Description:
        Checks input, if it is a 2D list convert to dictionary
        If it is a dictionary convert to a 2D list
        If not dict or list, print error message and return None
    Use: output = flip_list_dict(collection)
    -------------------------------------------------------
    Parameters:
        collection - any input to be tested (?)
    Returns:
        output - result of flip operation (dict or list or None)            
    -------------------------------------------------------
    """
    keys = []
    values = []
    
    output = None
    
    if isinstance(collection, list):
        for x in collection:
            keys.append(x[0])
            values.append(x[1])
            
        output = {key:value for key, value in zip(keys,values)}
                        
                
    elif isinstance(collection, dict):
        output = []
        for item in collection.items():
            sub_list = []
            sub_list.append(item[0])
            sub_list.append(item[1])
            output.append(sub_list)
    else:
        print('Error(flip_list_dict): input is not a list or dict')
        
    return output

"""-----------------------------------------------------------"""

def file_to_dict(filename):
    """
    -------------------------------------------------------
    Description:
        Converts contents of a file into dictionary
        File is formatted as: text1-text2
        The key should be text1 and the value is text2
    Use: output = file_to_dict(filename)
    -------------------------------------------------------
    Parameters:
        filename - name of file used in reading (str)
    Returns:
        output - dictionary containing contents of the file (dict)            
    -------------------------------------------------------
    """
    file = open(filename)
    output = {}
    for line in file:
        i = line.find('-')
        key = line[:i]
        value = line[i+1:].strip('\n')
        output[key] = value
    file.close()
    return output

"""-----------------------------------------------------------"""

def get_list_report(list1,list2):
    """
    -------------------------------------------------------
    Description:
        Finds intersection,union and symmetric difference of two lists
        intersection: items that appear in both lists
        union: items that appear in one or both lists
        symmetric difference: items that appear only in one of the lists
    Use: intersection,union,difference = get_list_report(list1,list2)
    -------------------------------------------------------
    Parameters:
        list1 - first list (list1)
        list2 - second list (list2)
    Returns:
        intersection - intersection of list1 and list2 (list)
        unioin - union of list1 and list2 (list)
        difference - symmetric difference of list1 and list2            
    -------------------------------------------------------
    """
    i = 0
    intersection = []
    union = list(set(list1) | set(list2))
    difference = list(set(list1) ^ set(list2))
    difference.sort()
    while i < len(list1):
        if list1[i] in list2:
            intersection.append(list1[i])
        i += 1
    
    return intersection, union, difference

"""-----------------------------------------------------------"""

def get_tuple_info(input_tuple):
    """
    -------------------------------------------------------
    Description:
        Makes three checks about a given tuple:
        1- Numeric: is all elements in the tuple numbers?
        2- Unique: Are all elements in the tuple distinct?
        3- Uniform: Are all elements in the tuple the same?
    Use: numeric,unique,uniform = get_tuple_info(input_tuple)
    -------------------------------------------------------
    Parameters:
        input_tuple - input tuple to be analyzed (tuple)
    Returns:
        numeric - True if all elements are numbers, False otherwise
        unique - True if all elements are distinct, False otherwise
        uniform - True if all elements are the same, False otherwise     
    -------------------------------------------------------
    """
    numeric = False
    unique = False
    uniform = False
    li = list(input_tuple)
    
    uniques = []
    
    for i in li:
        if is_instance(i, int):
            numeric = True
        elif is_instance(i, float):
            numeric = True
        break
    
    if input_tuple == ():
        unique = False
        
    elif len(li) == len(set(input_tuple)):
        unique = True
    
    for i in range(len(li)-1):
        if li[i] == li[i+1]:
            uniform = True

    return numeric, unique, uniform

"""-----------------------------------------------------------"""

def remove_duplicates(data):
    """
    -------------------------------------------------------
    Description:
        Remove all duplicates from a given collection
        if input is not a collection, print an error message and return None
    Use: updated_data = remove_duplicates(data)
    -------------------------------------------------------
    Parameters:
        data - a collection (?)
    Returns:
        updated_data: original data after removing duplicates (?)    
    -------------------------------------------------------
    """
    i = 0
    updated_data = []
    li = list(data)
    while i < len(li):
        if li[i] not in updated_data:
            updated_data.append(li[i])
        i += 1
    if type(data) == tuple:
        updated_data = tuple(updated_data)
    elif type(data) == set:
        updated_data = set(updated_data)
    else:
        updated_data = list(updated_data)
    return updated_data
