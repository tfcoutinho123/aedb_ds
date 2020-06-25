from .tad_queue import Queue
from ..exceptions import EmptyQueueException, FullQueueException
import ctypes

class ArrayQueue(Queue):
    def __init__(self, size):
        self.array_size = size
        self.queue = (self.array_size * ctypes.py_object)()
        self.num_elements = 0

        for i in range(self.array_size):
            self.queue[i] = None   

    def is_empty(self):
        return self.num_elements == 0       

    def is_full(self):
        return self.num_elements == self.array_size
        

    def size(self):
        return self.num_elements
        

    def enqueue(self, element):
        if self.is_full():
            raise FullQueueException()
        for i in range(self.array_size):
            if self.queue[i] == None:
                self.queue[i] = element
                self.num_elements += 1
                break        

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException()
        element = self.queue[0]
        self.num_elements -=1  
        for i in range(self.array_size):                      
            if i == self.array_size - 1:
                self.queue[i] == None
                break
            self.queue[i] = self.queue[i+1]
        return element