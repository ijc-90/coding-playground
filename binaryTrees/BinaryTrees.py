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
            
            
    def sameTree(self, otherNode):
        lefSideEquals = False
        rightSideEquals = False
        if otherNode is None:
            return False
        if self.value != otherNode.value:
            return False
        if self.left is None:
            if otherNode.left is not None:
                return False
            else:
                lefSideEquals = True
        else:
            lefSideEquals = self.left.sameTree(otherNode.left)
            if not lefSideEquals:
                return False
        
        if self.right is None:
            if otherNode.right is not None:
                return False
            else:
                rightSideEquals = True
        else:
            rightSideEquals = self.right.sameTree(otherNode.right)
        return (lefSideEquals and rightSideEquals)


    def isBST(self, minValue, maxValue):
        ##leftPart
        if (maxValue is not None and self.value > maxValue) or (minValue is not None and self.value <= minValue):
            return False

        leftPart = False
        if self.left is None:
            leftPart = True
        else:
            if maxValue is None:
                leftPart = self.left.isBST(minValue, self.value)
            else:
                leftPart = self.left.isBST(minValue, min(maxValue,self.value))

        if self.right is None:
            rightPart = True
        else:
            if minValue is None:
                rightPart = self.right.isBST(self.value, maxValue)
            else:
                rightPart = self.right.isBST(min(minValue, self.value), maxValue)

        return leftPart and rightPart

    def findParentOfValue(self, value, parent=None):
        if self.value == value:
            return parent
        if value <= self.value:
            if self.left is not None:
                return self.left.findParentOfValue(value, self.value)
        else:
            if self.right is not None:
                return self.right.findParentOfValue(value, self.value)
        return None

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
    
    def sameTree(self, otherTree):
        if self.root is None and otherTree.root is None:
            return True
        if self.root is not None:
            return self.root.sameTree(otherTree.root)
        else:
            return False

    def isBST(self):
        if self.root is None:
            return True
        else:
            return self.root.isBST(None,None)

    def findParentOfValue(self, valueToSearch):
        return self.root.findParentOfValue(valueToSearch, None)
        




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

#print(notBTree.isBST())

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
duplicatedTree.insert(0)
duplicatedTree.insert(9)
duplicatedTree.insert(8)
#print(duplicatedTree.isBST())
duplicatedTree.duplicate()
#print(duplicatedTree.isBST())
#duplicatedTree.breadthTraverse(print)



oneTree = BTree()
oneTree.insert(4)
oneTree.insert(3)
oneTree.insert(5)
oneTree.insert(2)
oneTree.insert(0)
oneTree.insert(9)
oneTree.insert(8)

otherTree = BTree()
otherTree.insert(4)
otherTree.insert(3)
otherTree.insert(5)
otherTree.insert(2)
otherTree.insert(0)
otherTree.insert(9)
#print(oneTree.sameTree(otherTree))
#print(oneTree.sameTree(oneTree))
otherTree.insert(8)
#print(oneTree.sameTree(otherTree))
otherTree.insert(10)
#print(oneTree.sameTree(otherTree))


def countTrees(numberOfValues):
    if numberOfValues <= 1:
        return 1
    sum = 0
    for i in range(1,numberOfValues+1):
        left = countTrees(i-1)
        right = countTrees(numberOfValues-i)
        sum += left*right
    return sum


#print(countTrees(15))




#print(tree.findParentOfValue(0))
