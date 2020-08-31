"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""

from copy import deepcopy
from my_queue import Queue


# Assume you have random data and you want to search through it [1, 2, 3, //4, 5, 6]
# Linear search searches item by item and returns the key --> O(n) as the worst case
# Binary search to improve time complexity and efficient, i.e. set in the middle
# Check middle, if 2 is smaller then 4, drop right half of the list (greater size/value),
# then pick middle value, compare key to value
# Splitting anything to half is O(log n)
# Binary search without the need to sort the data, the data is sorted in a specific manner
# Can only have 2 children MAX
# Any to the right of the middle node value of the binary search tree must be bigger and left is smaller
#                      ------25----- Look for key = 12, 12 < 25 drop right half
#                     /             \
#                   13 -             35- Look for key = 12, 12 <13, drop right half
#                 /     \           /   \
#               11      19        33     40 Look for key = 12, 12 > 11, drop left half
#              /  \    /   \     /  \   /  \ 
#             9   12  18   20   30  34 38  44 Look for key = 12, found 12, Node = None, key found
#                                 \
#                                 32
class BSTNode:
    """
    ----------------------------------------------
    Implementation of a Binary Search Tree node
    ----------------------------------------------
    """

    def __init__(self, value):
        """
        -------------------------------------------------------
        Description:
            Creates and initializes a binary search tree node
            data is set to given values
            left and right pointers are set to None
            height is set to 1
        Assert: none
        Use: my_node = Node()
        -------------------------------------------------------
        Parameters:
            item: An arbitrary object (?)
        Returns:
            An object of type BSTNode 
        -------------------------------------------------------
        """ 
        # Similar to linked list, however we have two pointers, left and right
        self._data = deepcopy(value)
        self._left = None
        self._right = None
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns string representation of BSTNode
            Used for testing purposes
        Assert: none
        Use: str(my_node) or print(my_node)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string represenation of BSTNode
        -------------------------------------------------------
        """
        # print the data
        return str(self._data)

    def height(self):
        """
        -------------------------------------------------------
        Description:
            Returns the height of the node
            height = 1 + max(left_node_height,right_node_height)
            if node is None returns 0
        Assert: none
        Use: h = node.height()
        -------------------------------------------------------
        Parameters:
            none
        Returns:
            h: height of node (int)     
        -------------------------------------------------------
        """
        # how many levels are in the tree starting for a specific node, no children, the node has height of 1.
        return self._height_aux(self)
    
    def _height_aux(self, node):
        """
        -------------------------------------------------------
        Description:
            Private helper function that computes the height of a node
        Assert: none
        Use: h = self._height_aux(node)
        -------------------------------------------------------
        Parameters:
            node: a bst node (BSTNode)
        Returns:
            h: height of node (int)     
        -------------------------------------------------------
        """
        if node is None:
            return 0 
        # receives node and determines the height, similar to human speech
        return 1 + max(self._height_aux(node._left), self._height_aux(node._right))

    
class BST:
    """
    ----------------------------------------------
    Implementation of Binary Search Tree
    ----------------------------------------------
    """
    MAX_SIZE = 1000

    def __init__(self):
        """
        -------------------------------------------------------
        Description:
            Initializes an empty binary search tree
            root is set to None and count to 0
        Assert: none
        Use: bst = BST()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An object of type BST
        -------------------------------------------------------
        """
        # Needs a pointer to the first node, similar to linked list
        self._root = None
        # from the root node, you can make left and right, plus further branches
        self._count = 0  # Keep track of the nodes, since tree can do very deep
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns a string representation of bst
            Uses Breadth First Search (BFS)
        Assert: none
        Use: str(bst) or print(bst)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string representation of bst (str)
        -------------------------------------------------------
        """
        # You can all the way down print the depth (DFS depth first search) --> Stacks
        # Horizontal search, reads horizontally to prints (BFS breath first search) --> Queues
        q = Queue(self.MAX_SIZE)
        output = ''
        q.insert(self._root)
        level = 1
        # come back to this in WEEK #11
        while not q.is_empty():
            node = q.remove()
            if node is None:
                continue
            node_level = self.level(node._data)
            if node_level == level:
                output += str(node._data) + ' '
            elif node_level > level:
                output = output[:-1] + '\n'
                output += str(node._data) + ' '
                level += 1
            if node._left is not None:
                q.insert(node._left)
            if node._right is not None:
                q.insert(node._right)
        return output[:-1]
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            Check if bst is empty
        Assert: none
        Use: result = bst.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if bst is empty, False otherwise (bool) 
        -------------------------------------------------------
        """
        return self._root is None
    
    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Returns number of items in a bst
            same as number of nodes
        Assert: none
        Use: length = len(bst)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            length: number of items in bst       
        -------------------------------------------------------
        """
        return self._count
    
    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Description:
            Private helper method to search for given key in bst
            returns reference to node and its parent
            If not found returns None,None
        Assert: none
        Use: parent,node = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            parent: reference to the parent of the node containing key (BSTNode)
            node: reference to the node containing the key (BSTNode)
        -------------------------------------------------------
        """
        if key is None:
            return None, None
        # You want to return the parent node and node with the data
        parent = None
        node = self._root
        while node is not None and key != node._data:
            parent = node
            if key > node._data:  # if key is greater move to right side
                node = node._right
            else:  # if key is less move to left side
                node = node._left
                
        if node is None:
            parent = None
            
        return parent, node
    
    def find(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds and returns(retrives) a copy of item in bst that matches key.
            If item not found returns None
        Assert: none
        Use: item = bst.find(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            item: the full item matching key (?)
        -------------------------------------------------------
        """
        _, node = self._binary_search(key)
        if node is None:
            return None
        return deepcopy(node._data)

    def insert(self, item):
        """
        -------------------------------------------------------
        Description:
            inserts a copy of given item into bst
            Duplicates not allowed
            if insertion is successful, returns True, otherwise False
        Assert: none
        Use: success = bst.insert(item)
        -------------------------------------------------------
        Parameters:
            item - an item to be added (?)
        Returns:
            success: True/False (bool)     
        -------------------------------------------------------
        """
        # returns True or False
        # all items are unique in a binary search tree
        
        return self._insert_aux(self._root, item)

    def _insert_aux(self, node, item):
        """
        -------------------------------------------------------
        Description:
            Private helper function for insert method
            inserts a copy of given item into node
            Uses recursion
        Assert: none
        Use: success = self._insert_aux(node,item)
        -------------------------------------------------------
        Parameters:
            node - a bst node (BSTNode)
            item - an item to be added (?)
        Returns:
            success: True/False (bool)     
        -------------------------------------------------------
        """
        # Case 1: base case, add a new node to empty BST
        if self._root is None:  # self._root is a node
            self._count += 1
            self._root = BSTNode(deepcopy(item))  # creating a new node with item
            return True
        
        # Case 2: BST does not allow duplicates
        if item == node._data: 
            return False
        
        # Case 3: move right
        if item > node._data:
            if node._right is None:
                self._count += 1
                node._right = BSTNode(deepcopy(item))
                return True
            # if there's node, keep recursing and to add a new node
            return self._insert_aux(node._right, item)
        
        # Case 4: move left 
        if item < node._data:
            if node._left is None:
                self._count += 1
                node._left = BSTNode(deepcopy(item))
                return True
            return self._insert_aux(node._left, item)

    def height(self):
        """
        -------------------------------------------------------
        Description:
            Returns the height of a tree
            height of tree is the height of its root node
        Assert: none
        Use: h = bst.height()
        -------------------------------------------------------
        Parameters:
            none
        Returns:
            h: height of tree (int)     
        -------------------------------------------------------
        """
        if self._root is None:
            return 0 
        return self._root.height()  # we already made a method of it in Node Class
    
    def level(self, key):
        """
        -------------------------------------------------------
        Description:
            Returns the level of the given key in the bst
            if not found, prints error message and returns -1
        Assert: none
        Use: l = bst.level(key)
        -------------------------------------------------------
        Parameters:
            key: partial data to search for
        Returns:
            l: level of given key (int)
        -------------------------------------------------------
        """
        # Level you can't go from bottom to top
        # start from root and search for the node, increase level by one until you find the node you're
        # looking for
        _, node = self._binary_search(key)
        if node is None:
            print('Error(get_level): key not found')
            return -1 
        return self._get_level_aux(self._root, node, 1)
        
    def _get_level_aux(self, start, node, level):
        """
        -------------------------------------------------------
        Description:
           A private helper method method for level()
           Uses recursion to find level of given node compared to start node
        Assert: none
        Use: l = self._get_level_aux(start,node,starting_level)
        -------------------------------------------------------
        Parameters:
            start: node acting as a root of subtree (BSTNode)
            node: current node being examined to determine level (BSTNode)
            level: level of starting node
        Returns:
            l: level of node (int)
        -------------------------------------------------------
        """
        if start is None:
            return -1
        if start._data == node._data:
            return level
        # Looking into both sides, to determine the level
        new_level = self._get_level_aux(start._left, node, level + 1)
        # start at left and increment the level
        if new_level != -1:
            return new_level
        # What if I didn't find it, go to right side
        else:
            return self._get_level_aux(start._right, node, level + 1)
        
    def is_descendant(self, key1, key2):
        """
        -------------------------------------------------------
        Description:
             Check if key1 is a descendent of key2 in bst
        Assert: None
        Use: result = bst.is_descendent(key1,key2)
        -------------------------------------------------------
        Parameters:
            key1 - partial data (?)
            key2 - partial data (?)
        Returns:
            returns True/False (bool)    
        -------------------------------------------------------
        """
        # Key 1 is related to Key 2, Key 2's is ancestors of Key 1, looking for grandfathers and etc
        # Key 1 is like grandchildren
        _, node1 = self._binary_search(key1)
        _, node2 = self._binary_search(key2)
        if node1 is None or node2 is None:
            return False
        if node1 is node2:
            return False
        return self._is_descendant_aux(node1, node2)
    
    def _is_descendant_aux(self, node1, node2):
        """
        -------------------------------------------------------
        Description:
            Private helper function for is_descendant
        -------------------------------------------------------
        """
        # trying to find node1 is a descendant of node2
        if node2 is None:  # go all the way to the bottom, you haven't found a child
            return False
        if node2._left is node1 or node2._right is node1:
            return True  # is a descendant
        return self._is_descendant_aux(node1, node2._left) or self._is_descendant_aux(node1, node2._right)
        # node 2 keeps going down

    def remove(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds, removes, and returns the value in bst that matches key.
            if key not found returns None
            If bst is empty, prints an error message and returns None
        Assert: none
        Use: item = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            item: the full item matching key (?)
        -------------------------------------------------------
        """

        # Think of the overall structure of the remove method
        # Search for it and find it
        # if it is a leaf node with no children, just delete it
        # if the leaf node has a single children, you just promote it to the next level
        # if you have multiple children (2 or more), pick the largest value on the left subtree, and replaces the leaf
        # so it maintains the the structure of binary search tree
        # make sure the node selected on the left side is greater than all the values on the left subtree
        # and all the values on the right subtree is smaller than the selected node
        if self._root is None:
            print('Error(BST.remove): Cannot remove from any empty bst')
        self._root, item = self._remove_aux(self._root, key)  # the self._root might get updated
        return item

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Preconditions:
            node - a bst node to search for key (_BSTNode)
            key - data to search for (?)
        Postconditions:
            returns
            node - the current node or its replacement (_BSTNode)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        # First Step: Find the node containing the key
        if node is None:  # Base Case
            item = None
        elif key < node._data:  # Search left subtree
            node._left, item = self._remove_aux(node._left, key)
        elif key > node._data:  # Search right subtree
            node._right, item = self._remove_aux(node._right, key)
        
        # Item has been found
        else:  # Second Step: Find replacement
            item = node._data  # Extract the data
            self._count -= 1  # Decrement count
            # Case 1: node has no children, void it no real replacement is occurring
            if node._left is None and node._right is None:
                node = None
            # Case 2: node has no left child
            elif node._left is None:
                node = node._right
            # Case 3: node has no right child
            elif node._right is None:
                node = node._left
            # Case 4: node has two children
            else:  # Search for largest node in left subtree
                if node._left._right is None:  # Nothing on the right subtree of left subtree
                    replacement_node = node._left  # left child is replacement node
                else:  # find replacement node in right subtree of left node
                    replacement_node = self._delete_node_left(node._left)
                    replacement_node = node._left
                replacement_node._right = node._right
                node = replacement_node
        return node, item

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Preconditions:
            parent - node to search for largest value (_BSTNode)
        Postconditions:
            returns
            repl_node - the node that replaces the deleted node. This node 
            is the node with the maximum value in the deleted node's left
            subtree (_BSTNode)
        -------------------------------------------------------
        """
        # Find the largest child in the left subtree
        child = parent._right  # largest to the rig
        if child._right is None:
            # child has the largest value in the left subtree
            replacement_node = child
            # move child's left tree up
            parent._right = child._left
        else:  # other items in the right side of subtree
            replacement_node = self._delete_node_left(child)
        return replacement_node
    
    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: n = bst.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Postconditions:
            returns
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        return self._leaf_count_aux(self._root)

    def _leaf_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: n = bst.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Preconditions:
            node - a BST node (_BSTNode)
        Postconditions:
            returns
            count - number of nodes with no children below node (int)
        ---------------------------------------------------------
        """
        if node is None:
            count = 0
        elif node._left is None and node._right is None:
            count = 1  # You are the left node
        else:
            count = self._leaf_count_aux(node._left) + self._leaf_count_aux(node._right)
        return count
    
    def __contains__(self, item):
        _, node = self._binary_search(item)
        return node is not None
    
    def get_parent(self, key):
        parent, _ = self._binary_search(key)
        if parent is None:
            return None
        else:
            return parent._data
    
    def get_children(self, key):
        _, node = self._binary_search(key)
        if node is None:
            return None, None
        else:
            return node._left, node._right

    def max(self):
        current_node = self._root
        while current_node._right is not None:
            current_node = current_node._right
        max_data = current_node._data
        return max_data
        
    def min(self):
        current_node = self._root
        while current_node._left is not None:
            current_node = current_node._left
        min_data = current_node._data
        return min_data
    
    def is_ancestor(self, key1, key2):
        _, node1 = self._binary_search(key1)
        _, node2 = self._binary_search(key2)
        
        if node1 is None or node2 is None:
            return False
        
        if node1 is node2:
            return False
        
        return self._is_ancestor_aux(node1, node2)
    
    def _is_ancestor_aux(self, node1, node2):
        if node1 is None:
            return False
        if node1._left is node2 or node1._right is node2:
            return True
        return self._is_ancestor_aux(node1._left, node2) or self._is_ancestor_aux(node1._right, node2)

    def classify_node(self, key):
        parent, node = self._binary_search(key)
        
        if node is None:
            string = str(key) + ' is not found'
        
        elif parent is None:
            string = str(key) + ' is a root leaf node'
        
        elif node._left is not None or node._right is not None:
            string = str(key) + ' is a root node with one child'
        
        elif node._left is not None and node._right is not None:
            string = str(key) + ' is a root node with two children'
        
        elif node._left is None and node._right is None:
            string = str(key) + ' is a leaf node'
        else:
            string = str(key) + 'is not found'
            
        return string
