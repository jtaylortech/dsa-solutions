# O(n) time | O(1) space - where n is the length of the array
# this is the time and space complexity if we are not allowed to use the built-in sort method
def isMonotonic(array):
    # created a variable to keep track of the direction
    isNonIncreasing = True
    isNonDecreasing = True

    # for loop to iterate through the array
    # if the current element is less than the previous element, we set isNonDecreasing to false
    # if the current element is greater than the previous element, we set isNonIncreasing to false
    for idx in range(1, len(array)):
        if array[idx] < array[idx - 1]:
            isNonDecreasing = False
        if array[idx] > array[idx - 1]:
            isNonIncreasing = False
    
    return isNonIncreasing or isNonDecreasing

