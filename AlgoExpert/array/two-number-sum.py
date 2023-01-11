def twoNumberSum(array, targetSum):
    # since I want to use two pointers to increase or decrease the value, sorting the array is neccessary 
    # establish two pointers will be set, one at the beginning one at the end
    array.sort()
    left = 0
    right = len(array) - 1

    # while loop to move the pointers according to the returned value until the left pointer passes the right pointer
    # the current sum will always be the value of the left and right array added together
    # # if the current sum is less than target sum, move the left idx to the right 1 because that means we need a larger number
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
    

