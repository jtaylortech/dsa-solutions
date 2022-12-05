def findClosestValueInBst(tree, target):
    # returns the closest value to the target value contained in the BST
    return findClosestValueHelper(tree, target, tree.value)


# helper function to find the closest value by comparing the absolute difference between the target and the current node value
# if the target is less than the current node value, we go left and vice versa
# if the target is equal to the current node value, we return the current node value
# tree.value is the closest value to the target value contained in the BST
def findClosestValueHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueHelper(tree.right, target, closest)
    else:
        return closest


# input tree
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None