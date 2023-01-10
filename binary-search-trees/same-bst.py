# O(n^2) time | O(d) space - where n is the number of nodes in each BST and d is the depth of the BST
def sameBsts(arrayOne, arrayTwo):
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))

# areSameBsts function is a helper function that takes in two arrays, two root indices, and two min and max values and returns a boolean indicating whether the BSTs are the same
# the leftRootIdxOne and leftRootIdxTwo variables are the indices of the first smaller value in the arrayOne and arrayTwo arrays, respectively and same with the rightRootIdxOne and rightRootIdxTwo variables
# the currentValue variable is the value of the current node in the BST
# the leftAreSame and rightAreSame variables are booleans indicating whether the left and right subtrees of the current node are the same
def areSameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo

    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False

    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxVal)

    currentValue = arrayOne[rootIdxOne]
    leftAreSame = areSameBsts(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
    rightAreSame = areSameBsts(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)

    return leftAreSame and rightAreSame

# getIdxOfFirstSmaller function takes in an array, a starting index, and a minimum value and returns the index of the first smaller value in the array that is greater than or equal to the minimum value
# the i variable is the index of the current value in the array and the startingIdx variable is the index of the value of the current node in the BST and the minVal variable is the minimum value of the current node in the BST
def getIdxOfFirstSmaller(array, startingIdx, minVal):
    for i in range(startingIdx + 1, len(array)):
        if array[i] < array[startingIdx] and array[i] >= minVal:
            return i
    return -1

# getIdxOfFirstBiggerOrEqual function takes in an array, a starting index, and a maximum value and returns the index of the first bigger or equal value in the array that is less than the maximum value 
# the i variable is the index of the current value in the array and the startingIdx variable is the index of the value of the current node in the BST and the maxVal variable is the maximum value of the current node in the BST
# the function returns -1 if there is no value in the array that is bigger or equal to the value of the current node in the BST and less than the maximum value
def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
    for i in range(startingIdx + 1, len(array)):
        if array[i] >= array[startingIdx] and array[i] < maxVal:
            return i
    return -1
