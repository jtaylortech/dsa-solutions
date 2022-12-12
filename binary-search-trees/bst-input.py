# input class for a BST

""" class BST creates a node for a binary search tree
each node has a value, a left child, and a right child
the left child is a node with a value less than the parent node
the right child is a node with a value greater than the parent node
the left and right children are also BSTs
the left and right children are None by default """

#def __init__ initializes the BST with a value
#self and value are the parameters for the function and self is the object that is created
#when the function is called and value is the value that is passed in when the function is called
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


