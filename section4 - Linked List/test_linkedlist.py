from linkedlist import LinkedList
from unittest import TestCase


class TestLinkedList(TestCase):

    def setUp(self):
        self.ll = LinkedList(1)

        for i in [2, 3, 4, 5]:
            self.ll.append(i)

    def test_partition_list(self):
        self.ll.partition_list(4)
        return

    def test_reverse_between(self):
        self.ll.print()
        self.ll.reverse_between(1, 3)
        self.ll.print()
        return
