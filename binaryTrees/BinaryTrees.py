# class NullNode(BNode):
#     isNull = True
#     def __init__(self):
#         self.value = None
#         self.isNull = True



class BNode:
    right = None
    left = None
    value = None


    def __init__(self, value):
        self.value = value

    # def setRight(self, node):
    #     self.right = node
    #
    #
    # def setLeft(self, node):
    #     self.right = node

    def insert(self, node):
        if node.value > self.value:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
        else:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)

    def lookup(self, value):
        if value == self.value:
            return True
        elif value <= self.value:
            return self.left is not None and self.left.lookup(value)
        else:
            return self.right is not None and self.right.lookup(value)

    def countNodes(self):

        if self.right is None:
            rightChildren = 0
        else:
            rightChildren = self.right.countNodes()
        if self.left is None:
            leftChildren = 0
        else:
            leftChildren = self.left.countNodes()

        return 1+rightChildren+leftChildren

    def maxDepth(self):
        if self.right is None:
            rightDepth = 0
        else:
            rightDepth = self.right.maxDepth()

        if self.left is None:
            leftDepth = 0
        else:
            leftDepth = self.left.maxDepth()

        return 1 + max(leftDepth,rightDepth)

    def minValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.minValue()

    def inOrder(self,function):
        if self.left is not None:
            self.left.inOrder(function)
        function(self.value)
        if self.right is not None:
            self.right.inOrder(function)


    def postOrder(self,function):
        if self.left is not None:
            self.left.postOrder(function)
        if self.right is not None:
            self.right.postOrder(function)
        function(self.value)



    def hasPathSum(self, value, acum):
        if (self.right is None and self.left is None):
            return value == self.value + acum
        else:
            if self.right is not None:
                if self.right.hasPathSum(value, acum + self.value):
                    return True
            if self.left is not None:
                return self.left.hasPathSum(value, acum + self.value)
            return False

    def isLeaf(self):
        return self.right is None and self.left is None

    def printPaths(self, pathSoFar):
        pathUpdated = pathSoFar.copy()
        pathUpdated.append(self.value)
        if self.isLeaf():
            print (pathUpdated)

        if self.left is not None:
            self.left.printPaths(pathUpdated)
        if self.right is not None:
            self.right.printPaths(pathUpdated)

    def duplicate(self):
        duplicatedNode = BNode(self.value)
        oldLeft = self.left
        self.left = duplicatedNode
        self.left.left = oldLeft
        if self.left.left is not None:
            self.left.left.duplicate()
        if self.right is not None:
            self.right.duplicate()



    def mirror(self):
        r = self.right
        self.right = self.left
        self.left = r
        if self.left is not None:
            self.left.mirror()
        if self.right is not None:
            self.right.mirror()








class BTree:
    root = None

    def __init__(self):
        pass

    def insert(self, value):
        node = BNode(value)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

    def lookup(self,value):
        if self.root is None:
            return False
        return self.root.lookup(value)

    def countNodes(self):
        if self.root is None:
            return 0
        else:
            return self.root.countNodes()

    def maxDepth(self):
        if self.root is None:
            return 0
        else:
            return self.root.maxDepth()

    def minValue(self):
        if self.root is None:
            return None
        else:
            return self.root.minValue()

    def inOrder(self, function):
        if self.root is None:
            return
        else:
            self.root.inOrder(function)

    def postOrder(self, function):
        if self.root is None:
            return
        else:
            self.root.postOrder(function)

    def breadthTraverse(self, function):
        if self.root is None:
            return
        nodesInThisLevel = [self.root]

        while ( len(nodesInThisLevel) > 0 ):
            nodesInNextLevel = []

            #print ( list (map ( lambda x:x.value ,nodesInThisLevel) ) )
            for node in nodesInThisLevel:
                function(node.value)
                if node.left is not None:
                    nodesInNextLevel.append(node.left)
                if node.right is not None:
                    nodesInNextLevel.append(node.right)

            nodesInThisLevel = nodesInNextLevel

    def hasPathSum(self,value):
        if self.root is None:
            return False
        return self.root.hasPathSum(value, 0)

    def mirror(self):
        if self.root is None:
            return
        self.root.mirror()

    def printPaths(self):
        if self.root is None:
            return
        self.root.printPaths([])

    def duplicate(self):
        if self.root is None:
            return
        self.root.duplicate()




tree = BTree()
tree.insert(8)
tree.insert(6)
tree.insert(9)
tree.insert(2)
tree.insert(4)
tree.insert(5)
tree.insert(0)
tree.insert(1)
tree.insert(3)
tree.insert(7)
#print(tree.countNodes())
#print (tree.maxDepth())
#print (tree.minValue())
lista = []
#tree.postOrder(print)
#tree.inOrder(lambda x: lista.append(x))

#print (lista)


otherTree = BTree()
otherTree.insert(4)
otherTree.insert(2)
otherTree.insert(5)
otherTree.insert(1)
otherTree.insert(3)
otherTree.mirror()
#print(otherTree.root.value)
#print(otherTree.root.left.value)
#print(otherTree.root.right.value)
#print(otherTree.root.right.left.value)
#print(otherTree.root.right.right.value)

notBTree = BTree()
notBTree.root = BNode(5)
notBTree.root.left = BNode(4)
notBTree.root.left.left = BNode(11)
notBTree.root.left.left.left = BNode(7)
notBTree.root.left.left.right = BNode(2)
notBTree.root.right = BNode(8)
notBTree.root.right.left = BNode(13)
notBTree.root.right.right = BNode(4)
notBTree.root.right.right.right = BNode(1)

#print(notBTree.hasPathSum(18))
#print(notBTree.hasPathSum(22))
#print(notBTree.hasPathSum(26))
#print(notBTree.hasPathSum(27))
#print(notBTree.hasPathSum(20))

#notBTree.printPaths()


duplicatedTree = BTree()
duplicatedTree.insert(4)
duplicatedTree.insert(3)
duplicatedTree.insert(5)
duplicatedTree.insert(2)
duplicatedTree.insert(3.5)
duplicatedTree.insert(0)
duplicatedTree.insert(9)
duplicatedTree.insert(8)
duplicatedTree.duplicate()
duplicatedTree.breadthTraverse(print)
