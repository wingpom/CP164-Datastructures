"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""
def recurrence1(i):
    """
    -------------------------------------------------------
    Description:
        Finds the ith number in the following recurrence equation:
            S(0) = 10
            S(1) = 25
            S(n) = 3*S(n/2) - 4*S(n-2)
        Note use integer division for S(n/2)
        Uses loops
    Assert: i is a positive integer
    Use: num = recurrence1(i)
    -------------------------------------------------------
    Parameters:
        i: a non-negative number (int)
    Returns:
        number: the ith number in the recurrene equation (int)         
    -------------------------------------------------------
    """
    assert(isinstance(i, int) and i >= 0), 'invalid i'
    if i == 0:
        return 10
    if i == 1:
        return 25
    
    seq_terms = [10,25]
    
    for n in range(2,i+1):
        s_n = (n//2)
        first_term = seq_terms[s_n]
        
        s_n1 = n-2
        second_term = seq_terms[s_n1]
        
        seq = 3*first_term - 4*second_term
        
        if seq not in seq_terms:
            seq_terms.append(seq)
    return seq

def recurrence2(i):
    """
    -------------------------------------------------------
    Description:
        Finds the ith number in the following recurrence equation:
            S(0) = 10
            S(1) = 25
            S(n) = 3*S(n/2) - 4*S(n-2)
        Note use integer division for S(n/2)
        Uses Recursion
    Assert: i is a positive integer
    Use: num = recurrence2(i)
    -------------------------------------------------------
    Parameters:
        i: a non-negative number (int)
    Returns:
        number: the ith number in the recurrene equation (int)         
    -------------------------------------------------------
    """
    assert(isinstance(i, int) and i >= 0), 'invalid i'
    if i == 0:
        return 10
    if i == 1:
        return 25
    return 3*recurrence2(i//2) - 4*recurrence2(i-2)

def sum_of_squares1(n):
    """
    -------------------------------------------------------
    Description:
        Finds the sum of squares from 1 to n if n > 0:
            1^2 + 2^2 + 3^2 + ... + n^2
        If n < 0, finds sum of squares from n to -1
            n^2 + ... + -3^2 + -2^2 + -1^2
        For n == 0 returns 0
        Uses loops
    Assert: n is an integer
    Use: total = sum_of_squares1(n)
    -------------------------------------------------------
    Parameters:
        n: an integer referring to upper bound for summation step (int)
    Returns:
        total: sum of squares (int)         
    -------------------------------------------------------
    """
    assert(isinstance(n, int)), 'invalid n'
    if n == 0:
        return 0
    total = 0
    for i in range(1,abs(n)+1):
        total += i**2
    return total

def sum_of_squares2(n):
    """
    -------------------------------------------------------
    Description:
        Finds the sum of squares from 1 to n if n > 0:
            1^2 + 2^2 + 3^2 + ... + n^2
        If n < 0, finds sum of squares from n to -1
            n^2 + ... + -3^2 + -2^2 + -1^2
        For n == 0 returns 0
        Uses Recursion
    Assert: n is an integer
    Use: total = sum_of_squares2(n)
    -------------------------------------------------------
    Parameters:
        n: an integer referring to upper bound for summation step (int)
    Returns:
        total: sum of squares (int)         
    -------------------------------------------------------
    """
    assert(isinstance(n, int)), 'invalid n'
    if n == 0:
        return 0
    return abs(n)**2 + sum_of_squares1(abs(n)-1)

def select_upper1(text,letter):
    """
    -------------------------------------------------------
    Description:
        replace every occurrence of 'letter' in 'text' with upper case
        Function does not change text, returns the updated version of text
        Uses loops
    Assert: text is a string
            letter is a string containing a single lower case alphabet
    Use: modified_text = select_upper1(text,letter)
    -------------------------------------------------------
    Parameters:
        text: a string of arbitrary lenght (str)
        letter: a single lower case character (str)
    Returns:
        modified_text: modified version of the text (str)         
    -------------------------------------------------------
    """
    assert isinstance(text, str), 'invalid text'
    assert(isinstance(letter, str) and letter.islower()), 'invalid letter'
    modified_text = ''
    for char in text:
        if char == letter:
            modified_text += char.upper()
        else:
            modified_text += char
    return modified_text

def select_upper2(text,letter):
    """
    -------------------------------------------------------
    Description:
        replace every occurrence of 'letter' in 'text' with upper case
        Function does not change text, returns the updated version of text
        Uses recursion
    Assert: text is a string
            letter is a string containing a single lower case alphabet
    Use: modified_text = select_upper2(text,letter)
    -------------------------------------------------------
    Parameters:
        text: a string of arbitrary lenght (str)
        letter: a single lower case character (str)
    Returns:
        modified_text: modified version of the text (str)         
    -------------------------------------------------------
    """
    assert isinstance(text, str), 'invalid text'
    assert(isinstance(letter, str) and letter.islower()), 'invalid letter'
    modified_text = ''
    if text == '':
        return ''
    if text[0] == letter:
        modified_text = text[0].upper() + select_upper2(text[1:], letter) 
    else:
        modified_text = text[0] + select_upper2(text[1:], letter)
    return modified_text 


def is_capitalized1(word):
    """
    -------------------------------------------------------
    Description:
        Checks if given word is capitalized
        Capitalized = first letter is upper case and all other letters are lower case
        Assume that if the input is a string, then it is a non-empty single-word
        Uses loops
    Assert: word is a string
    Use: result = is_capitalized1(word)
    -------------------------------------------------------
    Parameters:
        word: a non-empty single word (str)
    Returns:
        result: True/False (bool)       
    -------------------------------------------------------
    """
    assert isinstance(word, str), 'invalid word'
    result = True
    if word[0].isupper() and len(word) == 1:
        result = True
    elif word[0].isupper() and len(word) > 1:
        for char in word[1:]:
            if char.islower():
                continue
            else:
                result = False
                break
    else:
        result = False
    return result

def is_capitalized2(word):
    """
    -------------------------------------------------------
    Description:
        Checks if given word is capitalized
        Capitalized = first letter is upper case and all other letters are lower case
        Assume that if the input is a string, then it is a non-empty single-word
        Uses recursion
    Assert: word is a string
    Use: result = is_capitalized2(word)
    -------------------------------------------------------
    Parameters:
        word: a non-empty single word (str)
    Returns:
        result: True/False (bool)       
    -------------------------------------------------------
    """
    # one letter, A --> is upper 0
    # two letter, AB --> is upper then lower 0 1
    # three letter, Abc --> is upper then lower lower 0 1 2
    assert isinstance(word, str), 'invalid word'
    result = False
    if word[0].isupper() and len(word) == 1:
            result = True 
    if word[0].isupper() and len(word) > 1:
        if word[1:].islower():
            is_capitalized2(word[1:])
            result = True
    return result

def is_title1(text):
    """
    -------------------------------------------------------
    Description:
        Checks if every word in the given text is capitalized
        Capitalized = first letter is upper case and all other letters are lower case
        Assume that input is always a non-empty string
        Uses loops
    Assert: no asserts
    Use: result = is_title1(word)
    -------------------------------------------------------
    Parameters:
        text: a non-empty string of arbitrary length (str)
    Returns:
        result: True/False (bool)
    -------------------------------------------------------
    """
    result = True
    count = 0
    li = text.split(' ')
    for i in range(len(li)):
        result = is_capitalized1(li[i])
        if result == False:
            count += 1
    if count != 0:
        result = False
    return result

def is_title2(text):
    """
    -------------------------------------------------------
    Description:
        Checks if every word in the given text is capitalized
        Capitalized = first letter is upper case and all other letters are lower case
        Assume that input is always a non-empty string
        Uses recursion
    Assert: no asserts
    Use: result = is_title2(word)
    -------------------------------------------------------
    Parameters:
        text: a non-empty string of arbitrary length (str)
    Returns:
        result: True/False (bool)
    -------------------------------------------------------
    """
    array = text.split(' ')
    if len(array) == 1:
        result = is_capitalized2(array[0])
   
    elif len(array) > 1:
        result = is_capitalized2(array[0])
        if result == False:
            return False
        text = ' '.join(array[1:])
        is_title2(text) 
    return result

def binary_flip1(list1):
    """
    -------------------------------------------------------
    Description:
        Pick the first pair of items in a list and swap them
        Repeats the above until the end of list
        If list length is odd, no swaps for the last item
        Function does not change the input list, returns a new list
        Uses loops
    Assert: list1 is a list
    Use: list2 = binary_flip(list1)
    -------------------------------------------------------
    Parameters:
        list1: a list containing arbitrary items (list)
    Returns:
        list2: updated version of list1 (list)
    -------------------------------------------------------
    """
    assert isinstance(list1, list), 'invalid list1'
    list2 = []
    if list1 == []:
        return []
    elif len(list1) == 1:
        return list1
    elif len(list1)%2 == 0:
        for i in range(0,len(list1)-1,2):
            list2.append(list1[i+1])
            list2.append(list1[i])
    else: 
        for i in range(0,len(list1)-1,2):
            list2.append(list1[i+1])
            list2.append(list1[i])
        list2.append(list1[len(list1)-1])
    return list2
    
def binary_flip2(list1):
    """
    -------------------------------------------------------
    Description:
        Pick the first pair of items in a list and swap them
        Repeats the above until the end of list
        If list length is odd, no swaps for the last item
        Function does not change the input list, returns a new list
        Uses Recursion
    Assert: list1 is a list
    Use: list2 = binary_flip2(list1)
    -------------------------------------------------------
    Parameters:
        list1: a list containing arbitrary items (list)
    Returns:
        list2: updated version of list1 (list)
    -------------------------------------------------------
    """
    assert isinstance(list1, list), 'invalid list1'
    if list1 == []:
        return []
    if len(list1) == 1:
        return list1
    list2 = [list1[1]] + [list1[0]] + binary_flip2(list1[2:])
    return list2

