class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#  helper function swapLeftAndRight() swaps the left and right subtrees of the current node and then calls invertBinaryTree() on each side of the Binary Tree to
#  continue swapping the left and right subtrees of the nodes in the Binary Tree
def invertBinaryTree(tree):
    if tree is None:
        return 
    swapLeftAndRight(tree)
    
    invertBinaryTree(tree.right)
    invertBinaryTree(tree.left)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left
