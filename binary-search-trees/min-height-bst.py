# defines a BST class that returns a BST with the minimum height possible
def minHeightBst(array):
    return constructMinHeightBST(array, 0, len(array) - 1)

# defines the function that constructs the BST with the minimum height possible
# if the end index is less than the start index, then the BST is empty
# the middle index is the root of the BST and the left and right subtrees are constructed recursively
# the left subtree is constructed with the start index and the middle index - 1 as the end index 
# the right subtree is constructed with the middle index + 1 and the end index as the start index
def constructMinHeightBST(array, startIDX, endIDX):
    if endIDX < startIDX:
        return None
    midIDX = (startIDX + endIDX) // 2
    bst = BST(array[midIDX])
    bst.left = constructMinHeightBST(array, startIDX, midIDX - 1)
    bst.right = constructMinHeightBST(array, midIDX + 1, endIDX)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
