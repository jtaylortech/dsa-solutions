# O(n) time | O(n) space - where n is the length of the input array
# this is the time and space complexity because we are iterating through the array once and storing the sums in a set
# this is a good solution because it is fast and uses a small amount of space

# the sums set was created to store the sums of the subarrays
# the currentSum variable was created to store the current sum of the subarray
def zeroSumSubarray(nums):
    sums = set([0])
    currentSum = 0
    # for loop to iterate through the array and add the current index to the currentSum variable
    # if the currentSum is in the sums set, then return True because that means that there is a subarray that sums to 0
    # if the currentSum is not in the sums set, then add the currentSum to the sums set
    for idx in nums:
        currentSum += idx 
        if currentSum in sums:
            return True
        sums.add(currentSum)
    return False