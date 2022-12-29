class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

# function that returns True if the binary tree is height-balanced and False otherwise
def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced

# function works by calculating the height of the left and right subtrees of the current tree
# if the absolute difference between the height of the left and right subtrees is greater than 1, the current tree is not height-balanced
# if the absolute difference between the height of the left and right subtrees is less than or equal to 1, the current tree is height-balanced
# the height of the current tree is the maximum between the height of the left subtree and the height of the right subtree plus 1
# the base case is when the current tree is None, in this case the current tree is height-balanced and the height is -1
# the recursive case is when the current tree is not None, 
# in this case the algorithm calculates the height-balanced property and height of the left and right subtrees and then uses them to calculate the height-balanced property and height of the current tree
def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(True, -1)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    isBalanced = leftTreeInfo.isBalanced and rightTreeInfo.isBalanced and abs(leftTreeInfo.height - rightTreeInfo.height) <= 1
    height = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(isBalanced, height)