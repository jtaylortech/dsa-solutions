# O(n^2) time | O(n^2) space - where n is the length of the array 
# this is the time and space complexity of the brute force solution and the optimal solution which uses a hash table to store the sums of pairs of numbers

# all pair sums is the hash table that stores the sums of pairs of numbers in the array and the indices of the numbers that make up the sum as a list
# quadruplets is the list of quadruplets that sum up to the target sum and is returned at the end of the function
def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    # for loop to iterate through the array and find all the pairs of numbers that sum up to the target sum and store them in the hash table
    # the for loop starts at 1 and ends at the length of the array minus 1 because the first and last numbers in the array cannot be the first and last numbers in a quadruplet because there must be at least 2 numbers in between them
    for idx in range(1, len(array) - 1):
        # nested for loop is needed to find all the pairs of numbers that sum up to the target sum and store them in the hash table
        # define the current sum as the sum of the current number and the number at the current index of the outer for loop
        # define the difference as the target sum minus the current sum
        for jdx in range(idx + 1, len(array)):
            currentSum = array[idx] + array[jdx]
            difference = targetSum - currentSum
            # if the difference is in the hash table, then the difference is the sum of a pair of numbers in the array that sum up to the target sum
            # iterate through the list of pairs of numbers that sum up to the difference and append the current number and the number at the current index of the outer for loop to the list of pairs of numbers that sum up to the difference
            # append the list of pairs of numbers that sum up to the difference to the list of quadruplets
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[idx], array[jdx]])
        # this nested loop is to find all the pairs of numbers that sum up to the current sum and store them in the hash table which is needed to find the difference in the outer loop 
        # kdx is different from jdx because the current number and the number at the current index of the outer for loop cannot be the same number
        for kdx in range(0, idx):
            currentSum = array[idx] + array[kdx]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[kdx], array[idx]]]
            else:
                allPairSums[currentSum].append([array[kdx], array[idx]])

    return quadruplets