from node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        if self.tail:
            new = Node(value)
            self.tail.next = new
            self.tail = self.tail.next
        else:
            self.head = self.tail = Node(value)
        self.size += 1
        return self.size

    def dequeue(self):
        if self.head:
            rm = self.head.val
            self.head = self.head.next
            self.size -= 1
            return rm
        else:
            return None

    def printQueue(self):
        p = "queue: [ "
        current = self.head
        while current:
            p += str(current.val) + " <- "
            current = current.next
        p += "]"
        return p
