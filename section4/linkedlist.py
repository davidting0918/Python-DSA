
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
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None

            self.length -= 1
            if self.length == 0:
                self.tail = None
                self.head = None

        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
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
        if index < 0 or index > self.length: # if the linked list length is 4 then index can't be 4
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

    def partition_list(self, value):
        """
        Given a value, all the node less than the value will in the first part,
        and all the node greater than or equal to the value will in the second part.
        and return should be one linked list
        """
        
        pass

    def reverse(self):
        # switch head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # start reversing
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        return True

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while True:
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            if not fast:
                slow = slow.next
                break
            slow = slow.next
        return slow

    def has_loop(self):
        """
        Main idea: if the fast one will reach a None, then the linked list doesn't have a loop

        """
        slow = self.head
        fast = self.head

        while True:
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            if not fast:
                return False
            slow = slow.next
            if slow == fast:
                return True


def find_kth_from_end(ll: LinkedList, k):
    slow = ll.head
    fast = ll.head

    # first let the fast one move k nodes ahead
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow

def print_ll(ll: LinkedList):
    print("============")
    temp = ll.head
    while temp:
        print(temp.value)
        temp = temp.next
    print("============\n")

