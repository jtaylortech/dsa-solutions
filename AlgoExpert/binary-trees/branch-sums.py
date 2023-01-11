# This runs in O(n) time | O(n) space
def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# defines a function that takes in a binary tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum
# this is done with the help of a helper function that takes in a node, a running sum, and a list of sums
def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

# helper function that works by recursively traversing the tree and adding the value of each node to the running sum as it goes along until it reaches a leaf node 
# when it reaches a leaf node, it adds the running sum to the list of sums
# newRunningSum is the running sum plus the value of the current node which is passed into the function
# if the current node is a leaf node, it adds the newRunningSum to the list of sums and returns 
# if the current node is not a leaf node, it calls the function on the left and right subtrees
def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)