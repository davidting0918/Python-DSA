from linkedlist import LinkedList
from unittest import TestCase


class TestLinkedList(TestCase):

    def setUp(self):
        self.ll = LinkedList(5)

        for i in [3, 8, 2, 10, 4, 1]:
            self.ll.append(i)

    def test_partition_list(self):
        self.ll.partition_list(4)
        return
