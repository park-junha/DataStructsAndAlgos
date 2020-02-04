from node import Node, DoubleNode

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

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def insertAtHead(self, value):
        new = DoubleNode(value)
        new.next = self.head
        if self.head:
            self.head.prev = new
        self.head = new
        if self.size is 0:
            self.tail = self.head
        self.size += 1
        return self.size

    def insertAtTail(self, value):
        new = DoubleNode(value)
        new.prev = self.tail
        if self.tail:
            self.tail.next = new
        self.tail = new
        if self.size is 0:
            self.head = self.tail
        self.size += 1
        return self.size

    def removeHead(self):
        if self.head:
            rm = self.head.val
            self.head = self.head.next
            self.size -= 1
            if not self.resetIfEmpty():
                self.head.prev = None
            return rm
        else:
            return None

    def removeTail(self):
        if self.tail:
            rm = self.tail.val
            self.tail = self.tail.prev
            self.size -= 1
            if not self.resetIfEmpty():
                self.tail.next = None
            return rm
        else:
            return None

    def resetIfEmpty(self):
        if self.size < 1:
            self.head = self.tail = None
            self.size = 0
            return True
        return False

    def printList(self):
        p = "doubly linked list: (h)[ <-> "
        current = self.head
        while current:
            p += str(current.val) + " <-> "
            current = current.next
        p += "](t)"
        return p
