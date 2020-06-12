
class Node():
    def __init__(self, value):
        self.value = value
    value = None
    right = None
    left = None

def insert(node, value):
    if node is None:
        return Node(value)
    if value <= node.value:
        node.left = insert(node.left, value)
    else:
        node.right =  insert(node.right, value)
    return node

def countNodes(node):
    if node is None:
        return 0
    else:
        return countNodes(node.left) + countNodes(node.right) + 1

def inOrder(node, function):
    if node is None:
        return
    inOrder(node.left, function)
    function(node.value)
    inOrder(node.right, function)

def treeToListInternal(node):
    if node is None:
        return None
    left = node.left
    right = node.right
    leftList = treeToListInternal(node.left)

    if leftList is not None:
        lastNodeOnLeft = leftList.left
        lastNodeOnLeft.right = node
        node.right = leftList
        leftList.left = node
    else:
        leftList = node
        node.right = node
        node.left = node
    rightList = treeToListInternal(right)
    if rightList is not None:
        node.right = rightList
        rightList.left.right = leftList
        leftList.left = rightList.left
    return leftList

    # findOhterPevious = treeToListInternal(node.left, previousNode, firstNode)
    # if findOhterPevious is not None:
    #     previousNode = findOhterPevious
    #
    # if previousNode is None and firstNode is None:
    #     firstNode = node
    #
    # if previousNode is not None:
    #     previousNode.right = node
    # node.left = previousNode
    # rightSide = treeToListInternal(node.right, node, firstNode)
    # if rightSide is None:
    #     #node.right = firstNode
    #     #firstNode.left = node
    #     return node
    # return rightSide


def concatLists(listOne, listTwo):
    if listOne is None:
        return listTwo
    if listTwo is None:
        return listOne
    lastOfListOne = listOne.left
    lastOfListTwo = listTwo.left
    lastOfListOne.right = listTwo
    lastOfListTwo.right = listOne
    listOne.left = lastOfListTwo
    listTwo.left = lastOfListOne
    return listOne


def treeToList(root):
    if root is None:
        return None
    left = treeToList(root.left)
    right = treeToList(root.right)
    rootList = root
    rootList.right = rootList
    rootList.left = rootList
    leftAndRoot = concatLists(left, root)
    return concatLists(leftAndRoot, right)


def treeTolistt(node):
    if node is None:
        return None
    left = treeTolistt(node.left)
    right = treeToList(node.right)
    node.left = node
    node.right = node
    return concatListss(concatLists(left,node), right)

def concatListss(firstList, secondList):
    firstListLastNode = firstList.left
    secondListLastNode = secondList.left
    firstListLastNode.right = secondList
    secondList.left = firstListLastNode
    secondListLastNode.right = firstList
    firstList.left = secondListLastNode
    return firstList










root = insert(None,8)
root = insert(root, 6)
root = insert(root, 9)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 0)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 7)

def printear(x):
    print(x)

#print(countNodes(root))
#print(countNodes(None))
#inOrder(root, printear )
#bla = insert(None,8)
#print(bla.value)
bla = treeTolistt(root)
for i in range(20):
    #print(bla.value)
    bla = bla.left

def longestChain(node):
    if node is None:
        return 0
    pathLongitudes = []
    if len(node.children) == 0:
        return 1
    for child in node.children:
        lengthOfThisPath = longestChain(child) + 1
        pathLongitudes.append(lengthOfThisPath)
    return max(pathLongitudes)


class MultiNode():
    def __init__(self, value):
        self.value = value
        self.children = []
    value = None
    children = None

def isLeaf(node):
    return node.left is None and node.right is None

def printRootToLeaf(node, pathSoFar):
    if node is None:
        return None
    else:
        pathSoFar.append(node.value)
        if isLeaf(node):
            print(pathSoFar)
            return
        printRootToLeaf(node.left, pathSoFar.copy())
        printRootToLeaf(node.right, pathSoFar.copy())

def printRootToLeafNonRecursive(node):
    pass





node = insert(None,8)
node = insert(node, 6)
node = insert(node, 9)
node = insert(node, 2)
node = insert(node, 4)
node = insert(node, 5)
node = insert(node, 0)
node = insert(node, 1)
node = insert(node, 3)
node = insert(node, 7)
node = insert(node, 10)
node = insert(node, 11)
node = insert(node, 12)
node = insert(node, 13)
node = insert(node, 14)
node = insert(node, 15)
node = insert(node, 16)
#printRootToLeaf(node, [])


def findPairsThatSum(node, prev_value, sum, candidates, result_array):
    if node is None:
        return None
    candidates.append(node.value)
    if prev_value is not None and prev_value + node.value == sum:
        result_array.append([node.value, prev_value])
    findPairsThatSum(node.left,node.value,sum,result_array)
    findPairsThatSum(node.right,node.value,sum,result_array)
    return result_array

    #if  node.value >= sum / 2:
        # dont go right

    #else:

#print(findPairsThatSum(node,None,15,[],[]))

def validBSTNoDuplicates(node, localMax, localMin):
    if node is None:
        return True
    leftChecks = validBSTNoDuplicates(node.left, min(localMax,node.value),localMin )
    rightChecks = validBSTNoDuplicates(node.right, localMax, max(localMin, node.value))
    return node.value > localMin and node.value < localMax and leftChecks and rightChecks



print(validBSTNoDuplicates(node, 9999, -9999))

def sumTree(node):
    if node is None:
        return 0
    return node.value + sumTree(node.right) + sumTree(node.left)

def replaceWithGreaterSum(node, root):
    if node is None:
        return None
    rightSum = sumTree(node.right)
    replaceWithGreaterSum(node.right, 0)
    replaceWithGreaterSum(node.left, blindSum + rightSum + node.value)
    node.value = rightSum + blindSum

n = Node(5)
n = insert(n, 4)
n = insert(n, 3)
n = insert(n, 2)
n = insert(n, 6)
n = insert(n, 16)
n = insert(n, 11)
n = insert(n, 8)
n = insert(n, 9)

#bla = replaceWithGreaterSum(n, 0)
pass


def mirror(node):
    if node is None:
        return None
    left = node.left
    right = node.right
    node.left = right
    node.right = left
    mirror(node.left)
    mirror(node.right)

mirror(node)
pass

def height(root):
    if root is None or root.left is None and root.right is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

#print (height(n))

m = insert(None, 3)
m = insert(m, 5)
m = insert(m, 2)
m = insert(m, 1)
m = insert(m, 4)
m = insert(m, 6)
m = insert(m, 7)
#print (height(m))

def breadthFirstSearch(root, f):
    if root is None:
        return
    thisLevel = []
    nextLevel = []
    thisLevel.append(root)
    while len(thisLevel) > 0:
        for node in thisLevel:
            f(node.value)
            if node.left is not None:
                nextLevel.append(node.left)d
            if node.right is not None:
                nextLevel.append(node.right)
        thisLevel = nextLevel
        nextLevel = []
    return


breadthFirstSearch(m, print)
