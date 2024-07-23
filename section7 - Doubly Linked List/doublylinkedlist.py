class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print(self):
        temp = self.head
        print("============")
        while temp:
            print(temp.value)
            temp = temp.next
        print("============\n")
        
    def unpack(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.value)
            temp = temp.next
        return result
    
    def check(self):
        r1 = []
        r2 = []
        
        temp = self.head
        while temp:
            r1.append(temp.value)
            temp = temp.next
        
        temp = self.tail
        while temp:
            r2.append(temp.value)
            temp = temp.prev
        r2.reverse()
        
        if r1 == r2:
            return True
        else:
            raise ValueError(f"Not a doubly linked list. {r1} != {r2}")
    
    def append(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        
        return True
    
    def pop(self):
        """
        pop the last node in the dll and return the node
        """
        
        if self.length == 0:
            return None
        
        else:
            temp = self.tail
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                temp.prev = None
            self.length -= 1
            return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        
        if self.length == 0:
            return None
        else:
            temp = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
                temp.next = None
            self.length -= 1
            return temp
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        new_node = Node(value)
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            prev_node = self.get(index - 1)
            next_node = prev_node.next
            
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = next_node
            next_node.prev = new_node
            self.length += 1
            return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            # Method 1
            # temp = self.get(index)
            # before = temp.prev
            # after = temp.next
            # before.next = after
            # after.prev = before
            # temp.prev = None
            # temp.next = None
            # self.length -= 1
            
            # Method 2
            temp = self.get(index)
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.length -= 1
            
            temp.next = None
            temp.prev = None
            return temp

    def swap_first_last(self):
        if not self.head:
            return

        temp = self.head.value

        self.head.value = self.tail.value
        self.tail.value = temp
        return

    def reverse(self):
        if self.length <= 1:
            return

        current = self.head

        while current:
            next = current.next
            temp = current.prev
            current.prev = current.next
            current.next = temp

            current = next

        temp = self.head
        self.head = self.tail
        self.tail = temp
        return

    def is_palindrome(self):
        if self.length <= 1:
            return True
        
        left = self.head
        right = self.tail

        while left and right:
            if left.value != right.value:
                return False
            
            left = left.next
            right = right.prev

        return True