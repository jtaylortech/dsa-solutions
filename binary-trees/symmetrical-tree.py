class BinaryTree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def symmetricalTree(tree):
    return treesAreSymmetrical(tree.left, tree.right)

# function that returns True if the binary tree is symmetrical and False otherwise by comparing the left and right subtrees
# the base case is when the left and right subtrees are None, in this case the binary tree is symmetrical
# the recursive case is when the left and right subtrees are not None, and their values are equal,
def treesAreSymmetrical(left, right):
    if left is not None and right is not None and left.value == right.value:
        return treesAreSymmetrical(left.left, right.right) and treesAreSymmetrical(left.right, right.left)
    
    return left == right