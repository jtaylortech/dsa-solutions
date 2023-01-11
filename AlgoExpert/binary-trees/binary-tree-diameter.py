class BinaryTree:
    def __init(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
# O(n) time | O(h) space
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

# the longest path between any two nodes in the current tree is the sum of the height of the left subtree and the height of the right subtree
# the diameter of the current tree is the maximum between the longest path between any two nodes in the current tree and the maximum between the diameter of the left subtree and the diameter of the right subtree
# the height of the current tree is the maximum between the height of the left subtree and the height of the right subtree plus 1
# the base case is when the current tree is None, in this case the diameter and height are both 0
# the recursive case is when the current tree is not None, in this case the algorithm calculates the diameter and height of the left and right subtrees and then uses them to calculate the diameter and height of the current tree
# the algorithm returns a TreeInfo object containing the diameter and height of the current tree
def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPath = leftTreeInfo.height + rightTreeInfo.height
    maxDiameter = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter = max(longestPath, maxDiameter)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currentDiameter, currentHeight)

class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
