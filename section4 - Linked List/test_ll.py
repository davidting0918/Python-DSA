from linkedlist import LinkedList
from unittest import TestCase

class TestLinkedList(TestCase):
    
    def setUp(self):
        self.ll = LinkedList(1)
        
        values = range(2, 6)
        
        for i in values:
            self.ll.append(i)
            
    def test_partition_list(self):
        value = 5
        self.ll.print()
        self.ll.partition_list(value)
        self.ll.print()
        return
    
    def test_remove_duplicated(self):
        self.ll.print()
        self.ll.remove_duplicates()
        self.ll.print()
        return

    def test_reverse_between(self):
        self.ll.print()
        self.ll.reverse_between(1, 3)
        self.ll.print()
        return
