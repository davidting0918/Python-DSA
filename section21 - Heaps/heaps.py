# Use a list to implement Heaps

class Heap:
    def __init__(self):
        self.heap = []

    def print(self):
        print(self.heap)

    def _left_child(self, index: int):
        return (2 * index) + 1

    def _right_child(self, index: int) -> int:
        return 2 * (index + 1)

    def _parent(self, index: int) -> int:
        return (index - 1) // 2  # only get hte integer part

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        return True

    def _sink_down(self, index):
        return NotImplemented

class MaxHeap(Heap):
    def __init__(self):
        super().__init__()

    def _sink_down(self, index):
        if index >= len(self.heap):
            return False

        max_index = index

        while True:
            l_index = self._left_child(index)
            r_index = self._right_child(index)

            if l_index < len(self.heap):
                if self.heap[l_index] > self.heap[max_index]:
                    max_index = l_index

            if r_index < len(self.heap):
                if self.heap[r_index] > self.heap[max_index]:
                    max_index = r_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

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

        if not self.heap:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()

        self._swap(0, -1)
        remove = self.heap.pop()

        self._sink_down(0)

        return remove

class MinHeap(Heap):
    def __init__(self):
        super().__init__()


    def insert(self, value):
        self.heap.append(value)

        index = len(self.heap) - 1

        while index > 0:
            parent_index = self._parent(index)
            if self.heap[parent_index] > value:
                self._swap(parent_index, index)
                index = parent_index
                continue
            break
        return True

    def _sink_down(self, index):
        if index >= len(self.heap):
            return False

        min_index = index

        while True:
            l_index = self._left_child(index)
            r_index = self._right_child(index)

            if l_index < len(self.heap):
                if self.heap[l_index] < self.heap[min_index]:
                    min_index = l_index
                    continue

            if r_index < len(self.heap):
                if self.heap[r_index] < self.heap[min_index]:
                    min_index = r_index

            if min_index != index:
                self._swap(min_index, index)
                index = min_index

            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()

        else:
            self._swap(0, -1)
            remove = self.heap.pop()

            self._sink_down(0)
            return remove


def find_kth_smallest(nums: list, k: int) -> int:
    heap = MaxHeap()
    for num in nums:
        heap.insert(num)

    while len(heap.heap) > k:
        heap.remove()

    return heap.heap[0]

def stream_max(nums: list):
    heap = MaxHeap()
    results = []
    for num in nums:
        heap.insert(num)
        results.append(heap.heap[0])

    return results
