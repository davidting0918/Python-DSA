from unittest import TestCase

from .doublylinkedlist import DoublyLinkedList

class TestDoublyLinkedList(TestCase):
    
    def test_append(self):
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.append(3)
        dll.append(4)
        
        result = dll.unpack()
        self.assertEqual(result, [1, 2, 3, 4])
        self.assertTrue(dll.check())
        
    def test_pop(self):
        # pop a empty dll
        dll = DoublyLinkedList(1)
        dll.pop()
        self.assertEqual(dll.unpack(), [])
        
        # pop multiple nodes
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.append(3)
        dll.append(4)
        
        n = dll.pop()
        self.assertEqual(n.value, 4)
        self.assertEqual(dll.unpack(), [1, 2, 3])
        self.assertTrue(dll.check())
        
        n = dll.pop()
        self.assertEqual(n.value, 3)
        self.assertEqual(dll.unpack(), [1, 2])
        self.assertTrue(dll.check())
        
    
    def test_misc(self):
        pass
    