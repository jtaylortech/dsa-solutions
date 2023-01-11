# O(n) time // O(n) space - where n is the length of the input array
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# treeInfo is passed by reference to update the root index
class TreeInfo:
    def __init__(self, rootIDX):
        self.rootIDX = rootIDX

# function to reconstruct a BST from a pre-order traversal
# treeInfo is set to 0 to start at the first index of the pre-order traversal
# the lower and upper bounds are set to -inf and inf respectively to allow for any value to be inserted
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBSTFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)

# function to reconstruct a BST from a pre-order traversal
# the lower and upper bounds are used to determine if the current value is within the range of the BST
# if the current value is within the range, the value is inserted into the BST
# the root index is incremented to move to the next value in the pre-order traversal
# the left and right subtrees are recursively constructed
def reconstructBSTFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
    if currentSubtreeInfo.rootIDX == len(preOrderTraversalValues):
        return None
    
    rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIDX]
    if rootValue < lowerBound or rootValue >= upperBound:
        return None

    currentSubtreeInfo.rootIDX += 1
    leftSubtree = reconstructBSTFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
    rightSubtree = reconstructBSTFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)
    return BST(rootValue, leftSubtree, rightSubtree)