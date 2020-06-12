
class Node():
    value = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def isLeaf(self):
        return self.left is None and self.right is None

    def branchSums(self, sum, acc):
        if self.isLeaf():
            return self.value + acc == sum
        else:
            if self.right is not None:
                sumsRightChecks = self.right.branchSums(sum, acc + self.value)
            if self.left is not None:
                sumsLeftChecks = self.left.branchSums(sum, acc + self.value)
            return sumsLeftChecks or sumsRightChecks

    def isMirrored(self):
        if self.isLeaf():
            return True
        myMirror = self.mirror()
        return self.isIdentical(myMirror)

    def mirror(self):
        newNode = Node(self.value)
        if self.left is not None:
            newNode.right = self.left.mirror()

        if self.right is not None:
            newNode.left = self.right.mirror()
        return newNode


    def isIdentical(self, other):
        if self.value != other.value:
            return False

        if self.isLeaf() and other.isLeaf():
            return self.value == other.value

        if (self.left is None and other.left is not None) or (self.left is not None and other.left is None):
            return False
        if (self.right is None and other.right is not None) or (self.right is not None and other.right is None):
            return False

        leftChecks = False
        rightChecks = False

        if self.left is not None:
            leftChecks = self.left.isIdentical(other.left)
        else:
            leftChecks = True


        if self.right is not None:
            rightChecks = self.right.isIdentical(other.right)
        else:
            rightChecks = True

        return leftChecks and rightChecks




node1 = Node(5)
node2 = Node(3)
node3 = Node(4)
node4 = Node(1)
node5 = Node(7)
node6 = Node(6)
node7 = Node(8)
node1.left = node2
node2.right = node3
node2.left = node4
node1.right = node5
node5.left = node6
node5.right = node7


#print(node1.branchSums(9,0))
#print(node5.branchSums(15,0))

#print(node1.isIdentical(node1))
node1mirror = node1.mirror()
newNode = Node(99)
newNode.left = node1
newNode.right = node1mirror
print(node1.isMirrored())
print(newNode.isMirrored())

manualMirrorTree = Node(1)

manualMirrorTree.left = Node(10)
manualMirrorTree.right = Node(10)
manualMirrorTree.left.left = Node(20)
manualMirrorTree.left.right = Node(0)
manualMirrorTree.right.right = Node(20)
manualMirrorTree.right.left = Node(0)
print(manualMirrorTree.isMirrored())


