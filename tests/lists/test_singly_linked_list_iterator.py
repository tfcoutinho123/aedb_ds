import unittest

from aed_ds.lists.singly_linked_list import SinglyLinkedList

class TestSinglyLinkedListIterator(unittest.TestCase):
    def setUp(self):
        # antes de cada test_
        pass

    def test_has_next(self):
        singly_linked_list = SinglyLinkedList()

        # 0 elements
        iterator = singly_linked_list.iterator()
        self.assertFalse(iterator.has_next())

        # 1 elements
        singly_linked_list.insert_last("element 1")
        iterator = singly_linked_list.iterator()
        self.assertTrue(iterator.has_next())

        # 2 elements
        singly_linked_list.insert_last("element 2")
        iterator = singly_linked_list.iterator()
        self.assertTrue(iterator.has_next())

        # 5 elements
        singly_linked_list.insert_last("element 3")
        singly_linked_list.insert_last("element 4")
        singly_linked_list.insert_last("element 5")
        iterator = singly_linked_list.iterator()
        self.assertTrue(iterator.has_next())

        # clear list        
        singly_linked_list.make_empty()
        iterator = singly_linked_list.iterator()
        self.assertFalse(iterator.has_next())

    # def test_next(self): pass

    # def test_rewind(self): pass
        