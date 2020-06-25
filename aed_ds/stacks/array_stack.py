from .tad_stack import Stack
from ..exceptions import EmptyStackException, FullStackException
import ctypes

class ArrayStack(Stack):
    def __init__(self, size):
        self.array_size = size
        self.stack = (self.array_size * ctypes.py_object)()
        self.num_elements = 0
        
        for i in range(self.array_size):
            self.stack[i] = None 

    def is_empty(self):
        return self.num_elements == 0

    def is_full(self):
        self.num_elements == self.array_size

    def size(self):
        return self.num_elements

    def top(self):
        if self.is_empty():
            raise EmptyStackException()
        for i in range(self.array_size):
            if self.stack[i] == None:
                return self.stack[i-1]
        
    def push(self, element):
        if self.is_full():
            raise FullStackException()
        for i in range(self.array_size):
            if self.stack[i] == None:
                self.stack[i] = element
                self.num_elements += 1
                break

    def pop(self):
        if self.is_empty():
            raise EmptyStackException()
        for i in range(self.array_size):
            if self.stack[i] == None or i == self.array_size -1:
                element = self.stack[i-1]
                self.stack[i-1] = None
                self.num_elements -= 1
                return element