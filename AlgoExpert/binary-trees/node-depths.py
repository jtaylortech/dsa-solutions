# O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree
# this is because the function is called on each node in the Binary Tree 
# and the space complexity is O(h) because the maximum amount of space taken up on the call stack is equal to the height of the Binary Tree
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# returns the sum of all the node depths in the Binary Tree by taking in the root node of the Binary Tree and a depth of 0 as arguments 
# with those arguments, it calls the function nodeDepths() on each side of the Binary Tree and adds the depth of the current node to the sum of the depths of the left and right subtrees
def nodeDepths(root, depth = 0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)