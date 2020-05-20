import unittest

from aed_ds.lists.doubly_linked_list import DoublyLinkedList
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.lists.doubly_linked_list_iterator import DoublyLinkedListIterator
from aed_ds.exceptions import NoSuchElementException

class TestDoublyLinkedListIterator(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()
        self.iterator = self.list.iterator()

    def add_elements(self, quantity, shift=0):
        for i in range(quantity):
            self.list.insert_last(f"element {i+1+shift}")
        self.iterator = self.list.iterator()

    def test_has_next(self):
        self.assertFalse(self.iterator.has_next())

        self.add_elements(1)
        self.assertTrue(self.iterator.has_next())

        self.add_elements(1)
        self.assertTrue(self.iterator.has_next())

        self.add_elements(3)
        self.assertTrue(self.iterator.has_next())

        for _ in range(5):
            self.assertTrue(self.iterator.has_next())
            self.iterator.next()
        self.assertFalse(self.iterator.has_next())

        self.list.make_empty()
        self.iterator = self.list.iterator()
        self.assertFalse(self.iterator.has_next())


    def test_next(self):
        with self.assertRaises(NoSuchElementException):
            self.iterator.next()
        self.add_elements(1)
        self.assertEqual(self.iterator.next(), "element 1")
        self.add_elements(4, shift=1)
        self.assertEqual(self.iterator.next(), "element 1")
        self.assertEqual(self.iterator.next(), "element 2")
        self.assertEqual(self.iterator.next(), "element 3")
        self.assertEqual(self.iterator.next(), "element 4")
        self.assertEqual(self.iterator.next(), "element 5")
        with self.assertRaises(NoSuchElementException):
            self.iterator.next()

    def test_rewind(self):
        self.iterator.rewind()

        self.add_elements(5)
        
        
        for _ in range(3):
            self.iterator.next()
        self.iterator.rewind()
        self.assertTrue(self.iterator.has_next())
        self.assertEqual(self.iterator.next(), "element 1")

        
        while self.iterator.has_next():
            self.iterator.next()
        self.iterator.rewind()
        self.assertTrue(self.iterator.has_next())
        self.assertEqual(self.iterator.next(), "element 1")

    def test_has_previous(self):
        self.assertFalse(self.iterator.has_previous())

        self.add_elements(1)
        self.assertTrue(self.iterator.has_previous())

        self.add_elements(1)
        self.assertTrue(self.iterator.has_previous())

        self.add_elements(3)
        self.assertTrue(self.iterator.has_previous())

        for _ in range(5):
            self.assertTrue(self.iterator.has_previous())
            self.iterator.next()
        self.assertFalse(self.iterator.has_previous())

        self.list.make_empty()
        self.iterator = self.list.iterator()
        self.assertFalse(self.iterator.has_previous())


    def test_previous(self):
        with self.assertRaises(NoSuchElementException):
            self.iterator.previous()
        self.add_elements(1)
        self.assertEqual(self.iterator.previous(), "element 1")
        self.add_elements(4, shift=1)
        self.iterator.full_forward()
        self.assertEqual(self.iterator.previous(), "element 5")
        self.assertEqual(self.iterator.previous(), "element 4")
        self.assertEqual(self.iterator.previous(), "element 3")
        self.assertEqual(self.iterator.previous(), "element 2")
        self.assertEqual(self.iterator.previous(), "element 1")
        with self.assertRaises(NoSuchElementException):
            self.iterator.previous()

    def test_full_forward(self):
        self.iterator.full_forward()

        self.add_elements(5)
        
        
        for _ in range(3):
            self.iterator.next()
        self.iterator.full_forward()
        self.assertTrue(self.iterator.has_previous())
        self.assertEqual(self.iterator.previous(), "element 5")

        
        while self.iterator.has_previous():
            self.iterator.previous()
        self.iterator.full_forward()
        self.assertTrue(self.iterator.has_previous())
        self.assertEqual(self.iterator.previous(), "element 5")