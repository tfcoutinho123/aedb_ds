from tad_list import List
import nodes
import exceptions
import doubly_linked_list_iterator 
from singly_linked_list import SinglyLinkedList as sll

class DoublyLinkedList(sll):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    # Returns the number of elements in the list.
    def size(self):
        return self.count

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        if not self.count == None:
            if position <= int(self.count/2):
                sll.get(self, position)
            elif position > int(self.count/2):
                current_node = self.tail
                for _ in range(self.count - 1, position, -1):
                    current_node = current_node.get_next()
                return current_node.get_element()
        else:
            exceptions.EmptyListException()   

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        new_node = nodes.DoubleListNode(element, self.head, None)
        self.head = new_node
        self.count += 1

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        new_node = nodes.DoubleListNode(element, None, self.tail)
        self.tail = new_node
        self.count += 1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        if position not in range(0, self.count):
            exceptions.InvalidPositionException()
        elif not self.count == None:
            if position == 0:
                self.insert_first(element)
            elif position == self.count:
                self.insert_last(element)
            elif position <= int(self.count/2):
                sll.insert(self, element, position)
            elif position > int(self.count/2):
                new_node = nodes.DoubleListNode(element, None, None)
                previous_node = self.tail
                current_node = self.tail.get_previous()
                for _ in range(self.tail, position-1):
                    previous_node = previous_node.get_previous()
                    current_node = current_node.get_previous()
                previous_node.set_previous(new_node)
                new_node.set_previous(current_node)
                self.count += 1      
        else:
            exceptions.EmptyListException() 

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self): pass

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self): pass
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position): pass
    
    # Removes all elements from the list.
    def make_empty(self): pass

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self): pass
