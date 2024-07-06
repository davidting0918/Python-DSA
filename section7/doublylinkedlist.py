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
            
        

        