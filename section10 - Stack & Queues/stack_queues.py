class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    
class Stack:  # LIFI, last in first out
    def __init__(self, value):
        node = Node(value)
        self.top = node
        self.height = 1
        
    def print(self):
        print("======")
        current = self.top
        while current:
            print(current.value)
            current = current.next
        print("======\n")
        
    def unpack(self) -> list:
        r = []
        temp = self.top
        while temp:
            r.append(temp.value)
            temp = temp.next
        return r
        
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.height += 1
        return True
    
    def pop(self):
        """
        Remove the top node from the stack
        """
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp
        
    
class Queues:  # FIFO, first in first out
    def __init__(self, value):
        node = Node(value)
        self.first = node
        self.last = node
        self.length = 1
    
    def print(self):
        print("======")
        current = self.first
        while current:
            print(current.value)
            current = current.next
        print("======\n")
    
    def unpack(self) -> list:
        r = []
        temp = self.first
        while temp:
            r.append(temp.value)
            temp = temp.next
        return r
    
    def enqueue(self, value):
        node = Node(value)
        
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
            
        self.length += 1
        return True
    
    def dequeue(self):
        
        if self.length == 0:
            return None
        else:
            temp = self.first
            self.first = temp.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.last = None
            return temp
            
    