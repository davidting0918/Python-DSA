# helper function in quick sort
def _pivot(l: list, pivot: int, end: int):
    """
    This function will do 2 things:
    1. choose the first item be the pivot point and lt all the value less than on the left hand side,
       greater than at the right hand side.
    2. return the pivot point index
    """
    swap_index = pivot

    for i in range(pivot + 1, end + 1):
        if l[i] < l[pivot]:
            swap_index += 1
            _swap(l, swap_index, i)

    _swap(l, swap_index, pivot)
    return swap_index


def _swap(l: list, i1: int, i2: int):
    temp = l[i1]
    l[i1] = l[i2]
    l[i2] = temp


def quick_sort(ls: list, left: int, right: int):  # Big O is still O(n * log n)
    if left < right:
        pivot_index = _pivot(ls, left, right)
        quick_sort(ls, left, pivot_index - 1)
        quick_sort(ls, pivot_index+1, right)
    return ls


if __name__ == "__main__":
    ls = [4, 6, 1, 7, 3, 2, 5]
    print(quick_sort(ls, 0, 6))
