from .tad_iterator import Iterator
from ..exceptions import NoSuchElementException

class SinglyLinkedListIterator(Iterator):
    def __init__(self, head):
        self.head = head
        self.current = head

    # Returns true iff the iteration has more elements.
    # In other words, returns true next would return an element rather than throwing an exception.
    def has_next(self):
        return self.current != None
        

    # Returns the next element in the iteration.
    # Throws NoSuchElementException
    
    def next(self):
        if self.current == None:
            raise NoSuchElementException()
        current_node = self.current
        self.current = self.current.get_next()
        return current_node.get_element()        


    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first element in the iteration.
    
    def rewind(self):
        self.current = self.head