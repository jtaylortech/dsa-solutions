# O(n) time | O(h) space - where n is the number of nodes in the and h is the height of the tree
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# works by adding the values of the two trees together and returning a new tree
# if one of the trees is None, then we return the other tree
# if both trees are None, then we return None
def mergeBinaryTrees(tree1, tree2):
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1

    tree1.value += tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
    return tree1