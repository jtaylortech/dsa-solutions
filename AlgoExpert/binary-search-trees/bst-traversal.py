# if tree is not none means that the tree is not empty
# 1. traversing the left subtree
# 2. visiting the root
# 3. traversing the right subtree
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

# preOrderTraverse means that we visit the root first, then the left subtree and then the right subtree
# 1. visiting the root
# 2. traversing the left subtree
# 3. traversing the right subtree
def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

# postOrderTraverse means that we traverse the left subtree, then the right subtree and then the root
# 1. traversing the left subtree
# 2. traversing the right subtree
# 3. visiting the root
def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array