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
