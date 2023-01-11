# O(n^2) time | O(n) space - where n is the length of the input array 
# this is the time complexity because we are using a nested for loop and a while loop to iterate through the array
# this is the space complexity because we are creating a new array to store the triplets
def threeNumberSum(array, targetSum):
    # sort the array and create a result array
    array.sort()
    triplets = []

    # for loop to iterate through the array
    # we will use two pointers, left and right, in addition to the current number idx to find the sum
    # idx will start at i0, L will begin at i1, R is at iLEN-1
    for idx in range(len(array) - 2): 
        left = idx + 1
        right = len(array) - 1

        # while loop to iterate through the array and find the sum as long as L < R
        # if the sum is less than the target, we move L to the right
        # if the sum is greater than the target, we move R to the left
        # if the sum is equal to the target, we append the triplet to the result array
        # and move both L and R to the right and left respectively
        while left < right:
            currentSum = array[idx] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[idx], array[left], array[right]])
                left += 1 
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
                
    return triplets
        
