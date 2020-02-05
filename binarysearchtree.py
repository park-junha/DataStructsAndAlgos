from node import TreeNode

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

    # First attempt at remove function
    # Didn't work because it didn't delete all references to removed object
    # Return values were correct, but tree was not deleting nodes
    '''
    # Remove a node from a tree
    # Returns value of removed node if node has no children
    # Returns value of successor node if node has childrem
    # Returns None if node not found
    def originalRemove(self, value):
        nodeToRemove = self.depthFirstSearch(value, self.root)
        if nodeToRemove:
            if nodeToRemove.left and nodeToRemove.right:
                successorNode = self.minValueNode(self.root.right)
                newValue = self.remove(successorNode.val)
                nodeToRemove.val = newValue
                return nodeToRemove.val
            elif nodeToRemove.left:
                nodeToRemove = nodeToRemove.left
                return nodeToRemove.val
            elif nodeToRemove.right:
                nodeToRemove = nodeToRemove.right
                return nodeToRemove.val
            else:
                nodeToRemove = None
                return value
        else:
            return None
    '''

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
