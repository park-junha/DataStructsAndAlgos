from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new = Node(value)
        new.next = self.top
        self.top = new
        self.size += 1
        return self.size

    def pop(self):
        if self.top:
            self.size -= 1
            rm = self.top.val
            self.top = self.top.next
            return rm
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.val
        else:
            return None

    def printStack(self):
        p = "stack: [ "
        current = self.top
        while current:
            p += "-> " + str(current.val) + " "
            current = current.next
        p += "]"
        return p
