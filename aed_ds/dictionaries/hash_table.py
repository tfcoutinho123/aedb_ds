from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList
from .item import Item

import ctypes

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.array_size = size
        self.num_elements = 0
        self.table = (self.array_size * ctypes.py_object)() #Array of Pointers

        #Create an empty list for each table position
        for i in range(self.array_size):
            self.table[i] = SinglyLinkedList()        

    def size(self):
        return self.num_elements

    def is_full(self):
        return self.num_elements == self.array_size

    def get(self, k):          
        idx = self.hash_function(k)
        it = self.table[idx].iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return current_item.get_value()
        raise NoSuchElementException()
        

    def insert(self, k, v):
        if self.has_key(k):
            raise DuplicatedKeyException()
        idx = self.hash_function(k)
        item = Item(k, v)
        self.table[idx].insert_last(item)
        self.num_elements += 1

    def update(self, k, v):            
        idx = self.hash_function(k)
        it = self.table[idx].iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                current_item.set_value(v)
        raise NoSuchElementException()

    def remove(self, k):
        idx = self.hash_function
        it = self.table[idx].iterator
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                pass                
        raise NoSuchElementException()

    def keys(self):
        result = SinglyLinkedList()
        for i in range(self.array_size-1):
            #idx = self.hash_function(i)
            it = self.table[i].iterator()
            while it.has_next():
                current_item = it.next()
                result.insert_last(current_item.get_key())
        return result

    def values(self):
        result = SinglyLinkedList()
        for i in range(self.array_size-1):
            #idx = self.hash_function(i)
            it = self.table[i].iterator()
            while it.has_next():
                current_item = it.next()
                result.insert_last(current_item.get_value())    
        return result

    def items(self):
        result = SinglyLinkedList()
        for i in range(self.array_size-1):
            #idx = self.hash_function(i)
            it = self.table[i].iterator()
            while it.has_next():
                current_item = it.next()
                result.insert_last(current_item)
        return result

    def hash_function(self, k):
        # result = 0
        # a = 101
        # for c in k:
        #     result = (result * a + ord(c)) % self.array_size
        # return result
        return sum([ord(c) for c in k]) % self.size()

    def has_key(self, k):
        idx = self.hash_function(k)
        it = self.table[idx].iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return True
        return False