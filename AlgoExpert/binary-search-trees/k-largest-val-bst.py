class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# class to store the number of nodes visited and the latest visited node value
class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue

# function to find the kth largest value in a BST using reverse in-order traversal 
# Time: O(h + k) | Space: O(h) // h = height of the tree & k = the kth largest value to find
# Note: the time complexity is O(h + k) because we need to traverse the tree to the rightmost node and then traverse back up to the kth largest node   
# treeInfo is passed by reference so we can update the number of nodes visited and the latest visited node value
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)
    return treeInfo.latestVisitedNodeValue

# function to traverse the tree in reverse in-order 
# function works by traversing the right subtree, then the root node, then the left subtree
# the function stops when the node is None or when the number of nodes visited is equal to k
def reverseInOrderTraverse(node, k, treeInfo):
    if node is None or treeInfo.numberOfNodesVisited >= k:
        return
    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1
        treeInfo.latestVisitedNodeValue = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)
    
