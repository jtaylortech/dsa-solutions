class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# defines a BST as a tree where all nodes to the left of a node are less than the node and all nodes to the right of a node are greater than the node
def validateBst(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))

# helper function that takes in a tree, a minimum value, and a maximum value
# the minimum value and maximum value are used to determine if the tree is a valid BST
# leftISValid is a boolean that is used to determine if the left subtree is a valid BST
# the function returns True if the tree is a valid BST and False if the tree is not a valid BST
def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True # we reached a leaf (the bottom of the tree) successfully so True is returned
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBSTHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBSTHelper(tree.right, tree.value, maxValue)
