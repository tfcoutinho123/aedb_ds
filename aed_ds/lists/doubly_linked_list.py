from .singly_linked_list import SinglyLinkedList
from .nodes import DoubleListNode
from ..exceptions import InvalidPositionException, EmptyListException
from .doubly_linked_list_iterator import DoublyLinkedListIterator

class DoublyLinkedList(SinglyLinkedList):
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
        return self.head.get_element()

    # Returns the last element of the list.
    # Throws EmptyListException.
    
    def get_last(self):
        return self.tail.get_element()

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    
    def get(self, position):
        if position >= self.size() or position < 0:
            raise InvalidPositionException("Invalid Position.")
        if position == 0:
            return self.get_first()
        elif position == self.size() - 1:
            return self.get_last()
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
        if element == self.head.get_element():
            return 0
        elif element == self.tail.get_element():
            return self.size()-1
        position = 1
        current_node = self.head
        while True:
            if position > self.size()-1:
                return -1
            current_node = current_node.get_next()
            if element == current_node.get_element():
                return position
            position +=1

    # Inserts the specified element at the first position in the list.
    
    def insert_first(self, element):        
        new_node = DoubleListNode(element, self.head, None)
        self.head = new_node
        self.tail = self.head       
        self.num_elements +=1

    # Inserts the specified element at the last position in the list.
    
    def insert_last(self, element):
        new_node = DoubleListNode(element, None, self.tail)
        self.tail.set_next(new_node)
        self.tail = new_node
        self.num_elements +=1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    
    def insert(self, element, position):
        if position > self.size() or position < 0:
            raise InvalidPositionException("Invalid Position.")
        if position == 0:
            return self.insert_first(element)
        elif position == self.size():
            return self.insert_last(element)
        current_pos = 1
        current_node=self.head            
        while True:
            previous = current_node            
            current_node = current_node.get_next()
            if current_pos == position:
                new_node = DoubleListNode(element, current_node, previous)
                current_node.set_previous(new_node)
                previous.set_next(new_node)
                self.num_elements +=1
                break       
            current_pos +=1

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    
    def remove_first(self):
        if self.is_empty() == True:
            raise EmptyListException("List is empty.")
        else:
            first_element = self.head.get_element()
            self.head = self.head.get_next()
            self.head.set_previous(None)
            self.num_elements -=1            
            return first_element
            

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    
    def remove_last(self):
        if self.is_empty() == True:
            raise EmptyListException("List is empty.")
        else:
            self.tail = self.tail.get_previous()
            self.tail.set_next(None)
            self.num_elements +=1
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    
    def remove(self, position):
        if position >= self.size() or position < 0:
                raise InvalidPositionException("Invalid Position.")
        if position == 0:
            return self.remove_first()
        elif position == self.size() - 1:
            return self.remove_last()
        current_pos = 1
        current_node = self.head        
        while True:
            previous = current_node            
            current_node = current_node.get_next()
            if current_pos == position:                
                previous.set_next(current_node.get_next())
                current_node.get_next().set_previous(previous)
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
        iterator = DoublyLinkedListIterator(self.tail)        
        while iterator.has_previous() != False:
            elem = iterator.previous()
            print(elem)