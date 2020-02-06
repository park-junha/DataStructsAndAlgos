class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class DoubleNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

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

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        if self.head:
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

    def peek(self):
        if self.head:
            return self.head.val
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

class BinarySearchTree:
    # Constructor
    def __init__(self):
        self.root = None

    # Recursive function for insert()
    # Insert a node, returns tree traversal string or None if duplicate node
    def insertNode(self, value, startNode):
        if value < startNode.val:
            if startNode.left:
                try:
                    ret = str(startNode.val) + " < " + self.insertNode(value, startNode.left)
                except:
                    ret = None
                return ret
            else:
                startNode.left = TreeNode(value)
                return str(startNode.val) + " < " + str(value)
        elif value > startNode.val:
            if startNode.right:
                try:
                    ret = str(startNode.val) + " > " + self.insertNode(value, startNode.right)
                except:
                    ret = None
                return ret
            else:
                startNode.right = TreeNode(value)
                return str(startNode.val) + " > " + str(value)
        else:
            return None

    # Insert a value to BST, calls recursive member function insertNode
    # If no root node, sets root node to value
    def insert(self, value):
        if self.root:
            ret = self.insertNode(value, self.root)
            return ret
        else:
            self.root = TreeNode(value)
            return str(value)

    # Recursive function for depthFirstSearchPrint()
    # Returns tree traversal string or None if value doesn't exist
    def dfsNodePrint(self, value, startNode):
        if startNode:
            if value is startNode.val:
                return " (here)"
            elif value < startNode.val:
                try:
                    ret = " -> left" + self.dfsNodePrint(value, startNode.left)
                    return ret
                except:
                    return None
            elif value > startNode.val:
                try:
                    ret = " -> right" + self.dfsNodePrint(value, startNode.right)
                    return ret
                except:
                    return None
            else:
                return None
        else:
            return None

    # Search for a value using depth-first search and print the traversal
    def depthFirstSearchPrint(self, value):
        try:
            ret = "root" + self.dfsNodePrint(value, self.root)
            return ret
        except:
            return None

    # Search for a node using depth-first search, returns Node object
    def depthFirstSearch(self, value, startNode):
        if startNode:
            if startNode.val is value:
                return startNode
            elif value < startNode.val:
                return self.depthFirstSearch(value, startNode.left)
            elif value > startNode.val:
                return self.depthFirstSearch(value, startNode.right)
        else:
            return None

    # Get the minimum value node of a tree
    def minValueNode(self, startNode):
        if startNode.left:
            ret = self.minValueNode(startNode.left)
            return ret
        else:
            return startNode

    # Remove a node from BST
    # If node doesn't exist, return None
    # If value is less than node, recursively call from left node
    # If value is greater than node, recursively call from right node
    # If node is the value to remove, remove it
    # > Replace node with right node if left node doesn't exist
    # > Replace node with left node if right node doesn't exist
    # > Otherwise, move minimum value node of right subtree to removed node
    def removeNode(self, value, startNode):
        if not startNode:
            return None
        if value < startNode.val:
            startNode.left = self.removeNode(value, startNode.left)
        elif value > startNode.val:
            startNode.right = self.removeNode(value, startNode.right)
        else:
            if not startNode.left:
                successorNode = startNode.right
                startNode = None
                return successorNode
            elif not startNode.right:
                successorNode = startNode.left
                startNode = None
                return successorNode
            successorNode = self.minValueNode(startNode.right)
            startNode.val = successorNode.val
            startNode.right = self.removeNode(successorNode.val, startNode.right)
        return startNode

    # Remove value of BST
    # Call recursive member removeNode
    def remove(self, value):
        return self.removeNode(value, self.root).val

# Implemented with Python lists, kinda defeats the purpose but oh well
# Also implemented with chaining, using stacks 
class HashTable:
    def __init__(self, bucketSize = 1000):
        self.bucketSize = bucketSize
        self.bucket = []
        for index in range(self.bucketSize):
            self.bucket.append(Stack())

    # Hashing function
    def hashKey(self, key):
        return key % self.bucketSize

    # Pushes to stack at hash ID
    def insert(self, key, value):
        hashId = self.hashKey(key)
        self.bucket[hashId].push(value)
        return hashId

    # Pops from stack at hash ID
    def remove(self, key):
        hashId = self.hashKey(key)
        ret = self.bucket[hashId].pop()
        return ret

    # Only peeks top of stack at hash ID
    def search(self, key):
        hashId = self.hashKey(key)
        ret = self.bucket[hashId].peek()
        return ret
