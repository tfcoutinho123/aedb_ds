from .tad_tree import Tree
from ..dictionaries.tad_ordered_dictionary import OrderedDictionary
from ..exceptions import DuplicatedKeyException, NoSuchElementException, \
    EmptyDictionaryException, EmptyTreeException
from .nodes.binary_nodes import BinarySearchTreeNode


class BinarySearchTree(OrderedDictionary, Tree):
    def __init__(self):
        self.root = None
        self.num_elements = 0
    
    # Returns the number of elements in the dictionary.
    def size(self):
        return self.num_elements

    # Returns true if the dictionary is full.
    def is_full(self):
        return False

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, k):       
        return self.get_value(self.root, k)                       

    def get_value(self, root, k):
        if root == None:
            raise NoSuchElementException()
        elif root.get_key() == k:
            return root.get_element()      
        elif root.get_left_child() != None and k < root.get_key():
            return self.get_value(root.get_left_child(), k)                    
        elif root.get_right_child() != None and k > root.get_key():
            return self.get_value(root.get_right_child(), k)             
        

    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    def insert(self, k, v): 
        self.root = self.insert_element(self.root, k, v)
    
    def insert_element(self, root, k, v):
        if root == None:
            root = BinarySearchTreeNode(k, v)
            self.num_elements += 1
        elif root.get_key() == k:
            raise DuplicatedKeyException()
        elif root.get_key() > k:
            node = self.insert_element(root.get_left_child(), k, v)
            root.set_left_child(node)
        else:
            node = self.insert_element(root.get_right_child(), k, v)
            root.set_right_child(node)
        return root


    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, k, v):
        self.update_value(self.root, k, v)

    def update_value(self, root, k, v):
        if root == None:
            raise NoSuchElementException()
        elif root.get_key() == k:
            root.set_element(v)
        elif root.get_key() > k:
            self.update_value(root.get_left_child(), k, v)            
        elif root.get_key() < k:
            self.update_value(root.get_right_child(), k, v)
        

    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, k):
        self.root = self.remove_root(self.root, k)    

    def remove_root(self, root, k):
        if root == None:
            raise NoSuchElementException()
        elif root.get_key() > k:
            self.remove_root(root.get_left_child(), k)
        elif root.get_key() < k:
            self.remove_root(root.get_right_child(), k)
        elif root.get_key() == k and (root.is_leaf() or self.num_elements == 1):
            root = None
            self.num_elements =-1
            return root
        elif root.get_key() == k and root.get_right_child() == None:
            root = root.get_left_child()
            self.num_elements =-1 
            return root             
        elif root.get_key() == k and root.get_left_child() == None:            
            min_node = self.get_min_node(root.get_right_child())
            min_node_key = min_node.get_key()
            min_node.set_right_child(root.get_right_child())
            root = min_node
            min_node.set_left_child(None)
            min_node.set_right_child(None)            
            self.remove_root(root, min_node_key)
            return root                 
        elif root.get_key() == k and (root.get_left_child() and root.get_right_child() != None):
            min_node = self.get_min_node(root.get_right_child())
            min_node_key = min_node.get_key()
            min_node.set_left_child(root.get_right_child())
            min_node.set_right_child(root.get_right_child())
            root = min_node
            min_node.set_left_child(None)
            min_node.set_right_child(None)
            self.remove_root(root, min_node_key)         
            return root
        
        

    # Returns a List with all the keys in the dictionary.
    def keys(self): pass
        

    # Returns a List with all the values in the dictionary.
    def values(self): pass

    # Returns a List with all the key value pairs in the dictionary.
    def items(self): pass

    # Returns an iterator of the elements in the dictionary
    def iterator(self): pass

    # Returns the element with the smallest key
    # Throws EmptyTreeException
    def get_min_element(self):
        if self.is_empty():
            raise EmptyTreeException()
        return self.get_min_node(self.root).get_element()
    
    def get_min_node(self, root):
        if root.get_left_child() is None:
            return root
        else:
            return self.get_min_node(root.get_left_child())
    
    # Returns the element with the largest key
    # Throws EmptyTreeException
    def get_max_element(self):
        if self.is_empty():
            raise EmptyTreeException()
        else:
            return self.get_max_node(self.root).get_element()

    def get_max_node(self, root):
        if root.get_right_child() is None:
            return root
        return self.get_max_node(root.get_right_child())

    # Returns the root of the tree
    # Throws EmptyTreeException
    def get_root(self):
        if self.is_empty():
            raise EmptyTreeException()
        return self.root.get_element()        

    # Returns the height of the tree
    # Throws EmptyTreeException
    def height(self):
        return self.get_height(self.root)

    def get_height(self, root):
        if self.is_empty():
            raise EmptyTreeException()
        elif root == None:
            return 0
        else:
            left_height = self.get_height(root.get_left_child())
            right_height = self.get_height(root.get_right_child())
            if(left_height > right_height):
                return 1 + left_height
            else:
                return 1 + right_height

         

    # Returns True if the tree is empty
    def is_empty(self):
        return self.num_elements == 0