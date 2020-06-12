#https://www.hackerrank.com/challenges/swap-nodes-algo/problem


class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def createTree(root, indexes):
    if indexes is None or len(indexes) == 0:
        return root, indexes
    if indexes[0][0] != -1:
        root.left = Node(indexes[0][0])
    if indexes[0][1] != -1:
        root.right = Node(indexes[0][1])
    del indexes[0]
    if root.left is not None:
        (left, indexes) = createTree(root.left, indexes)
    if root.right is not None:
        (right, indexes) = createTree(root.right, indexes)
    return root, indexes

def inOrder(root, f):
    if root is None:
        return
    inOrder(root.left, f)
    f(root.value)
    inOrder(root.right, f)




def swapNodes(indexes, queries):
    #print(indexes)
    #print(queries)
    result = []
    def internalSwap(root, k, actualDepth):
        if root is None:
            return
        if actualDepth % k == 0:
            aux = root.left
            root.left = root.right
            root.right = aux
        internalSwap(root.left,k,actualDepth+1)
        internalSwap(root.right,k,actualDepth+1)
        return root

    root = Node(1)
    root, _ = createTree(root, indexes)
    for i in range(len(queries)):
        root = internalSwap(root, queries[i], 1)
        a = []
        def f(value):
            a.append(value)
        inOrder(root, f)
        result.append(a)
    return result


t = swapNodes([[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]],
              [2, 3])
pass
