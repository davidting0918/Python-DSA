def merge(l1: list, l2: list):
    result = []

    while len(l1) != 0 and len(l2) != 0:
        if l1[0] < l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))

    if l1:
        result += l1
    if l2:
        result += l2
    return result


def merge_sort(raw_list: list) -> list:  # Time complexity: O(nlogn), since merge is O(n) and we need to do divide and conquer
    if len(raw_list) == 1:
        return raw_list
    mid_index = int(len(raw_list) / 2)
    left = merge_sort(raw_list[:mid_index])
    right = merge_sort(raw_list[mid_index:])

    return merge(left, right)




if __name__ == '__main__':
    print(merge([1, 2, 7, 8], [3, 4, 5, 6]))