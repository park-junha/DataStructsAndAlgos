from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtHead(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new
        self.size += 1
        return self.size

    def find(self, value, occurrence = 1):
        index = 0
        current = self.head
        while current:
            if current.val is value:
                occurrence -= 1
                if occurrence is 0:
                    return index
            index += 1
            current = current.next
        return None

    def insertAfter(self, value, afterValue, occurrence = 1):
        current = self.head
        while current:
            if current.val is afterValue:
                occurrence -= 1
                if occurrence is 0:
                    new = Node(value)
                    new.next = current.next
                    current.next = new
                    self.size += 1
                    return self.size
            current = current.next
        return None

    def removeHead(self):
        if self.head:
            rm = self.head.val
            self.head = self.head.next
            self.size -= 1
            return rm
        else:
            return None

    def removeAfter(self, value, occurrence = 1):
        current = self.head
        if not current:
            return None
        while current.next:
            if current.val is value:
                occurrence -= 1
                if occurrence is 0:
                    rm = current.next.val
                    current.next = current.next.next
                    return rm
            current = current.next
        return None

    def printList(self):
        p = "singly linked list: [ "
        current = self.head
        while current:
            p += str(current.val) + " -> "
            current = current.next
        p += "]"
        return p
