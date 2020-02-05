from node import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

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

    def insert(self, value):
        if self.root:
            ret = self.insertNode(value, self.root)
            return ret
        else:
            self.root = TreeNode(value)
            return str(value)

    def dfsNode(self, value, startNode):
        if startNode:
            if value is startNode.val:
                return " (here)"
            elif value < startNode.val:
                try:
                    ret = " -> left" + self.dfsNode(value, startNode.left)
                    return ret
                except:
                    return None
            elif value > startNode.val:
                try:
                    ret = " -> right" + self.dfsNode(value, startNode.right)
                    return ret
                except:
                    return None
            else:
                return None
        else:
            return None

    def depthFirstSearch(self, value):
        try:
            ret = "root" + self.dfsNode(value, self.root)
            return ret
        except:
            return None
