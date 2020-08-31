"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""
from copy import deepcopy

from bst import BST


def tree_sort(self):
    tree = BST()
    if self is []:
        return []
    for i in range(len(self)):
        tree.insert(self[i])
    items = tree.inorder2()
    return items


def tree_sort_r(data):
    tree = BST()
    if len(data) == 0:
        return data
    tree.insert(data[0:])
    return tree.inorder2()


def _swap(data, i, j):
    temp = deepcopy(data[i])
    data[i] = deepcopy(data[j])
    data[j] = deepcopy(temp) 
    return


def selection_sort(data):
    # we need to iterate through all the items in list and swap with last item
    for i in range(len(data)):
        # find the minimum element in unsorted sublist
        min_indx = i
        for j in range(i + 1, len(data)):  # we find to start with right side which is unsorted
            if data[min_indx] < data[j]:
                min_indx = j
        
        # swap minimum with the last item in the sorted list 
        _swap(data, min_indx, i)
    return 


def selection_sort_r(data):
    _selection_sort_r_aux(data, 0)
    return 


def _selection_sort_r_aux(data, i):
    if i == len(data):
        return 
    min_indx = _min_r(data, i, i)
    # swap minimum with the last element in sorted sublist
    _swap(data, min_indx, i)
    _selection_sort_r_aux(data, i + 1)
    return


def _min_r(data, i, min_indx):
    if i == len(data):
        return min_indx 
    if data[i] > data[min_indx]:
        min_indx = i
    return _min_r(data, i + 1, min_indx)

    
def _merge(data, first, middle, last, mode):
    temp = []
    i = first 
    j = middle + 1 
    if mode == 'A':
        # compare left-most elements in both left and right sublists 
        while i <= middle and j <= last:
            if data[i] <= data[j]:  # select from left sublist 
                temp.append(data[i])
                i += 1
            else:  # select from right sublist 
                temp.append(data[j])
                j += 1
        # copy any remaining elements from the left sublist 
        while i <= middle:
            temp.append(data[i])
            i += 1
            
        # copy any remaining elements from the right sublist 
        while j <= last:
            temp.append(data[j])
            j += 1
            
        # copy the resulting "sorted sublist" back to original list 
        i = 0 
        while i < len(temp):
            data[first + i] = temp[i]
            i += 1
    else:
        # compare left-most elements in both left and right sublists 
        while i <= middle and j <= last:
            if data[i] >= data[j]:  # select from left sublist 
                temp.append(data[i])
                i += 1
            else:  # select from right sublist 
                temp.append(data[j])
                j += 1
        # copy any remaining elements from the left sublist 
        while i <= middle:
            temp.append(data[i])
            i += 1
            
        # copy any remaining elements from the right sublist 
        while j <= last:
            temp.append(data[j])
            j += 1
            
        # copy the resulting "sorted sublist" back to original list 
        i = 0 
        while i < len(temp):
            data[first + i] = temp[i]
            i += 1
    return 


def _merge_sort_r_aux(data, first, last, mode):
    if first >= last:
        return 
    
    middle = (last - first) // 2 + first
    _merge_sort_r_aux(data, first, middle, mode)
    _merge_sort_r_aux(data, middle + 1, last, mode)
    _merge(data, first, middle, last, mode)
    return 

        
def merge_sort_r(data, mode):
    _merge_sort_r_aux(data, 0, len(data) - 1, mode)
    return 
