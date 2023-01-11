class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# insert method to insert a value into the BST
# this is done by creating a new node and inserting it into the tree in the correct position 
# based on its value relative to the values of the other nodes in the tree
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self


# contains method to check if a value is contained in the BST by traversing the tree and comparing the value to the value of the current node 
# if the value is less than the current node's value, we traverse to the left child node
# if the value is greater than the current node's value, we traverse to the right child node
# if the value is equal to the current node's value, we return true 
# if we traverse to a node that is None, we return false
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False


# remove method to remove a value from the BST by traversing the tree and comparing the value to the value of the current node
# if the value is less than the current node's value, we traverse to the left child node 
# if the value is greater than the current node's value, we traverse to the right child node
# if the value is equal to the current node's value, we remove the node and return the tree
# if we traverse to a node that is None, we return the tree
# if the node to remove has no children, we remove it by setting the parent node's left or right pointer to None
# if the node to remove has one child, we remove it by setting the parent node's left or right pointer to the child node
# if the node to remove has two children, we find the smallest value in the right subtree and replace the value of the node to remove with that value
# we then remove the smallest value in the right subtree by calling the remove method on the right child node of the node to remove
    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self


# method to get the minimum value in the BST by traversing the left child nodes until we reach a node with no left child node
# this node will have the minimum value in the BST
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
                    
    
























