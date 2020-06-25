from .tad_stack import Stack
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyStackException, FullStackException

class ListStack(Stack):
    def __init__(self):
        self.stack = SinglyLinkedList()
        self.limit = None

    def is_empty(self):
        return self.stack.is_empty()

    def is_full(self):
        return self.size() == self.limit

    def size(self):
        return self.stack.size()

    def top(self):
        if self.is_empty():
            raise EmptyStackException()
        return self.stack.get_last()

    def push(self, element):
        if self.is_full():
            raise FullStackException()
        self.stack.insert_last(element)

    def pop(self):
        if self.is_empty():
            raise EmptyStackException()
        return self.stack.remove_last()