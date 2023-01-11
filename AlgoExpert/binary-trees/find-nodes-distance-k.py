# O(n) time | O(n) space - where n is the number of nodes in the tree and h is the height of the tree
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findNodesDistanceK(tree, target, k):
    nodesDistK = []
    findDistFromNode(tree, target, k, nodesDistK)
    return nodesDistK

def findDistFromNode(node, target, k, nodesDistK):
    if node is None:
        return -1

    if node.value == target:
        addSubtreeNodesAtDistK(node, 0, k, nodesDistK)
        return 1

    leftDist = findDistFromNode(node.left, target, k, nodesDistK)
    rightDist = findDistFromNode(node.right, target, k, nodesDistK)

    if leftDist == k or rightDist == k:
        nodesDistK.append(node.value)

    if leftDist != -1:
        addSubtreeNodesAtDistK(node.right, leftDist + 1, k, nodesDistK)
        return leftDist + 1

    if rightDist != -1:
        addSubtreeNodesAtDistK(node.left, rightDist + 1, k, nodesDistK)
        return rightDist + 1

    return -1

def addSubtreeNodesAtDistK(node, dist, k, nodesDistK):
    if node is None:
        return
    if dist == k:
        nodesDistK.append(node.value)
    else:
        addSubtreeNodesAtDistK(node.left, dist + 1, k, nodesDistK)
        addSubtreeNodesAtDistK(node.right, dist + 1, k, nodesDistK)