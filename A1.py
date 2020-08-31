"""
-------------------------
# Student Name: Quynh Dao
# Student ID: 130440130
# Student email: daox0130@mylaurier.ca
#-------------------------
"""
def read_airports(filename):
    """
    -------------------------------------------------------
    Description:
        Reads a file containing airport records. File format:
        (code)-province:airport_name
        The code-name is stored in a dictionary
        list of provinces is stored in a set
    Use: airport_dict,province_set = read_airpors(filename)
    -------------------------------------------------------
    Parameters:
        filename - name of file (str)
    Returns:
        airport_dict - dictionary containing codes & airport names (dict)
        province_set - set of provinces (set)            
    -------------------------------------------------------
    """
    file = open(filename)
    
    province_set = set()
    airport_dict = {}
    
    for line in file:
        key = line[1:4]
        
        k = line.find('-')
        i = line.find(':')
        
        province_set.add(line[k+1:i])
        value = line[i+1:].strip('\n')
        airport_dict[key] = value
        
    file.close()
    
    return airport_dict, province_set

def query_airports_DB(code_name_dict,prov_code_dict):
    """
    -------------------------------------------------------
    Description:
        Constructs a dictionary such taht:
            - Key is a province
            - Value is a tuple containing all airport names in that province
        Two dictionaries are given:
            1- Code - airport name
            2- province - string of airport codes separated by a space
    Use: dict3 = query_airports_DB(dict1,dict2)
    -------------------------------------------------------
    Parameters:
        code_name_dict - dictionary of codes-names (dict)
        prov_code_dict - dictionary of provinces-codes (dict)
    Returns:
        prov_name_dict - dictionary of province-names (dict)          
    -------------------------------------------------------
    """
    values = []
    keys = []
    for x in prov_code_dict.items():
        keys.append(x[0])
        sub_list = []
        codes = x[1].split(' ')
        for y in range(len(codes)):
            z = code_name_dict.get(codes[y])
            sub_list.append(z)
        values.append(sub_list)
    
    tuple_values = tuple(map(tuple,values))
    tuple_keys = tuple(keys)

    prov_code_dict = dict(zip(tuple_keys,tuple_values))
    
    return prov_code_dict
        
def is_array(data):
    """
    -------------------------------------------------------
    Description:
        Checks if given data is an array.
        An array is: an ordered and mutable data structure
            all elements are of the same type
            if elements are collections, then they all share same size
    Use: result = is_array(data)
    -------------------------------------------------------
    Parameters:
        data - an arbitrary data to be tested (data)
    Returns:
        True if data is an array and False otherwise         
    -------------------------------------------------------
    """
    result = False
    i = 0
    if isinstance(data,list):
        if data == []:
            result = True
        else: 
            while i < len(data)-1:
                if type(data[i]) == type(data[i+1]):
                    if len(data[i]) == len(data[i+1]):
                        result = True
                    else:
                        result = False
                        break
                else:
                    result = False
                    break
                i += 1
            
    if isinstance(data, dict):
        if data == {}:
            result = True
        else:
            while i < len(data)-1:
                if type(data[i]) == type(data[i+1]):
                    if len(data[i]) == len(data[i+1]):
                        result = True
                    else:
                        result = False
                        break
                else:
                    result = False
                    break
                i += 1
    
    if isinstance(data, tuple):
        result = False
    
    if isinstance(data, set):
        result = False
    return result

def get_num_baskets(collection):
    """
    -------------------------------------------------------
    Description:
        Read numbers stored in a collection
        constructs a list containing baskets.
        A basket is a set containing all numbers of equal #digits
        basket0: contains single-digit numbers
        basket1: contains 2-digit numbers
        ...
        If input is not a list,tuple or set, print error and return empty set
    Use: baskets = get_num_baskets(collection)
    -------------------------------------------------------
    Parameters:
        collection - a collection containing numbers (list,tuple,set)
    Returns:
        baskets = list containing sets of numbers (list)
    -------------------------------------------------------
    """
    empty = [(),[],{}]
    baskets = []   
    i = 0
    j = 0
            
    if isinstance(collection, tuple) and collection not in empty:
        maximum = max(collection)
        largest_basket = len(str(maximum)) 
        
        for _ in range(largest_basket):
            baskets.append(set())
        while i < largest_basket:
            while j < len(collection):
                size = len(str(collection[j]).strip('-'))
                if size == 1:
                    baskets[0].add(collection[j])
                elif size == 2:
                    baskets[1].add(collection[j])
                elif size == 3:
                    baskets[2].add(collection[j])
                elif size == 4:
                    baskets[3].add(collection[j])
                elif size == 5:
                    baskets[4].add(collection[j])
                j += 1
            i += 1
      
    elif isinstance(collection, set) and collection not in empty:
        maximum = max(collection)
        largest_basket = len(str(maximum))
        
        for _ in range(largest_basket):
            baskets.add(set())
            
        while i < largest_basket:
            while j < len(collection):
                size = len(str(collection[j]).strip('-'))
                if size == 1:
                    baskets[0].add(collection[j])
                elif size == 2:
                    baskets[1].add(collection[j])
                elif size == 3:
                    baskets[2].add(collection[j])
                elif size == 4:
                    baskets[3].add(collection[j])
                elif size == 5:
                    baskets[4].add(collection[j])
                j += 1
            i += 1

    elif isinstance(collection, list) and collection not in empty:
        maximum = max(collection)
        largest_basket = len(str(maximum))
        
        for _ in range(largest_basket):
            baskets.append(set())
            
        while i < largest_basket:
            while j < len(collection):
                size = len(str(collection[j]).strip('-'))
                if size == 1:
                    baskets[0].add(collection[j])
                elif size == 2:
                    baskets[1].add(collection[j])
                elif size == 3:
                    baskets[2].add(collection[j])
                elif size == 4:
                    baskets[3].add(collection[j])
                elif size == 5:
                    baskets[4].add(collection[j])
                j += 1
            i += 1
    elif collection in empty:
        return []
    else:
        print('Error(get_num_baskets): input is not a valid collection')
        return []
    
    return baskets

def is_valid_container(text):
    """
    -------------------------------------------------------
    Description:
        Checks if given string represent a valid python container (list,tuple,set) 
        assume the string contains no spaces
    Use: result = is_valid_container(text)
    -------------------------------------------------------
    Parameters:
        text - a string representing a python container (text)
    Returns:
        True if text is a valid container and Fralse otherwise
    -------------------------------------------------------
    """
    
    start = ['(', '[','{']
    end = [')',']','}']
    white_space = ' '
    
    if type(text) != str:
        return None
    elif white_space in text:
        return False
    else:
        if text[0] in start and text[-1] in end:
            if len(text) == 2:
                return True
            container = text[1:-1].split(',')
            for i in container:
                if i == '':
                    if text[0] == '(' and text [-1] == ')' and len(text) == 4:
                        return True
                    return False
            if text[0] == '[' and text[-1] == ']':
                return True
            elif text[0] == '{' and text[-1] == '}':
                return True
            elif text[0] == '(' and text [-1] == ')':
                if len(text) == 3:
                    return False
                return True
            else:
                return False
    return False

    
        
        
    