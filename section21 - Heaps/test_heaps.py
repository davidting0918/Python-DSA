from heaps import find_kth_smallest
from unittest import TestCase

class TestHeap(TestCase):

    def test_find_kth_smallest(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 2
        find_kth_smallest(nums, k)
        return

