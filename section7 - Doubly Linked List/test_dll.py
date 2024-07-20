from unittest import TestCase

from doublylinkedlist import DoublyLinkedList

class TestDoublyLinkedList(TestCase):
    def setUp(self):
        self.ddll = DoublyLinkedList(1)
    
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
        
    def test_prepend(self):
        self.ddll.prepend(2)
        self.assertEqual(self.ddll.unpack(), [2, 1])
        self.assertTrue(self.ddll.check())
        
        self.ddll.pop()
        self.ddll.pop()
        self.ddll.prepend(1)
        self.assertEqual(self.ddll.unpack(), [1])
        self.assertTrue(self.ddll.check())
        
    def test_pop_first(self):
        n = self.ddll.pop_first()
        self.assertEqual(n.value, 1)
        self.assertEqual(self.ddll.unpack(), [])
        self.assertTrue(self.ddll.check())
        
        self.ddll.append(2)
        self.ddll.append(3)
        self.ddll.pop_first()
        self.assertEqual(self.ddll.unpack(), [3])
        self.assertTrue(self.ddll.check())
    
    def test_reverse(self):
        values = range(2, 10)

        for i in values:
            self.ddll.append(i)
        self.ddll.print()
        self.ddll.reverse()
        self.ddll.print()
        return
    