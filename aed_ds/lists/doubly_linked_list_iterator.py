from .tad_iterator import TwoWayIterator
from ..exceptions import NoSuchElementException, EmptyListException


class DoublyLinkedListIterator(TwoWayIterator):
    def __init__(self, tail):        
        self.tail = tail
        self.current = tail        

    # Returns true iff the iteration has more elements in the reverse direction.
    # In other words, returns true if previous would return an element rather than throwing an exception.
    def has_previous(self):
        return self.current != None
    
    # Returns the previous element in the iteration.
    # Throws NoSuchElementException
    def previous(self):
        if self.current == None:
            raise NoSuchElementException()
        current_node = self.current
        self.current = self.current.get_previous()
        return current_node.get_element() 

    # Restarts the iteration in the reverse direction. After fullForward, if the iteration is not empty, previous will return the last element in the iteration.
    def full_forward(self):
        self.current = self.tail