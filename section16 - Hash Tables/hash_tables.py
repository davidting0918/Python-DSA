class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print(self):
        for i, val in enumerate(self.data_map):
            print(f"{i}: {val}")

    def set_item(self, key, value):
        index = self.__hash(key)

        if not self.data_map[index]:
            self.data_map[index] = []

        self.data_map[index].append([key, value])
        return True

    def get(self, key):
        index = self.__hash(key)

        if not self.data_map[index]:
            return None
        else:
            for i in self.data_map[index]:
                if i[0] == key:
                    return i[1]

            return None

    def keys(self):
        keys = []
        for datas in self.data_map:
            if datas:
                for data in datas:
                    keys.append(data[0])

        return keys


def item_in_common(l1: list, l2: list):
    my_dict = {
        i: True for i in l1
    }
    for i in l2:
        if i in my_dict:
            return True
    return False


def find_duplicates(l: list):
    results = []
    ht = {}
    for i in l:
        if i not in ht:
            ht[i] = True
        else:
            results.append(i)
    return results


def first_non_repeating_char(string: str):
    if not string:
        return None
    ht = {}

    for l in string:
        ht[l] = ht.get(l, 0) + 1

    for l in ht:
        if ht[l] == 1:
            return l
    return None


def group_anagrams(items: list):
    # test case: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    ht = {}
    for item in items:
        ht[item] = {}
        for letter in item:
            ht[item][letter] = ht.get(letter, 0) + 1

    results = []
    for sub_value in ht.values():
        result = [k for k, value in ht.items() if value == sub_value]
        if result not in results:
            results.append(result)
    return results
