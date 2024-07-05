
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        first_node = Node(value)
        self.head = first_node
        self.tail = first_node
        self.length = 1

    def append(self, value):
        # append the value to the end of the linked list
        node = Node(value)

        if not self.head or not self.tail:
            self.head = node
            self.tail = node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # remove the last value in the linked list
        if self.length == 0:
            return None
        else:
            pre = self.head
            temp = self.head
            while pre.next:
                temp = pre
                pre = pre.next
            self.tail = temp
            self.tail.next = None

            self.length -= 1
            if self.length == 0:
                self.tail = None
                self.head = None

        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.append(value)
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1

            if self.length == 0:
                self.tail = None
            return temp

    def get(self, index):
        # will return the node of that index
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length - 1:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == self.length - 1:
            return self.pop()
        elif index == 0:
            return self.pop_first()
        else:
            temp = self.get(index - 1)
            removed = temp.next
            temp.next = removed.next
            removed.next = None
            self.length -= 1
            return removed



def print_ll(ll: LinkedList):
    print("============")
    temp = ll.head
    while temp:
        print(temp.value)
        temp = temp.next
    print("============\n")


def main():
    ll = LinkedList(5)
    print_ll(ll)

    ll.append(10)
    ll.prepend(1)
    print_ll(ll)

    ll.pop_first()
    print_ll(ll)

    ll.pop()
    print_ll(ll)

    ll.pop()
    print_ll(ll)
    return


if __name__ == '__main__':
    main()