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
    # we will use the two pointers to keep track of the current index of each array
    # we will also use the current variable to keep track of the current difference between the two values
    # we will also use the smallest variable to keep track of the smallest difference between the two values
    # we will also use the smallestPair variable to keep track of the pair of values that have the smallest difference
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        # we will use the if statement to check if the current difference is smaller than the smallest difference
        # if it is, we will update the smallest difference and the pair of values that have the smallest difference
        # we will also use the if statement to check if the first value is smaller than the second value
        # if it is, we will increment the first pointer
        # otherwise, we will increment the second pointer
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        # we will use the else statement to update the current difference and the pair of values that have the current difference
        else:
            return [firstNum, secondNum]
        # we will use the if statement to check if the current difference is smaller than the smallest difference
        # if it is, we will update the smallest difference and the pair of values that have the smallest difference
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
        
    return smallestPair