from linkedlist import LinkedList
from unittest import TestCase

class TestLinkedList(TestCase):
    
    def setUp(self):
        self.ll = LinkedList(3)
        
        values = [8, 5, 10, 2, 1]
        
        for i in values:
            self.ll.append(i)
            
    def test_partition_list(self):
        value = 5
        self.ll.print()
        self.ll.partition_list(value)
        self.ll.print()
        return