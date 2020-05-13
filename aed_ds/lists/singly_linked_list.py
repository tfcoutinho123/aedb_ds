from .tad_list import List
from .nodes import SingleListNode
from ..exceptions import EmptyListException, InvalidPositionException
from .singly_linked_list_iterator import SinglyLinkedListIterator

                                                    
class SinglyLinkedList(List):
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
    

    # Returns true iff the list contains no elements.

    def is_empty(self):
        return self.head == None

    # Returns the number of elements in the list.
    
    def size(self):
        return self.num_elements

    # Returns the first element of the list.
    # Throws EmptyListException.
    
    def get_first(self):
        if self.is_empty():
            raise EmptyListException()
        else:
            return self.head.get_element()
        

    # Returns the last element of  the list.
    # Throws EmptyListException.
    
    def get_last(self):            
        if self.is_empty():
            raise EmptyListException()
        else:
            return self.tail.get_element()
        

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    
    def get(self, position):
        if self.is_empty():
            raise EmptyListException()
        elif position >= self.size()-1 or position < 0:
            raise InvalidPositionException()        
        else:
            current_pos = 1
            current_node = self.head            
            while True:                       
                current_node = current_node.get_next()
                if current_pos == position:
                    return current_node.get_element()
                current_pos +=1


    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    
    def find(self, element):
        if self.size() == 0:
            return -1       
        position = 1
        current_node = self.head
        while position <= self.size()-1:
            current_node = current_node.get_next()                   
            if element == current_node.get_element():
                return position            
            position +=1
        return -1 
            

    # Inserts the specified element at the first position in the list.
    
    def insert_first(self, element):
        if self.is_empty():        
            new_node = SingleListNode(element, self.head)
            self.head = new_node
            self.tail = self.head
        else:
            previous_node = self.head
            self.head = SingleListNode(element, previous_node)
        self.num_elements +=1
        

    # Inserts the specified element at the last position in the list.
    
    def insert_last(self, element):        
        if self.is_empty():
            self.tail = SingleListNode(element, None)
            self.head = self.tail
        else:         
            self.tail.set_next(SingleListNode(element, None))
            self.tail = self.tail.get_next()
        self.num_elements +=1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    
    def insert(self, element, position):
        if position > self.size() or position < 0:
            raise InvalidPositionException()
        if position == 0:
            return self.insert_first(element)
        elif position == self.size()-1:
            return self.insert_last(element)
        current_pos = 0
        current_node=self.head            
        while True:
            previous = current_node            
            current_node = current_node.get_next()
            if current_pos == position:
                new_node = SingleListNode(element, current_node)
                previous.set_next(new_node)
                self.num_elements +=1
                break       
            current_pos +=1
     
        
    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    
    def remove_first(self): 
        if self.is_empty():
            raise EmptyListException()
        else:
            first_element = self.head
            self.head = self.head.get_next()
            self.num_elements -=1            
            return first_element.get_element()
            

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    
    def remove_last(self):
        if self.is_empty() == True:
            raise EmptyListException()          
        current_pos = 0
        current_node = self.head                       
        while current_pos != self.size()-2:
            if current_node.get_next() == None:
                break
            current_pos += 1
            current_node = current_node.get_next()                                                        
        current_node.set_next(None)
        self.tail = current_node
        self.num_elements -= 1
        return current_node.get_element()
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    
    def remove(self, position):
        if position >= self.size() or position < 0:
                raise InvalidPositionException()
        if position == 0:
            return self.remove_first()
        elif position == self.size() - 1:
            return self.remove_last()
        current_pos = 0
        current_node = self.head        
        while True:
            previous = current_node            
            current_node = current_node.get_next()
            if current_pos == position:
                previous.set_next(current_node.get_next())
                self.num_elements -=1
                break
            current_pos +=1       
    
    # Removes all elements from the list.
    
    def make_empty(self):
        self.num_elements = 0
        self.head = None
        self.tail = None

    # Returns an iterator of the elements in the list (in proper sequence).
    
    def iterator(self):        
        return SinglyLinkedListIterator(self.head)