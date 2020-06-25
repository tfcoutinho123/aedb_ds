from .tad_queue import Queue
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyQueueException, FullQueueException


class ListQueue(Queue):
    def __init__(self):
        self.queue = SinglyLinkedList()
        self.limit = None   

    def is_empty(self):
        return self.queue.is_empty()
        
    def is_full(self):
        return self.size() == self.limit       

    def size(self):
        return self.queue.size()        

    def enqueue(self, element):
        if self.is_full():
            raise FullQueueException()
        self.queue.insert_last(element)        

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException()
        return self.queue.remove_first()