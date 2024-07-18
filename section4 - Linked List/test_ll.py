from linkedlist import LinkedList
from unittest import TestCase

class TestLinkedList(TestCase):
    
    def setUp(self):
        self.ll = LinkedList(1)
        
        values = [2, 3, 1, 4, 2, 5]
        
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