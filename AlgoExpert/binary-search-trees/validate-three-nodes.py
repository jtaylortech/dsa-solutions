# O(h) time | O(1) space - where h is the height of the tree
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# if statement to check if nodeTwo is a descendant of nodeOne and another if statement to check if nodeThree is a descendant of nodeTwo
# if both of these statements are true, then return True
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDescendant(nodeTwo, nodeOne):
        return isDescendant(nodeThree, nodeTwo)

    if isDescendant(nodeTwo, nodeThree):
        return isDescendant(nodeOne, nodeTwo)

    return False

def isDescendant(node, target):
    while node is not None and node is not target:
        node = node.left if target.value < node.value else node.right

    return node is target
