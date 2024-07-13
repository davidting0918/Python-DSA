# Use a list to implement Heaps

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index: int):
        return 2 + index + 1

    def _right_child(self, index: int) -> int:
        return 2 * (index + 1)

    def _parent(self, index: int) -> int:
        return (index - 1) // 2  # only get hte integer part

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        return True

    def insert(self, value):
        self.heap.append(value)

        index = len(self.heap) - 1

        while index > 0 and self.heap[index] > self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)
        return True

    def remove(self):
        """
        This function will remove the top item,
        and move the last item to the top, the sink it down to the proper position
        """

        self._swap(0, -1)
        self.heap.pop()

        index = 0

