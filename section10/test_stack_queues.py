from unittest import TestCase
from  .stack_queues import Stack
import pandas as pd

class TestStack(TestCase):
    def setUp(self):
        self.s = Stack(1)
        
        
    def test_push(self):
        self.s.push(2)
        self.assertEqual(self.s.height, 2)
        self.assertEqual(self.s.unpack(), [2, 1])
        
        self.s.pop()
        self.s.pop()
        self.s.push(3)
        self.assertEqual(self.s.height, 1)
        self.assertEqual(self.s.unpack(), [3])
    
    
    def test_pop(self):
        self.s.push(2)
        self.s.push(3)
        self.s.push(4)
        self.s.pop()
        self.assertEqual(self.s.height, 3)
        self.assertEqual(self.s.unpack(), [3, 2, 1])
        
        self.s.pop()
        self.s.pop()
        self.s.pop()
        self.assertEqual(self.s.height, 0)
        self.assertEqual(self.s.unpack(), [])
        
        self.s.pop()
        self.assertEqual(self.s.height, 0)
        self.assertEqual(self.s.unpack(), [])
        
        self.s.push(1)
        n = self.s.pop()
        self.assertEqual(n.value, 1)

class TestQueue(TestCase):
    pass