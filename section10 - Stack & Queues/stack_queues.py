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


# exercise question code
# exercise 40 ~ 45
class Stack2:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if not self.stack_list:
            return None
        else:
            return self.stack_list.pop()
    def size(self):
        return len(self.stack_list)

    def is_empty(self):
        return True if self.size() == 0 else False

    def peek(self):
        if self.size() > 0:
            return self.stack_list[-1]
        return None
def is_balanced_parentheses(raw_s: str) -> bool:
    s = Stack2()
    for i in raw_s:
        if i == "(":
            s.push("(")
        elif i == ")":
            if s.size() == 0:
                return False
            s.pop()
    if s.size() > 0:
        return False

    return True


def reverse_string(raw_s: str) -> str:
    s = Stack2()

    for i in raw_s:
        s.push(i)

    result = ""
    while True:
        if s.size() == 0:
            break
        result += s.pop()
    return result

def sort_stack(stack: Stack2):
    sorted_s = Stack2()

    while not stack.is_empty():
        temp = stack.pop()

        while (not sorted_s.is_empty()) and (sorted_s.peek() > temp):
            stack.push(sorted_s.pop())

        sorted_s.push(temp)

    while not sorted_s.is_empty():
        stack.push(sorted_s.pop())


if __name__ == "__main__":
    print(is_balanced_parentheses("()()()"))


