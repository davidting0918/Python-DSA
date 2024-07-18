def bubble_sort(raw_list: list) -> list:
    for i in range(len(raw_list) - 1, 0, -1):
        for k in range(i):
            if raw_list[k] > raw_list[k+1]:
                temp = raw_list[k]
                raw_list[k] = raw_list[k+1]
                raw_list[k+1] = temp
    return raw_list


def selection_sort(raw_list: list) -> list:
    for i in range(len(raw_list) - 1):
        min_index = i
        for j in range(i + 1, len(raw_list)):
            if raw_list[j] < raw_list[min_index]:
                min_index = j

        if min_index != i:
            temp = raw_list[min_index]
            raw_list[min_index] = raw_list[i]
            raw_list[i] = temp

    return raw_list


def insertion_sort(raw_list: list) -> list:
    for i in range(1, len(raw_list)):
        temp = raw_list[i]

        j = i - 1
        while temp < raw_list[j] and j >= 0:
            raw_list[j + 1] = raw_list[j]
            raw_list[j] = temp
            j -= 1
    return raw_list



"""
Only the Big O of insertion sort is O(n) when the list is almost sorted.
"""
if __name__ == "__main__":
    l1 = [4, 2, 8, 3, 5, 7]
    print(bubble_sort(l1))

    print(selection_sort(l1))

    print(insertion_sort(l1))