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
        if not self.has_key(k):
             raise NoSuchElementException()         
        idx = self.hash_function(k)
        it = self.table[idx].iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return current_item.get_value()       
        

    def insert(self, k, v):
        if self.has_key(k):
            raise DuplicatedKeyException()
        idx = self.hash_function(k)
        item = Item(k, v)
        self.table[idx].insert_last(item)
        self.num_elements += 1

    def update(self, k, v):
        if not self.has_key(k):
            raise NoSuchElementException()            
        idx = self.hash_function(k)
        it = self.table[idx].iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                current_item.set_value(v)
                break
        

    def remove(self, k):
        if not self.has_key(k):
            raise NoSuchElementException()
        idx = self.hash_function(k)
        it = self.table[idx].iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                    self.table[idx].remove(self.table[idx].find(current_item))
                    self.num_elements -= 1
                    return current_item.get_value()               
        

    def keys(self):
        result = SinglyLinkedList()
        for i in range(self.array_size):
            for _ in range(self.table[i].size()):
                result.insert_last(self.table[i].iterator().next().get_key())
        return result

    def values(self):
        result = SinglyLinkedList()
        for i in range(self.array_size):
            for _ in range(self.table[i].size()):
                result.insert_last(self.table[i].iterator().next().get_value())
        return result

    def items(self):
        result = SinglyLinkedList()
        for i in range(self.array_size):
            for _ in range(self.table[i].size()):
                new_node = SinglyLinkedList()
                new_node.insert_last(self.table[i].iterator().next().get_key())
                new_node.insert_last(self.table[i].iterator().next().get_value())
                result.insert_last(new_node)
        return result

    def hash_function(self, k):
        return sum([ord(c) for c in k]) % self.array_size

    def has_key(self, k):
        for i in range(self.array_size):
            for _ in range(self.table[i].size()):
                if self.table[i].iterator().next().get_key() == k:
                    return True
        return False
        # idx = self.hash_function(k)
        # it = self.table[idx].iterator()
        # while it.has_next():
        #     current_item = it.next()
        #     if current_item.get_key() == k:
        #         return True
        # return False