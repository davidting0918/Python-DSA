from recursive_binary_search_tree import rBST
from unittest import TestCase


class TestrBST(TestCase):
    def test_sorted_list_to_bst(self):
        nums = [0, 1, 2, 3, 4]
        rbst = rBST()

        rbst.sorted_list_to_bst(nums)
        rbst.visualize()
        return

    def test_invert_tree(self):
        nums = [0, 1, 2, 3, 4]
        rbst = rBST()

        rbst.invert()
        rbst.visualize()
        return

