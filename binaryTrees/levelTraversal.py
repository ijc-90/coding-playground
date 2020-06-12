class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def levelOrder(root):
    # Write your code here
    def height(root):
        if root is None or root.left is None and root.right is None:
            return 0
        return 1 + max(height(root.left), height(root.right))

    def visitLevel(root, h, aList):
        if root is None:
            return
        if h == 0:
            aList.append(root.info)
        else:
            visitLevel(root.left, h - 1, aList)
            visitLevel(root.right, h - 1, aList)

    h = height(root)
    aList = []
    for i in range(h+1):
        visitLevel(root, i, aList)
    print(aList)

tree = BinarySearchTree()

arr = [1,2,5,3,6,4]

for i in range(len(arr)):
    tree.create(arr[i])

levelOrder(tree.root)