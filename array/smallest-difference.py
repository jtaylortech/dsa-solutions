# O(nlog(n) + mlog(m)) time | O(1) space - where n is the length of the first array and m is the length of the second array
# this is the time complexity because we are sorting the two arrays and we are iterating through both arrays
# this is the space complexity because we are not using any additional space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    # my two pointers
    idxOne = 0
    idxTwo = 0
    #smallest differences initialized to infinity as of now
    smallest = float("inf") 
    current = float("inf")
    smallestPair = [] 
    
    # while loop to iterate through both arrays until we reach the end of one of them
    # use the two pointers to keep track of the current index of each array
    # also use the current variable to keep track of the current difference between the two values
    # also use the smallest variable to keep track of the smallest difference between the two values
    # also use the smallestPair variable to keep track of the pair of values that have the smallest difference
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        # use the if statement to check if the current difference is smaller than the smallest difference
        # if it is, we will update the smallest difference and the pair of values that have the smallest difference
        # also use the if statement to check if the first value is smaller than the second value
        # if it is, we will increment the first pointer
        # otherwise, we will increment the second pointer
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        # use the else statement to update the current difference and the pair of values that have the current difference
        else:
            return [firstNum, secondNum]
        # use the if statement to check if the current difference is smaller than the smallest difference
        # if it is, we will update the smallest difference and the pair of values that have the smallest difference
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
        
    return smallestPair